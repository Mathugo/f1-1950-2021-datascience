# Python ETL Tools : Petl, Pandas, ApacheAirflow
from sys import displayhook
import pandas as pd
import os, glob
import kaggle
import psycopg2
from configparser import ConfigParser


USER="root"
PASSWORD="informatiquedecisionnelle"

dataset_path = 'dataset'

class ETL:
    def __init__(self, user_, password_, db_, server_="localhost", port_=5432) -> None:
        self.current_path = os.getcwd()
        
        print("[*] Connecting to %s .."%(db_))
        self.conn, self.cur = ETL.connect()
        print("[*] Done !")


    def extract(self) -> None:
        """ extract dataset from kaggle account and csv files """
        self.csv_files = glob.glob(os.path.join(dataset_path, "*.csv"))
        # getting data from kaggle 
        if not self.csv_files:
            print("[*] Downloading data from kaggle ..")
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files('mathugo/f1-1950-2020', path='./dataset', unzip=True)
            print("[*] Done")
            self.csv_files = glob.glob(os.path.join(dataset_path, "*.csv"))
        else:
            print("[*] Dataset already here")

        for f in self.csv_files:
            # read the csv file
            df = pd.read_csv(f)
            # print the location and filename
            print('Location:', f)
            print('File Name:', f.split("\\")[-1])
            
            # print the content
            print('Content:')
            displayhook(df)
            print()
    
    def transform(self):
        """ Transform data to our needs .. """
        pass

    def load(self):
        """ Load current csv to GCP BDD """
        pass

    @staticmethod
    def connect():
        """ connect to postgres server"""
        conn = None
        cur = None
        try:
            # read connection parameters
            params = ETL.config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)
		
            # create a cursor
            cur = conn.cursor()
        
            # execute a statement
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            return conn, cur

    @staticmethod
    def config(filename='database.ini', section='postgresql'):
        """ get config file for the postgres connection """
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db
        

#pandas.DataFrame.to_sql. -> apres on le stock en bdd et requete
# 1er couche 
# 2eme nettoyage, selection,
# 3eme couche, presenter les données

etl = ETL(USER, PASSWORD, 'f1-1950-2021')
"""etl.extract()
etl.transform()
etl.load()"""
