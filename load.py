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
        self.conn = ETL.connect()
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
        self.dfs = {"name" : [], "df" : [] }

        for f in self.csv_files:
            # read the csv file
            df = pd.read_csv(f)
            # print the location and filename
            print('Location:', f)
            print('File Name:', (f.split("/")[-1]).split(".csv")[0])
            
            # print the content
            print('Content:')
            displayhook(df)
            print()
            self.dfs["name"].append((f.split("/")[-1]).split(".csv")[0])
            self.dfs["df"].append(f)        
    
    def transform(self):
        """ Transform data to our needs .. """
        # remove url from data 
        pass

    def load(self):
        """ Load current csv to GCP BDD """
        #if self.create_tables():
        # self.dfs : {name: [], df: []}
        print("Number of tables : "+str(len(self.dfs["name"])))
        """
        for name, df in self.dfs.items():
            for i in range(0, len(name)):
                df[i].to_sql(name[i], self.conn, if_exists='replace', index = False)
        """

    def create_tables(self):
        """ create the tables using the sql schemas """
        with self.conn as cursor:
            cursor.execute(open("f1-1950-2021.sql", "r").read())
            return True
        return False

    def insert(self, req):
        """ Execute a single insert"""
        cur = self.conn.cursor()
        try: 
            cur.execute(req)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conn.rollback()
            cur.close()
            return 1

    @staticmethod
    def connect():
        """ connect to postgres server"""
        conn = None
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
            cur.close()

        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            return conn

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

etl.extract()
etl.transform()
etl.load()
