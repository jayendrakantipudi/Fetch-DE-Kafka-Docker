# Kafka Real-Time Stream Processing with Docker

This project sets up a real-time streaming data pipeline using Apache Kafka and Docker. It includes a Kafka producer that generates data and a Kafka consumer that processes this data to extract meaningful insights.

## Table of Contents
- [Requirements](#requirements)
- [Project Setup](#project-setup)
- [Kafka Consumer Processing](#kafka-consumer-processing)
- [Step-by-Step Guide](#step-by-step-guide)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Build and Start Docker Containers](#2-build-and-start-the-docker-containers)
  - [3. Verify Kafka Setup](#3-verify-kafka-setup)
  - [4. View Consumer Logs](#4-view-consumer-logs)
- [Data Processing Insights](#data-processing-insights)
- [Troubleshooting](#troubleshooting)
- [Conclusion](#conclusion)

## Requirements

- Docker and Docker Compose installed on your local machine.
- Internet connection to pull necessary Docker images.

## Project Setup

This project uses Docker Compose to set up the following services:
- Zookeeper: To manage and coordinate Kafka brokers.
- Kafka: To handle the messaging system.
- Data Generator: Produces messages to a Kafka topic.
- Kafka Consumer: Consumes and processes messages from the Kafka topic.

## Kafka Consumer Processing

The Kafka consumer performs the following data processing tasks:
1. **Find the most visited user**.
2. **Find the count of each different type of device**.
3. **Find the number of users from each country** based on their IP address.
4. **Find the different device types used in each country**.
5. **Find the number of users for each locale**.

## Step-by-Step Guide

### 1. Clone the Repository
```bash
git clone https://github.com/jayendrakantipudi/Fetch-DE-Kafka-Docker.git
```
### 2. Build and Start the Docker Containers
```bash
docker-compose up -d --build
```

### 3. Verify Kafka Setup
```bash
docker-compose logs -f kafka
```

### 4. View Consumer Logs
```bash
docker-compose logs -f consumer-processor
```
You can end the docker container to stop streaming the data or stop the logs using the command `CTRL+C`.

## Data Processing Insights
The insights are shown after processing every 10 messages. The `consumer_processor.py` script performs the following data processing:

- Most Visited User: Identifies the user who has the most login attempts.
- Device Type Counts: Counts how many times each device type (e.g., Android, iOS) is used.
- Device Types by Country: Lists the device types used in each country.
- Users by Locale: Counts the number of users for each locale.

<table>
  <thead>
    <tr>
      <td>Analysis</td>
      <td>Processed after 10 messages</td>
      <td>Processed after 20 messages</td>
      <td>Processed after 30 messages</td>
      <td>Processed after 40 messages</td>
      <td>Processed after 50 messages</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Most Visited User</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Device Type Counts</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Top 3 countries with most users</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Top 3 Locale with most users</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

## Conclusion
This project demonstrates setting up a real-time data processing pipeline using Kafka and Docker. By following the steps outlined in this README, you can analyze streaming data efficiently and gain insights from the processed data that continuously flows from the stream.
