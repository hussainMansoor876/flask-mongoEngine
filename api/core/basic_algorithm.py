#!/usr/bin/env python
# coding: utf-8

# Basic algorithm for API v0.1.1
#
# The basic algorithm aims at transforming an user input Excel file (CSV, XLS, XLSX) into an object of the **Dataset_core class** with the following attributes:
# - filename: the name of the Excel file including the extension
# - rows: the count of rows of the Excel file
# - columns: the count of columns of the Excel file
# - headers: the list of columns headers of the Excel file.


# Loading of the required librairies

import pandas as pd # importing pandas library
import os as os # importing os  library


# Definition of the Dataset_core class

class Dataset_core:

    def __init__(self, filepath):

        # Capture of the file's path
        # filepath expected to be a string - e.g. 'folder/spreadsheet.xlsx'

        self.filepath = filepath

        # Extraction of the file's name, including the extension

        self.filename = os.path.basename(self.filepath)

        # Opening of the file within a pandas dataframe ('df')

        if self.filename.lower().endswith(('.xls', '.xlsx')): # checking if file's extension is .xls or .xlsx
            self.df = pd.read_excel(self.filepath, sheet_name=0, header=0) # reading the Excel input file into a pandas dataframe
        elif self.filename.lower().endswith(('.csv')): # checking if file's extension is .csv
            self.df = pd.read_csv(self.filepath, header=0) # reading the CSV input file into a pandas dataframe

        # Count of the dataframe's rows and columns

        self.rows = len(self.df.index) # counting rows
        self.columns = len(self.df.columns) # counting columns

        # Capture of the dataframe's list of column headers

        self.headers = list(self.df.columns.values)


obj1 = Dataset_core('abc.txt')
print(obj1)