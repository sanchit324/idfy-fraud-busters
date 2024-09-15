from transformers import pipeline

# Define the categories
categories = {
    "Account-related information": ["account name", "account number", "transaction amount"],
    "Banking details": ["BIC", "IBAN", "Bitcoin address", "Ethereum address"],
    "Personal information": ["full name", "first name", "middle name", "last name", "gender", "date of birth"],
    "Contact information": ["email", "phone number", "street address", "building number", "city", "county", "state", "zip code"],
    "Job-related data": ["job title", "job area", "job descriptor", "job type"],
    "Financial data": ["credit card number", "issuer", "CVV", "currency code", "currency name", "currency symbol"],
    "Digital identifiers": ["IP address", "MAC address", "user agent"],
    "Online presence": ["URL", "username", "password"],
    "Other sensitive data": ["SSN", "vehicle VIN", "vehicle VRM", "phone IMEI", "GPS coordinates"]
}

# Initialize the PII detection model
model = pipeline("token-classification", model="lakshyakh93/deberta_finetuned_pii", device=-1)

# Function to classify labels into categories
def classify_pii(labels):
    classified_data = {category: [] for category in categories}
    for label in labels:
        for category, keywords in categories.items():
            if any(keyword.lower() in label.lower() for keyword in keywords):
                classified_data[category].append(label)
                break
    return classified_data

def detect_pii(text):
    predictions = model(text)
    pii_info = []
    for entity in predictions:
        entity_info = {
            'entity': entity['word'],
            'label': entity['entity']
        }
        pii_info.append(entity_info)
    
    # Extract only the labels for classification
    labels = [entity['entity'] for entity in pii_info]
    
    # Classify the labels into categories
    classified_data = classify_pii(labels)
    return pii_info, classified_data

def process_dataframe(df):
    df['Merged_Column'] = df.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    df['PII_Detected'], df['Classified_PII'] = zip(*df['Merged_Column'].apply(detect_pii))
    return df
