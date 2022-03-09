# Python ETL Tools : Petl, Pandas, ApacheAirflow
from pickle import NONE
from sys import displayhook
from venv import create
import pandas as pd
import os, glob
import kaggle
from configparser import ConfigParser
from sqlalchemy import create_engine

dataset_path = 'dataset'

class ETL:
    def __init__(self, bdd_=None) -> None:
        self.current_path = os.getcwd()
        self.conn = ETL.connect(bdd=bdd_)

    def extract(self) -> pd.DataFrame:
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
            #print('Content:')
            #displayhook(df)
            print()
            self.dfs["name"].append((f.split("/")[-1]).split(".csv")[0])
            self.dfs["df"].append(df)
        return self.dfs        
    
    def transform(self, dfs=None) -> pd.DataFrame:
        """ Transform data to our needs .. """
        # remove url from data, driver code
        print("[*] Removing url column from csv files ..")
        processed_dfs = []
        i = 0        
        if dfs != None:
            self.dfs = dfs

        for df in self.dfs["df"]:
            if (self.dfs["name"][i] == "circuits"):
                df.pop('url')
            elif (self.dfs["name"][i] == "constructors"):
                df.pop('url')
            elif (self.dfs["name"][i] == "drivers"):
                df.pop('url')
                df.pop('code')
            elif (self.dfs["name"][i] == "races"):
                df.pop('url')
            processed_dfs.append(df)
            i+=1
        self.dfs["df"] = processed_dfs
        print("[*] Done")
        return self.dfs
        
    def load(self, dfs=None) -> None:
        """ Load current csv to GCP BDD """
        if dfs == None:
            dfs = self.dfs
        print("Number of tables : "+str(len(dfs["name"])))
        for i in range(0, len(dfs["name"])):
            print("[*] Loading {} ..".format(dfs["name"][i]))           
            dfs["df"][i].to_sql(dfs["name"][i], self.conn, if_exists='replace', index = False)
            print("[*] Done ")

    def create_tables(self):
        """ create the tables using the sql schemas """
        print("[*] Creating tables using schemas ..")
        with self.conn as cursor:
            cursor.execute(open("f1-1950-2021.sql", "r").read())
            return True
        return False

    @staticmethod
    def connect(bdd=None):
        """ connect to postgres server"""
        conn = None
        try:
            # read connection parameters
            params = ETL.config()
            # connect to the PostgreSQL server
            if bdd==None:
                conn_string = 'postgresql://'+ params["user"]+ ':'+params["password"]+'@'+params["host"]+'/'+params["database"]
                bdd = params["database"]
            else:
                conn_string = 'postgresql://'+ params["user"]+ ':'+params["password"]+'@'+params["host"]+'/'+bdd
            print("[*] Connecting to the PostgreSQL database %s .."%(bdd))
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

class SecondLayer:
    def __init__(self, bdd="2-f1-1950-2021") -> None:
        print("[*] Loading data and transforming it for the second layer ..")
        self.etl = ETL(bdd_=bdd)
        self.dfs = self.etl.extract()
        self.dfs = self.etl.transform(self.dfs)
        print("[*] Done")
    
    def transform(self) -> pd.DataFrame:
        """ Transform data for the second layer """
        # remove constructor_results etc ..
        i = 0
        for df in self.dfs["df"]:

            """ remove pk to create new tuple composite pk """
            if (self.dfs["name"][i] == "results"):                
                del self.dfs["df"][i]["resultId"]
                self.dfs["df"][i]["raceId_driverId_constructorId"] = list(zip(self.dfs["df"][i].raceId, self.dfs["df"][i].driverId, self.dfs["df"][i].constructorId))
                del self.dfs["df"][i]["raceId"]
                del self.dfs["df"][i]["driverId"]
                del self.dfs["df"][i]["constructorId"]

            elif (self.dfs["name"][i] == "constructor_standings"):
                del self.dfs["df"][i]["constructorStandingsId"]
                self.dfs["df"][i]["raceId_constructorId"] = list(zip(self.dfs["df"][i]["raceId"], self.dfs["df"][i]["constructorId"]))
                del self.dfs["df"][i]["raceId"]
                del self.dfs["df"][i]["constructorId"]

            elif (self.dfs["name"][i] == "driver_standings"):
                del self.dfs["df"][i]["driverStandingsId"]
                self.dfs["df"][i]["raceId_driverId"] = list(zip(self.dfs["df"][i]["raceId"], self.dfs["df"][i]["driverId"]))
                del self.dfs["df"][i]["raceId"]
                del self.dfs["df"][i]["driverId"]
            
            if (self.dfs["name"][i] == "constructor_results"):
                del self.dfs["df"][i]
            i+=1

        self.dfs["name"].remove('constructor_results')
        return self.dfs

    def load(self, dfs=None) -> None:
        if dfs == None:
            self.etl.load(self.dfs)
        else:
            self.etl.load(dfs)

class ThirdLayer:
    def __init__(self):
        print("[*] Loading data and transforming it for the third layer ..")
        self.second_layer = SecondLayer("3-f1-1950-2021")
        self.dfs = self.second_layer.transform()
        print("[*] Done")

    def transform(self):
        """ Transform data for the third layer"""
        i=0
        for df in self.dfs["df"]:
            if (self.dfs["name"][i] == "constructor_standings"):                
                del self.dfs["df"][i]["positionText"]
            if (self.dfs["name"][i] == "driver_standings"):                
                del self.dfs["df"][i]["positionText"]
            i+=1
        return self.dfs

    def load(self):
        self.second_layer.load(self.dfs)

#pandas.DataFrame.to_sql. -> apres on le stock en bdd et requete
# 1er couche 
# 2eme nettoyage, selection, dimension fait
# 3eme couche, presenter les données

if __name__ == "__main__":
    """
    etl = ETL()
    etl.extract()
    etl.transform()
    etl.load()

    
    second = SecondLayer()
    second.transform()
    second.load()
    """

    third = ThirdLayer()
    third.transform()
    third.load()
    
    