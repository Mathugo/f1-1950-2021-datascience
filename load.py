# Python ETL Tools : Petl, Pandas, ApacheAirflow
from sys import displayhook
from venv import create
import pandas as pd
import os, glob
import kaggle
from configparser import ConfigParser
from sqlalchemy import create_engine


dataset_path = 'dataset'

class ETL:
    def __init__(self) -> None:
        self.current_path = os.getcwd()
        self.conn = ETL.connect()

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
            self.dfs["df"].append(df)        
    
    def transform(self) -> None:
        """ Transform data to our needs .. """
        # remove url from data, driver code
        print("[*] Removing url column from csv files ..")
        processed_dfs = []
        i = 0        
        for df in self.dfs["df"]:
            if (self.dfs["name"][i] == "circuits"):
                df.pop('url')
            elif (self.dfs["name"][i] == "constructors"):
                df.pop('url')
            elif (self.dfs["name"][i] == "drivers"):
                df.pop('url')
            elif (self.dfs["name"][i] == "races"):
                df.pop('url')
            df.pop('code')
            processed_dfs.append(df)
            i+=1
        self.dfs["df"] = processed_dfs
        print("[*] Done")
        
    def load(self):
        """ Load current csv to GCP BDD """
        import time
        #if self.create_tables():
        # self.dfs : {name: [], df: []}
        print("Number of tables : "+str(len(self.dfs["name"])))
        for i in range(0, len(self.dfs["name"])):
            print("[*] Loading {} ..".format(self.dfs["name"][i]))           
            self.dfs["df"][i].to_sql(self.dfs["name"][i], self.conn, if_exists='replace', index = False)
            print("[*] Done ")

    def create_tables(self):
        """ create the tables using the sql schemas """
        print("[*] Creating tables using schemas ..")
        with self.conn as cursor:
            cursor.execute(open("f1-1950-2021.sql", "r").read())
            return True
        return False

    @staticmethod
    def connect():
        """ connect to postgres server"""
        conn = None
        try:
            # read connection parameters
            params = ETL.config()
            
            # connect to the PostgreSQL server
            print("[*] Connecting to the PostgreSQL database %s .."%(params["database"]))

            #conn = psycopg2.connect(**params)
            
            conn_string = 'postgresql://'+ params["user"]+ ':'+params["password"]+'@'+params["host"]+'/'+params["database"]
            db = create_engine(conn_string)
            conn = db.connect()
            print("[*] Done !")

        except (Exception) as error:
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

if __name__ == "__main__":
    etl = ETL()
    etl.extract()
    etl.transform()
    etl.load()
