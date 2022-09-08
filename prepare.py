import acquire
import pandas as pd
from sklearn.model_selection import train_test_split

def prep_iris():
    '''
    This function acquires iris data and prepares it by:
    dropping species_id and measurement_id
    renaming species_name to species
    creating dummy variables of the species column
    concatenating those dummies back to the original dataframe. 
    '''
    df = acquire.get_iris_data()
    df = df.drop(columns=['species_id', 'measurement_id','Unnamed: 0'])
    df = df.rename({'species_name': 'species'}, axis=1)
    df_dummies = pd.get_dummies(df.species)
    df = pd.concat([df, df_dummies], axis=1)
    return df

def prep_titanic():
    '''
    This function acquires the titanic data from the mysql db and prepares it in the following way:
    drop embarked as it is duplicate of embarked_town
    drop deck as there are too many missing values. 
    drop 'Unnamed: 0'
    drop age due to number of missing values (until we come back and impute)
    '''
    df = acquire.get_titanic_data()
    cols_to_drop = ['passenger_id', 'embarked', 'Unnamed: 0', 'deck', 'age']
    df = df.drop(columns=cols_to_drop)
    df_dummies = pd.get_dummies(df[['sex', 'class', 'embark_town']], drop_first=True)
    df = pd.concat([df, df_dummies], axis=1)
    return df

def prep_telco():
    '''
    This function acquires telco data and prepares it by:
    dropping first column o indices, duplicate contract_type, internet_service_type and payment_type columns, 
    those ID columns (since we have the columns with named values now)
    creating dummy variables of the categorical columns and
    concatenating those dummies back to the original dataframe. 
    '''
    df = acquire.get_telco_data()
    cols_to_drop = ['Unnamed: 0', 'customer_id', 'contract_type.1', 'internet_service_type.1', 'payment_type.1', 'payment_type_id', 'internet_service_type_id', 'contract_type_id']
    df = df.drop(columns=cols_to_drop)
    df_dummies = pd.get_dummies(df[['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'contract_type', 'internet_service_type', 'payment_type', 'churn']], drop_first=True)
    df = pd.concat([df, df_dummies], axis=1)
    return df

def split_data(df):
    train, test_validate = train_test_split(df, test_size=.4)
    validate, test = train_test_split(test_validate, test_size=.4)
    return train, validate, test