# PII Detection and Risk Assessment App

## Overview

This is a Streamlit application designed to detect Personally Identifiable Information (PII) in data fetched from SQL databases and AWS S3 storage. The app identifies sensitive information, classifies it into categories, and computes a risk score based on the sensitivity of the PII and other factors. It also provides visualizations of the PII distribution and associated risks.

## Features

- **Data Source Options**: Fetch data from either SQL databases or AWS S3 buckets.
- **PII Detection**: Detects PII such as names, addresses, banking details, and more using a pre-trained transformer model.
- **Classification**: Automatically classifies detected PII into predefined categories.
- **Risk Assessment**: Calculates a risk score based on PII sensitivity, data volume, and regulatory compliance.
- **Visualizations**: Displays clear and informative graphs of PII distribution and risk levels.

## Data Sources

### SQL Database
- Enter the SQL Database URI and the SQL query in the input fields.
- Click on **"Fetch and Process SQL Data"** to retrieve and process the data.

### AWS S3
- Enter the AWS Access Key, Secret Access Key, Bucket Name, and File Key.
- Click on **"Fetch and Process S3 Data"** to retrieve and process the data.

## Risk Assessment
The app calculates a risk score for each piece of data based on:
- **PII Sensitivity:** The type of PII detected (e.g., account numbers, personal information, etc.).
- **Data Volume:** The amount of sensitive data present in the dataset.
- **Regulatory Compliance:** Factors such as GDPR, HIPAA, or other regulatory requirements.

The risk score is used to prioritize potential vulnerabilities in the data.

## Visualizations
The app provides three primary visualizations:
- **PII Distribution:** Shows the breakdown of PII types in the dataset.
- **Risk Distribution:** Displays the distribution of calculated risk scores.
- **PII Risk:** A combined visualization showing PII categories and associated risk levels.

## Files
- **app.py:** The main application file that handles user input, fetches data from SQL or S3, processes the data using PII detection, computes risk scores, and displays the data along with visualizations.
- **aws_handler.py:** Contains functions to connect to AWS S3 and retrieve files.
- **sql_handler.py:** Contains functions to connect to an SQL database and fetch data based on a user-provided query.
- **pii_detection.py:** This file contains the logic for detecting PII using a pre-trained transformer model and classifying the PII into predefined categories.
- **risk_assessment.py:** Calculates a risk score for each PII category based on its sensitivity, the volume of PII detected, and compliance factors.
- **visualization.py:** Includes functions to plot and display visualizations for PII distribution, risk levels, and combined PII-risk metrics.

## Dependencies
- **streamlit:** Frontend for the application
- **pandas:** Data processing
- **numpy:** Numerical computations
- **transformers:** For loading pre-trained models for PII detection
- **matplotlib & plotly:** Visualization libraries
- **boto3:** AWS S3 interaction
- **sqlalchemy:** SQL database handling

## Future Enhancements
- Add more granular risk assessment features based on industry-specific compliance requirements.
- Provide support for additional data sources (e.g., Google Cloud Storage, Azure).
- Implement custom rules for detecting specific organization-sensitive data types.

