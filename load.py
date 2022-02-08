# Python ETL Tools : Petl, Pandas, ApacheAirflow
from sys import displayhook
import pandas as pd
import os, glob
import kaggle

dataset_path = 'dataset'

class ETL:
    def __init__(self) -> None:
        self.current_path = os.getcwd()

    def extract(self) -> None:
        """ 
        extract dataset from kaggle account
        """
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

#pandas.DataFrame.to_sql. -> apres on le stock en bdd et requete
# 1er couche 
# 2eme nettoyage, selection,
# 3eme couche, presenter les données

etl = ETL()
etl.extract()
