from genericpath import isfile
import pandas as pd
import env
import os

def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''
    This function takes username, password, host and db name as arguments
    and returns a string to be used for connecting to the database. 
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    '''
    This function acquires the titanic data from the codeup mysql db, caches the file as a csv locally, 
    and returns a dataframe. If the cached version already exists, it reads the csv instead of pinging the database. 
    '''
    filename = 'titanic.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into dataframe
        df = pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        # write file to csv
        df.to_csv(filename)
        # return the dataframe
        return df

def get_iris_data():
    '''
    This function acquires the iris dataset from the codeup mysql database, caches the file as a csv locally, 
    and returns a dataframe. If the cached version already exists, it reads the csv instead of pinging the database. 
    '''
    filename = 'iris.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into dataframe
        query = 'SELECT m.*, s.species_name FROM measurements m	JOIN species s USING (species_id);'
        df = pd.read_sql(query, get_connection('iris_db'))
        # write file to csv
        df.to_csv(filename)
        # return the dataframe
        return df

def get_telco_data():
    '''
    This function acquires telco customer data from the codeup mysql database, caches the file as a csv locally, 
    and returns a dataframe. If the cached version already exists, it reads the csv instead of pinging the database. 
    '''
    filename = 'telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into dataframe
        query = 'SELECT *, ct.contract_type, ist.internet_service_type, pt.payment_type FROM customers c \
            JOIN contract_types ct USING (contract_type_id) \
                JOIN internet_service_types ist USING (internet_service_type_id) \
                    JOIN payment_types pt USING (payment_type_id);'
        df = pd.read_sql(query, get_connection('telco_churn'))

        # write file to csv
        df.to_csv(filename)

        # return dataframe
        return df