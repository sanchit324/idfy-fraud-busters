import pandas as pd

# Define sensitivity scores for different PII categories
sensitivity_scores = {
    "Account-related information": 3,
    "Banking details": 5,
    "Personal information": 4,
    "Contact information": 3,
    "Job-related data": 2,
    "Financial data": 5,
    "Digital identifiers": 4,
    "Online presence": 3,
    "Other sensitive data": 5
}

def calculate_risk_score(df):
    # Assuming df has columns 'PII_Detected' and 'Merged_Column'
    # Calculate sensitivity score based on detected PII
    df['Sensitivity_Score'] = df['PII_Detected'].apply(lambda x: sum(sensitivity_scores.get(label, 0) for label in x))

    # Calculate risk score based on volume and sensitivity
    df['Data_Volume'] = df['Merged_Column'].apply(lambda x: len(x.split()))
    df['Risk_Score'] = df['Sensitivity_Score'] * df['Data_Volume']
    
    return df
