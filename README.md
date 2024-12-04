# CS7980-ClimateDoor

# AWS Personalize Recommendation System

## Overview

This project implements a complete personalized recommendation system using **Amazon Personalize** and other AWS services such as **DynamoDB**, **Kinesis Data Streams**, **API Gateway**, **Lambda Functions**, and **S3**. The solution provides real-time tracking of user interactions and delivers personalized recommendations via REST APIs.

---

## Research Scope

As part of the **Master of Science in Computer Science (MSCS)** program at **Northeastern University**, this project aligns with the research scope of **Green Software**. It explores how cloud-based serverless architectures and machine learning solutions can be leveraged to optimize energy efficiency, reduce carbon footprints, and contribute to sustainable computing practices.

The research investigates:
- AI for User Guidance - How can AI enhance user guidance in cleantech?
- AI for Stakeholder Outreach - How can AI optimize stakeholder outreach?
- Sustainable Software Design - How can software design cut carbon emissions?
- Energy Efficiency - How can cloud scaling reduce energy waste?

A **research poster** and **demo video** accompanying this project detail the architectural design, sustainability considerations, and system performance.

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

- **Sustainability Focus**:
  - The project includes metrics to evaluate the energy efficiency of AWS components in alignment with green software principles.

---

## Additional Resources

- **Research Poster**:
  - Visualizes the architectural design and highlights sustainability goals achieved through serverless and managed AWS services.

- **Demo Video**:
  - Demonstrates the functionality of the recommendation system, including real-time event tracking, training workflows, and recommendation retrieval via API Gateway.
 
**License**
This project is licensed under the MIT License.
