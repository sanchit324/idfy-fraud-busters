import streamlit as st
import pandas as pd
from aws_handler import connect_to_s3, get_s3_file
from sql_handler import connect_to_sql, get_sql_data
from pii_detection import process_dataframe, detect_pii
from risk_assessment import calculate_risk_score 
from visualization import plot_pii_distribution, plot_risk_distribution, plot_pii_risk

def main():
    st.title("PII Detection App")

    st.sidebar.title("Team Flare")
    data_source = st.sidebar.selectbox("Choose Data Source", ["SQL Database", "AWS S3"])
    
    if data_source == "SQL Database":
        st.header("SQL Database Configuration")

        db_uri = st.text_input("Enter SQL Database URI")
        sql_query = st.text_area("Enter SQL Query")
        
        if st.button("Fetch and Process SQL Data"):
            try:
                engine = connect_to_sql(db_uri)
                sql_data = get_sql_data(engine, sql_query)
                
                st.subheader("Raw SQL Data")
                st.dataframe(sql_data)
                
                processed_data = process_dataframe(sql_data)
                risk_data = calculate_risk_score(processed_data)
                
                st.subheader("Processed Data with PII Detection and Classification")
                st.dataframe(risk_data[['Merged_Column', 'PII_Detected', 'Classified_PII', 'Risk_Score']])
                
                st.subheader("Visualizations")
                plot_pii_distribution(risk_data)
                plot_risk_distribution(risk_data)
                plot_pii_risk(risk_data)
                
            except Exception as e:
                st.error(f"Error: {e}")

    elif data_source == "AWS S3":
        st.header("AWS S3 Configuration")
        
        aws_access_key_id = st.text_input("AWS Access Key ID")
        aws_secret_access_key = st.text_input("AWS Secret Access Key", type="password")
        bucket_name = st.text_input("S3 Bucket Name")
        file_key = st.text_input("S3 File Key (e.g., path/to/file.csv)")
        
        if st.button("Fetch and Process S3 Data"):
            try:
                s3_client = connect_to_s3(aws_access_key_id, aws_secret_access_key)
                s3_data = get_s3_file(s3_client, bucket_name, file_key)

                if isinstance(s3_data, pd.DataFrame):
                    st.subheader("Raw S3 Data")
                    st.dataframe(s3_data)
                    
                    processed_data = process_dataframe(s3_data)
                    risk_data = calculate_risk_score(processed_data)
                    
                    st.subheader("Processed Data with PII Detection and Classification")
                    st.dataframe(risk_data[['Merged_Column', 'PII_Detected', 'Classified_PII', 'Risk_Score']])
                    
                    st.subheader("Visualizations")
                    plot_pii_distribution(risk_data)
                    plot_risk_distribution(risk_data)
                    plot_pii_risk(risk_data)
                    
                else:
                    st.subheader("Unstructured S3 Data")
                    st.write(s3_data)
                    
                    pii_info, classified_data = detect_pii(s3_data)
                    st.subheader("Detected PII Information")
                    st.json(pii_info)
                    st.subheader("Classified PII Information")
                    st.json(classified_data)
                    
            except Exception as e:
                st.error(f"Error: {e}")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("Made with ❤️ by Sanchit")

if __name__ == "__main__":
    main()
