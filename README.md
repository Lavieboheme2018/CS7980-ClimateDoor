# CS7980-ClimateDoor

# AWS Personalize Recommendation System

## Overview

This project implements a complete personalized recommendation system using **Amazon Personalize** and other AWS services such as **DynamoDB**, **Kinesis Data Streams**, **API Gateway**, **Lambda Functions**, and **S3**. The solution provides real-time tracking of user interactions and delivers personalized recommendations via REST APIs.

---

## Solution Architecture

The architecture consists of the following key components:

1. **Amazon Personalize**:
   - Manages dataset groups, schemas, and campaigns.
   - Trains machine learning models for personalized recommendations.

2. **Real-Time Event Tracking**:
   - **API Gateway** collects user interaction events.
   - **Kinesis Data Streams and Firehose** process and store events in S3.
   - **Lambda Functions** send interactions to **Amazon Personalize Event Tracker**.

3. **Recommendations Retrieval**:
   - API Gateway routes requests to Lambda functions that fetch recommendations from Amazon Personalize Campaigns.

---

## Features

- **Real-Time Recommendations**:
  - Provides API endpoints to fetch personalized recommendations for Tools, Grants, Incubators, and Events.
  
- **Dynamic Event Tracking**:
  - Tracks user interactions (clicks, purchases, etc.) in real-time and updates the recommendation model using Amazon Personalize Event Tracker.

- **Scalable Architecture**:
  - Built with serverless components such as Lambda, API Gateway, and Kinesis for high scalability.
