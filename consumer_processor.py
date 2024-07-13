# Required Imports
from kafka import KafkaConsumer, KafkaProducer
import json
import logging
from collections import Counter, defaultdict
import requests

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Kafka consumer and producer
consumer = KafkaConsumer(
    'user-login',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Data structures for processing
user_visits = Counter()
device_type_counts = Counter()
country_user_counts = Counter()
country_device_types = defaultdict(set)
locale_user_counts = Counter()

def get_country_from_ip(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response_data = response.json()
        return response_data.get('country', 'Unknown')
    except requests.RequestException as e:
        # logger.error(f"Error getting country from IP: {e}")
        return 'Unknown'

# Process messages
message_count = 0

for message in consumer:
    data = message.value
    try:
    
        # Increment user visits
        user_visits[data['user_id']] += 1
        

        # Increment locale user counts
        locale_user_counts[data['locale']] += 1
        
        # Increment device type counts
        device_type_counts[data['device_type']] += 1
        
        # Get country from IP and update counts
        country = get_country_from_ip(data['ip'])
        if country == 'Unknown': # Do not process if country is not known
            continue
        country_user_counts[country] += 1
        
        # Update device types for each country
        country_device_types[country].add(data['device_type'])
        
        # Optionally, produce processed data to a new topic
        processed_data = {
            'user_id': data['user_id'],
            'most_visited_user': user_visits.most_common(1)[0],
            'device_type_counts': device_type_counts,
            'country_user_counts': country_user_counts,
            'country_device_types': {k: list(v) for k, v in country_device_types.items()},
            'locale_user_counts': locale_user_counts
        }
        producer.send('processed-login', value=processed_data)
        producer.flush()
    except:
        pass
    
    # Process & Print every 10 messages
    if message_count % 10 == 0:
        logger.info(f"Most visited user: {user_visits.most_common(1)}")
        logger.info(f"Device type counts: {device_type_counts}")
        logger.info(f"Country user counts: {country_user_counts}")
        logger.info(f"Country device types: {country_device_types}")
        logger.info(f"Locale user counts: {locale_user_counts}")
    
    message_count += 1

# Print final results
logger.info(f"Most visited user: {user_visits.most_common(1)}")
logger.info(f"Device type counts: {device_type_counts}")
logger.info(f"Country user counts: {country_user_counts}")
logger.info(f"Country device types: {country_device_types}")
logger.info(f"Locale user counts: {locale_user_counts}")
