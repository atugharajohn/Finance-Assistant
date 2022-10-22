import pandas as pd
import time

def DataCleaningandFormatData():
    time.sleep(2)
    print ("\t\t\t ****** Patient Address Data ******")    
    print("Data Cleaning\n")
    file_path = 'data\\patient_addressdata.csv'
    df = pd.read_csv(file_path)
    print(df.head())
    print("Missing values:\n", df.isnull().sum())
    df = df.dropna()
    df = df.drop_duplicates()
    cleaned_file_path = 'data\\cleaned_patient_addressdata.csv'
    df.to_csv(cleaned_file_path, index=False)
    print("Cleaned data:\n", df.head())
    print("\nData Formating\n")
    cleaned_file_path = 'data\\cleaned_patient_addressdata.csv'
    df = pd.read_csv(cleaned_file_path)
    print("Data Types:\n", df.dtypes)
    formatted_file_path = 'data\\formatted_patient_data.csv'
    df.to_csv(formatted_file_path, index=False)
    print("Formatted Data:\n", df.head())
    time.sleep(2)
    print ("\t\t\t ****** Seasonal Fluctuations data ******")    
    print("Data Cleaning\n")
    file_path = 'data\\Seasonal_Fluctuationsdata.csv'
    df = pd.read_csv(file_path)
    print(df.head())
    print("Missing values:\n", df.isnull().sum())
    df = df.dropna()
    df = df.drop_duplicates()
    cleaned_file_path = 'data\\cleaned_Seasonal_Fluctuationsdata.csv'
    df.to_csv(cleaned_file_path, index=False)
    print("Cleaned data:\n", df.head())
    print("\nData Formating\n")
    cleaned_file_path = 'data\\cleaned_Seasonal_Fluctuationsdata.csv'
    df = pd.read_csv(cleaned_file_path)
    print("Data Types:\n", df.dtypes)
    formatted_file_path = 'data\\formatted_cleaned_Seasonal_Fluctuationsdata.csv'
    df.to_csv(formatted_file_path, index=False)
    print("Formatted Data:\n", df.head())
    time.sleep(2)
    print ("\t\t\t ****** Disease Patterns data ******")    
    print("Data Cleaning\n")
    file_path = 'data\\Disease_Patternsdata.csv'
    df = pd.read_csv(file_path)
    print(df.head())
    print("Missing values:\n", df.isnull().sum())
    df = df.dropna()
    df = df.drop_duplicates()
    cleaned_file_path = 'data\\cleaned_Disease_Patternsdata.csv'
    df.to_csv(cleaned_file_path, index=False)
    print("Cleaned data:\n", df.head())
    print("\nData Formating\n")
    cleaned_file_path = 'data\\cleaned_Disease_Patternsdata.csv'
    df = pd.read_csv(cleaned_file_path)
    print("Data Types:\n", df.dtypes)
    formatted_file_path = 'data\\formatted_Disease_Patternsdata.csv'
    df.to_csv(formatted_file_path, index=False)
    print("Formatted Data:\n", df.head())
