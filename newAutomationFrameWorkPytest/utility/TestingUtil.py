import calendar
import csv
import glob
import os
import pickle
import platform
import random
import re
import shutil
import string
import time
from datetime import datetime
from io import BytesIO
from pathlib import Path
from shutil import rmtree
from zipfile import ZipFile

import bitmath
import numpy as np
import pandas
import psycopg2
import requests
from psycopg2._psycopg import ProgrammingError

if platform.system() == 'Linux':
    import boto3


class TestingUtil:

    def __init__(self):
        # self._get_relative_path() = env.properties('project.path')
        # Not using env at this time due to bug in sitepackage
        super().__init__()
        self.to_ignore = ["\d\d\d\d-\d\d-\d\d[A-Z]\d\d:\d\d:\d\d.\d\d\d[A-Z]",  # example 2020-09-30T20:18:56.524Z
                          "%SKIP%", "IGNORE"]

    def dict_to_csv(self, dictionary, filename):
        keys = sorted(dictionary.keys())
        filePath = Path(self._get_relative_path()) / '_data' / filename
        with open(filePath, "w") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(keys)
            writer.writerows(zip(*[dictionary[key] for key in keys]))

    def wait_for_file_to_download(self, keyword, maxWait):
        """
        Will wait for a file matching the given keyword to download.

        Note: This wont work for large files.

        :params keyword: partial file name to look for in the _data folder.
        :params maxWait: (int) max number of seconds to wait for the download to complete.
        """
        count = 0
        while count < maxWait:
            for file in os.listdir(Path(self._get_relative_path()) / '_data'):
                filename = os.fsdecode(file)
                if keyword in filename:
                    return
            count += 1
            time.sleep(1)
        assert False, 'File not found after wait time.'

    def JSON_to_CSV_Encoding(self, json, columns, fileName, encoding=None):
        """
        Converts JSON to csv file with given encoding.

        : param json : JSON response retrieved from API POST call
        : param columns : Name of columns to include in the conversion
        : param fileName : Name of the file to be saved, including file extension
        : param encoding : Type of character encoding. OPTIONAL - leave blank/default if not needed. Ex) 'utf-8' or 'ISO-8859-1'
        : return : None
        """
        # print(json)
        columnArray = columns.split("|")

        with open(Path(self._get_relative_path()) / '_data' / fileName, "w", encoding=encoding) as file:
            if not json:
                file.writelines("EMPTY FILE")
                return
            else:
                for i in range(0, len(json)):
                    lineString = ""
                    for j in range(0, len(columnArray)):
                        if ',' in str(json[i][columnArray[j]]):
                            strValue = str(json[i][columnArray[j]])
                            strValue = strValue.replace(', ', '_')
                            lineString = lineString + strValue
                        else:
                            lineString = lineString + str(json[i][columnArray[j]])
                        if j < len(columnArray) - 1:
                            lineString = lineString + ","
                            # print(lineString)

                    file.writelines(lineString + "\n")

    def JSON_to_CSV_InvoiceLineItem(self, json, fileName, encoding=None):
        """
        Converts JSON to csv file for Invoice Line Item.

        : param json : JSON response retrieved from API POST call
        : param fileName : Name of the file to be saved, including file extension
        : param encoding : Type of character encoding. OPTIONAL - leave blank/default if not needed. Ex) 'utf-8' or 'ISO-8859-1'
        : return : None
        """
        # print(json)
        with open(Path(self._get_relative_path()) / '_data' / fileName, "w+", encoding=encoding) as file:
            if not json['_data']:
                file.writelines("EMPTY FILE")
                return
            else:
                for object in json['_data']:
                    lineString = ''
                    for item in object['fields']:
                        # replacing comma within fieldValue due to comma delimiters
                        if ',' in str(item['fieldValue']):
                            strValue = str(item['fieldValue']).strip()
                            strValue = strValue.replace(', ', '_')
                            lineString = lineString + strValue
                        else:
                            lineString = lineString + str(item['fieldValue'])
                        # check if the item is last in list and don't put an comma at end
                        if item == (object['fields'])[-1]:
                            pass
                        else:
                            lineString = lineString + ","
                    file.writelines(lineString + "\n")

    def JSON_to_CSV_InvoiceLineItemSummaries(self, json, fileName, encoding=None):
        """
        Converts JSON to csv file for Invoice Line Item Summaries.

        : param json : JSON response retrieved from API POST call
        : param fileName : Name of the file to be saved, including file extension
        : return : None
        """
        # print(json)
        with open(Path(self._get_relative_path()) / '_data' / fileName, "w", encoding=encoding) as file:
            if not json['_data']:
                file.writelines("EMPTY FILE")
                return
            else:
                for object in json['_data']:
                    lineString = str(object['summaryCode']) + ","
                    for item in object['fields']:
                        # replacing comma within fieldValue due to comma delimiters
                        if ',' in str(item['fieldValue']):
                            strValue = str(item['fieldValue'])
                            strValue = strValue.replace(', ', '_')
                            lineString = lineString + strValue
                        else:
                            lineString = lineString + str(item['fieldValue'])
                        lineString = lineString + ","

                    file.writelines(lineString + "\n")

    def JSON_to_CSV_Import(self, json, columns, fileName):
        """
        Converts JSON to csv file for Imports.

        : param json : JSON response retrieved from API POST call
        : param columns : Name of columns to include in the conversion
        : param fileName : Name of the file to be saved, including file extension
        : return : None
        """
        # print(json)
        columnArray = columns.split("|")

        with open(Path(self._get_relative_path()) / '_data' / fileName, "w", encoding='utf-8') as file:
            for i in range(0, len(json)):
                lineString = ""
                for j in range(0, len(columnArray)):
                    try:
                        lineString = lineString + str(json[i][columnArray[j]])
                        lineString = lineString + ","
                    except KeyError:
                        try:
                            lineString = lineString + str(json[i]['_auditMetadata'][columnArray[j]])
                            lineString = lineString + ","
                        except KeyError:
                            lineString = lineString + str(json[i]['_auditMetaData'][columnArray[j]])
                            lineString = lineString + ","
                # print(lineString)

                file.writelines(lineString + "\n")

    def JSON_to_CSV_Return_Information(self, json, fieldName, fileName):
        """
        Converts JSON to csv file for Return Information tab (in Report Setup).

        : param json : JSON response retrieved from API POST call
        : param fields : Category name.
        : param fileName : Name of the file to be saved, including file extension
        : return : None
        """

        with open(Path(self._get_relative_path()) / '_data' / fileName, "w") as file:
            if not json:
                file.writelines("EMPTY FILE")
                return
            else:
                for item in json[0]['sections']:
                    lineString = ""
                    if item['name'].lower() == fieldName.lower():
                        for object in item['values']:
                            if ',' in str(object['value']):
                                strValue = str(object['value'])
                                strValue = strValue.replace(', ', '_')
                                # removes the extra comma at the end
                                strValue = strValue.replace(',', '')
                                lineString = lineString + strValue
                            else:
                                lineString = lineString + str(object['value'])
                            lineString = lineString + "\n"
                    file.writelines(lineString)

    def JSON_to_CSV(self, json, columns, fileName):
        """
        Converts JSON to csv file (standard).

        : param json : JSON response retrieved from API POST call
        : param columns : Name of columns to include in the conversion
        : param fileName : Name of the file to be saved, including file extension
        : return : None
        """
        # print(json)
        columnArray = columns.split("|")

        with open(Path(self._get_relative_path()) / '_data' / fileName, "w") as file:
            if not json:
                file.writelines("EMPTY FILE")
                return
            else:
                for i in range(0, len(json)):
                    lineString = ""
                    for j in range(0, len(columnArray)):
                        if ',' in str(json[i][columnArray[j]]):
                            strValue = str(json[i][columnArray[j]])
                            strValue = strValue.replace(', ', '_')
                            lineString = lineString + strValue
                        else:
                            lineString = lineString + str(json[i][columnArray[j]])
                        if j < len(columnArray) - 1:
                            lineString = lineString + ","
                            # print(lineString)

                    file.writelines(lineString + "\n")

    def JSON_to_CSV_VITR_Format(self, json, columns, fileName, numericColumnList=None):
        """
        Converts JSON to csv file that matches the VITR format(standard).

        :param json : JSON response retrieved from API POST call
        :param columns : Name of columns to include in the conversion
        :param fileName : Name of the file to be saved, including file extension
        :param numericColumnList : List of any columns expected to be formatted with trailing 0's in decimal
        :return : None
        """

        if numericColumnList is None:
            numericColumnList = []

        with open(Path(self._get_relative_path()) / '_data' / fileName, "w", encoding='utf-8') as file:
            if not json:
                file.writelines("EMPTY FILE")
                return
            else:
                # Write the header
                file.writelines(columns + "\n")

                # Loop through and add JSON content
                for i in range(0, len(json)):
                    lineString = ""
                    # this value is used to keep the j loop aligned with the 'columnNumber' value in the JSON.
                    # This is needed because some columns are not used.
                    columnPadder = 0
                    lastColumn = len(json[i]['columns'])
                    for j in range(0, len(json[i]['columns'])):
                        # print(json[i]['columns'][j])
                        # check if this column is expected to be empty. If it is, move to the next column.
                        while json[i]['columns'][j]['columnNumber'] != j + 1 + columnPadder:
                            strValue = ""
                            lineString = lineString + ","
                            columnPadder = columnPadder + 1

                        if ',' in str(json[i]['columns'][j]['columnValue']):
                            if 'AP' in fileName or 'AR' in fileName:  # for AP/AR ledgers
                                strValue = str(json[i]['columns'][j]['columnValue']).replace(', ', '_').replace(',',
                                                                                                                '_').replace(
                                    ',', '')
                            else:
                                strValue = str(json[i]['columns'][j]['columnValue']).replace(', ', '_').replace(',', '')
                            lineString = lineString + strValue
                        else:
                            if j + columnPadder in numericColumnList:
                                columnValue = format(float(json[i]['columns'][j]['columnValue']), '.2f')
                            elif 'AP' in fileName or 'AR' in fileName:  # for AP/AR ledgers with percentages
                                columnValue = json[i]['columns'][j]['columnValue'].replace('0%', '0 %')
                            else:
                                columnValue = json[i]['columns'][j]['columnValue']
                            lineString = lineString + str(columnValue)

                        if j < len(json[i]['columns']) - 1:
                            lineString = lineString + ","

                    # Write line content to file
                    file.writelines(lineString + "\n")

    def update_VITR_baseline_to_GCView_Format(self, basefile, updatedfile, skipRows='', reportName=None):
        """
        Creates a new file in the _data folder based on a VITR baseline.  Multiple tranformations are made
        to format the file to match the GC View format.

        : param basefile : Original file to read from.  Expected to be in the GC baseline directories.
        : param updatedfile : Newly created file, written to the _data folder.
        : param skipRows : Optional. Integer type. The number of rows to skip over in the base file starting at 1. This includes
            skipping over the last row.
        : param reportName : Optional. When specified, only the formatting specified for the report should be performed.
        : return : None
        """

        if '_data' in basefile:
            base = str(Path(self._get_relative_path()) / basefile.replace('\\', '/'))
        else:
            base = str(
                Path(self._get_baseline_relative_path()) / 'GlobalComplianceBaselineFiles' / basefile.replace('\\',
                                                                                                              '/'))
        updated = str(Path(self._get_relative_path()) / '_data' / updatedfile.replace('\\', '/'))

        if skipRows:  # removing extra headers within AP/AR ledgers
            with open(base, 'r') as file:
                for _ in range(int(skipRows) - 1):
                    next(file)
                for line in file:
                    baseText = file.read()
        else:
            with open(base, 'r') as file:
                baseText = file.read()

        # temporary replacement for quotes in quotes situations
        baseText = baseText.replace('""', '####')

        # remove commas that end a string within quotes
        baseText = baseText.replace(',","', '","')

        # remove remaining quotes
        baseText = baseText.replace('"', '')

        # bring back quotes in quotes
        baseText = baseText.replace('####', '"')

        # replace listing commas in string with underscores
        baseText = baseText.replace(', ', '_')

        if reportName:
            if reportName == 'Germany Intrastat Arrivals':
                baseText = baseText.replace('99,8%', '998%')  # Germany Intrastat Arrivals
            if reportName == 'Germany Intrastat Dispatch':
                baseText = baseText.replace('0,2 mm', '02 mm')  # Germany Intrastat Dispatch
            if reportName == 'Finland Intrastat Dispatch':
                baseText = baseText.replace('8215_of base metal,', '8215_of base metal')  # Finland Intrastat Dispatch
            if reportName == 'Denmark AP/AR Ledgers':
                baseText = baseText.replace('4,11', '411')  # Denmark AP/AR Ledgers
                baseText = baseText.replace('4,11,A1', '411A1')  # Denmark AP/AR Ledgers
                baseText = baseText.replace('4,11,A2', '411A2')  # Denmark AP/AR Ledgers
                baseText = baseText.replace('1,11', '111')  # Denmark AP/AR Ledgers
                baseText = baseText.replace('2,11', '211')  # Denmark AP/AR Ledgers
                baseText = baseText.replace('3,11', '311')  # Denmark AP/AR Ledgers
            if reportName == 'Norway AP/AR Ledgers':
                baseText = baseText.replace('17,19', '1719')  # Norway AP/AR Ledgers
                baseText = baseText.replace('18,19', '1819')  # Norway AP/AR Ledgers
                baseText = baseText.replace('14,19', '1419')  # Norway AP/AR Ledgers
                baseText = baseText.replace('15,19', '1519')  # Norway AP/AR Ledgers
                baseText = baseText.replace('16,19', '1619')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,3,19', '2319')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,4,19', '2419')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,5,19', '2519')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,6', '26')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,7', '27')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,8', '28')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,9,19', '2919')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,10,19', '21019')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,11', '211')  # Norway AP/AR Ledgers
                baseText = baseText.replace('2,12,19', '21219')  # Norway AP/AR Ledgers
                baseText = baseText.replace('13,19', '1319')  # Norway AP/AR Ledgers
            if reportName == 'Ireland AP/AR Ledgers':
                baseText = baseText.replace('.,Ltd.', '._Ltd.')  # Ireland AP/AR Ledgers
                baseText = baseText.replace('Changshu,2', 'Changshu_2')  # Ireland AP/AR Ledgers
                baseText = baseText.replace('China,', 'China_')  # Ireland AP/AR Ledgers
                baseText = baseText.replace('T1,T4', 'T1_T4')  # Ireland AP/AR Ledgers
                baseText = baseText.replace('T2,T4', 'T2_T4')  # Ireland AP/AR Ledgers
                baseText = baseText.replace('T4,PA1', 'T4_PA1')  # Ireland AP/AR Ledgers
                baseText = baseText.replace('0%', '0 %')  # Ireland AP/AR Ledgers
            if reportName == 'Germany AP/AR Ledgers':
                baseText = baseText.replace('58,62', '5862')  # Germany AP/AR Ledgers
                baseText = baseText.replace('55,58,62', '555862')  # Germany AP/AR Ledgers
                baseText = baseText.replace('55,60,62', '556062')  # Germany AP/AR Ledgers
                baseText = baseText.replace('60,62', '6062')  # Germany AP/AR Ledgers
                baseText = baseText.replace('56,62', '5662')  # Germany AP/AR Ledgers
                baseText = baseText.replace('57,62', '5762')  # Germany AP/AR Ledgers
                baseText = baseText.replace('55,62', '5562')  # Germany AP/AR Ledgers
                baseText = baseText.replace('22,43', '2243')  # Germany AP/AR Ledgers
                baseText = baseText.replace('22,43,73', '224373')  # Germany AP/AR Ledgers
                baseText = baseText.replace('27,28', '2728')  # Germany AP/AR Ledgers
                baseText = baseText.replace('43,40', '4340')  # Germany AP/AR Ledgers
                baseText = baseText.replace('43,41,42,65,66', '4341426566')  # Germany AP/AR Ledgers
                baseText = baseText.replace('43,41,65,66', '43416566')  # Germany AP/AR Ledgers
                baseText = baseText.replace('43,41,42', '434142')  # Germany AP/AR Ledgers
                baseText = baseText.replace('43,41', '4341')  # Germany AP/AR Ledgers
                baseText = baseText.replace('20,43', '2043')  # Germany AP/AR Ledgers
                baseText = baseText.replace('21,43', '2143')  # Germany AP/AR Ledgers
                baseText = baseText.replace('20,43,73', '204373')  # Germany AP/AR Ledgers
                baseText = baseText.replace('21,43,73', '214373')  # Germany AP/AR Ledgers
                baseText = baseText.replace('34,43', '3443')  # Germany AP/AR Ledgers
                baseText = baseText.replace('37,43', '3743')  # Germany AP/AR Ledgers
                baseText = baseText.replace('35,43', '3543')  # Germany AP/AR Ledgers
                baseText = baseText.replace('36,43', '3643')  # Germany AP/AR Ledgers
                baseText = baseText.replace('65,66', '6566')  # Germany AP/AR Ledgers
                baseText = baseText.replace('43,42', '4342')  # Germany AP/AR Ledgers
                baseText = baseText.replace('43,40', '4340')  # Germany AP/AR Ledgers
            if reportName == 'Belgium AP/AR Ledgers':
                baseText = baseText.replace('81,82,83,86,59,YY', '8182838659YY')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83', '818283')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,84,86,61,XX', '818283848661XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,84,88,61,XX', '818283848861XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,59,YY', '81828359YY')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,85,61,XX', '8182838561XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,85', '81828385')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,87,59,YY', '8182838759YY')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,85,87,61,XX', '818283858761XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,85,63,XX', '8182838563XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('81,82,83,88,59,YY', '8182838859YY')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('01,54,XX', '0154XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('02,54,XX', '0254XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('03,54,XX', '0354XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('49,64,YY', '4964YY')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('55,XX', '55XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('62,YY', '62YY')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('57,XX', '57XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('56,XX', '56XX')  # Belgium AP/AR Ledgers
                baseText = baseText.replace('62,YY', '62YY')  # Belgium AP/AR Ledgers
            if reportName == 'France AP/AR Ledgers':
                baseText = baseText.replace('09,16,28,32', '09_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('09,16,18,28,32', '09_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('09,35,14,16,28,32', '09_35_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('10,16,28,32', '10_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('10,35,14,16,28,32', '10_35_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('11,16,28,32', '11_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('11,35,14,16,28,32', '11_35_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('13,16,28,32', '13_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('13,16,17,28,32', '13_16_17_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('13,16,18,28,32', '13_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('13,16,17,18,28,32', '13_16_17_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('15,15_1,16,28,32', '15_15_1_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('15,16,28,32', '15_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('19,20,23,28,32', '19_20_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('19,23,28,32', '19_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('19,21,23,28,32', '19_21_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('19,20,21,23,28,32', '19_20_21_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('20,23,28,32', '20_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('20,21,23,28,32', '20_21_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('20,23,2E,28,32', '20_23_2E_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('21,23,28,32', '21_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('35,36,14,16,28,32', '35_36_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('35,39,14,16,28,32', '35_39_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('35,40,14,16,28,32', '35_40_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('35,41,14,16,28,32', '35_41_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('35,44,14,16,28,32', '35_44_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('35,45,14,16,28,32', '35_45_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('36,14,16,28,32', '36_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('39,14,16,28,32', '39_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('40,14,16,28,32', '40_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('41,14,16,28,32', '41_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('44,14,16,28,32', '44_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('45,14,16,28,32', '45_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A1,B1,08,16,28,32', 'A1_B1_08_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A1,B1,08,P1,16,28,32', 'A1_B1_08_P1_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A1,A2,B1,08,P1,16,28,32',
                                            'A1_A2_B1_08_P1_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,B4', 'A2_B4')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,08,16,28,32', 'A2_08_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,9B,16,28,32', 'A2_9B_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,09,16,18,28,32', 'A2_09_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,B1,08,P1,16,18,28,32',
                                            'A2_B1_08_P1_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,B1,08,35,14,16,28,32',
                                            'A2_B1_08_35_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,B4,9B,16,28,32', 'A2_B4_9B_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,B4,08,16,28,32', 'A2_B4_08_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,B4,09,16,28,32', 'A2_B4_09_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A2,41,14,16,28,32', 'A2_41_14_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A3,9B,16,28,32', 'A3_9B_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A3,09,16,28,32', 'A3_09_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('A3,08,16,18,28,32', 'A3_08_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B1,08,P1,16,18,28,32', 'B1_08_P1_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B1,9B,16,28,32', 'B1_9B_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B1,9B,35,14,16,18,28,32',
                                            'B1_9B_35_14_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B1,P1,I1,16,28,32', 'B1_P1_I1_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B2,17', 'B2_17')  # France AP/AR Ledgers
                baseText = baseText.replace('B2,08,16,17,28,32', 'B2_08_16_17_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B2,08,16,17,18,28,32', 'B2_08_16_17_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B2,09,16,17,28,32', 'B2_09_16_17_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B2,09,16,17,18,28,32', 'B2_09_16_17_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B2,9B,16,17,18,28,32', 'B2_9B_16_17_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B3,08,16,28,32', 'B3_08_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B3,08,16,18,28,32', 'B3_08_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B3,09,16,28,32', 'B3_09_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B3,09,16,18,28,32', 'B3_09_16_18_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B3,9B,16,28,32', 'B3_9B_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B5,21,23,28,32', 'B5_21_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('B5,21,21_1,23,28,32', 'B5_21_21_1_23_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('I2,16,28,32', 'I2_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('I4,16,28,32', 'I4_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('I5,16,28,32', 'I5_16_28_32')  # France AP/AR Ledgers
                baseText = baseText.replace('E2,F7', 'E2_F7')  # France AP/AR Ledgers
                baseText = baseText.replace('0%', '0 %')  # France AP/AR Ledgers
        else:
            # specific special cases
            baseText = baseText.replace('0,4 kW', '04 kW')

        with open(updated, 'w') as file:
            file.write(baseText)

    def JSON_to_CSV_Adjustments(self, json, columns, fileName, encoding='utf-8'):
        """
        Converts JSON to csv file for Adjustment list.

        : param json : JSON response retrieved from API POST call
        : param columns : Name of columns to include in the conversion
        : param fileName : Name of the file to be saved, including file extension
        : return : None
        """
        # print(json)
        columnArray = columns.split("|")

        with open(Path(self._get_relative_path()) / '_data' / fileName, "w", encoding=encoding) as file:
            if not json:
                file.writelines("EMPTY FILE")
                return
            else:
                for i in range(0, len(json)):
                    lineString = ""
                    for j in range(0, len(columnArray)):
                        # print(str(json[i][columnArray[j]]))
                        if str(json[i][columnArray[j]]) == "startDate":
                            lineString = lineString + str(json[i]['filingRange'][columnArray[j]])
                        elif str(json[i][columnArray[j]]) == "endDate":
                            lineString = lineString + str(json[i]['filingRange'][columnArray[j]])
                        elif ',' in str(json[i][columnArray[j]]):
                            strValue = str(json[i][columnArray[j]])
                            strValue = strValue.replace(', ', '_')
                            lineString = lineString + strValue
                        else:
                            lineString = lineString + str(json[i][columnArray[j]])
                        if j < len(columnArray) - 1:
                            lineString = lineString + ","
                            # print(lineString)

                    file.writelines(lineString + "\n")

    def JSON_to_CSV_FilingReports(self, json, type, fileName):
        """
        Converts JSON to csv file for filing reports.

        : param json : JSON response from API call
        : param type : JSON type - either 'meta' or 'data'
        : param fileName : Name of the file to be saved, including file extension
        : return : None
        """
        if not json:
            with open(Path(self._get_relative_path()) / '_data' / fileName, "w") as file:
                file.writelines("EMPTY FILE")
            file.close()
            return

        if type.lower() == 'meta':
            df = pandas.DataFrame(json)
        elif type.lower() == 'data':
            df = pandas.json_normalize(json, 'columns', ['rowNumber'])
            # reorder rowNumber column to the front
            cols = df.columns.tolist()
            cols = cols[-1:] + cols[:-1]
            df = df[cols]
        else:
            assert False, "Does not match the type of JSON response. Please use either 'meta' or 'data' for type parameter."

        path = Path(self._get_relative_path()) / '_data' / fileName
        df.to_csv(path, index=False, header=True)
        # print(df)

    def compare_csv_files(self, base, actual, delimiter='', encoding='', header=0, dataDir=False, skipHeaders=False,
                          errorBadLines=None, names=None):
        """
        This component will compare two csv files.  Looks first for differences
        in row and column count followed by a cell by cell comparison.
        Differences recorded in log.

        :param base: Relative folder path to base file ("C:\\base\\baseline_file.csv") or additional folder path to the base file starting from \\GlobalComplianceBaselineFiles\\ folder ("Dashboard Baselines\\Baseline_File_Example.csv")
        :param actual:  Name of actual file, including file extension. Defaults to locating file in C:\\test\\_data\\ folder. Ex) "Actual_File_Example.csv"
        :param delimiter: Type of delimiter/separator. OPTIONAL - leave blank/default if not needed. Ex) '|' or ',' or ';'
        :param encoding: Type of character encoding. OPTIONAL - leave blank/default if not needed. Ex) 'utf-8' or 'ISO-8859-1'
        :param header: Row number to use as the column names, and the start of the data.
        :param dataDir: Set to true if baseline files are in the _data directory.
        :param skipHeaders: Optional.  If true, skips the File Headers check.
        :param errorBadLines: Optional. If None, Lines with too many fields will by default cause an exception to be raised. if False it will bypass the exception
        :param names: Optional. If None, Row number(s) to use as the column names  are inferred from the first line of the file. If passed list of integers, this will be the headers in the dataframe
        :return : None
        """
        # check if base path is defaulted baseline folder or another path location
        if dataDir:
            base = str(Path(TestingUtil()._get_project_relative_path()) / '_data' / base.replace('\\', '/'))
        else:
            base = str(
                Path(self._get_baseline_relative_path()) / 'GlobalComplianceBaselineFiles' / base.replace('\\', '/'))
            # print(base)

        # check if actual path is defaulted download folder or another path location
        actual = str(Path(self._get_relative_path()) / '_data' / actual.replace('\\', '/'))

        # Load data into pandas DF
        if delimiter == '' and encoding == '':
            baseDF = pandas.read_csv(base, header=header, error_bad_lines=errorBadLines, names=names)
            actualDF = pandas.read_csv(actual, header=header, error_bad_lines=errorBadLines, names=names)
        elif delimiter == '':
            baseDF = pandas.read_csv(base, encoding=encoding, header=header, error_bad_lines=errorBadLines,
                                     names=names)
            actualDF = pandas.read_csv(actual, encoding=encoding, header=header, error_bad_lines=errorBadLines,
                                       names=names)
        elif encoding == '':
            baseDF = pandas.read_csv(base, delimiter=delimiter, header=header, error_bad_lines=errorBadLines,
                                     names=names)
            actualDF = pandas.read_csv(actual, delimiter=delimiter, header=header, error_bad_lines=errorBadLines,
                                       names=names)
        else:
            baseDF = pandas.read_csv(base, encoding=encoding, delimiter=delimiter, header=header,
                                     error_bad_lines=errorBadLines, names=names)
            actualDF = pandas.read_csv(actual, encoding=encoding, delimiter=delimiter, header=header,
                                       error_bad_lines=errorBadLines, names=names)

        # Compare DF sizes
        assert baseDF.shape == actualDF.shape, \
            f'The number of columns or rows does not match in the two files.\n' \
            f'Base: {baseDF.shape[0]} rows, {baseDF.shape[1]} columns.\n' \
            f'Actual: {actualDF.shape[0]} rows, {actualDF.shape[1]} columns. '

        # Compare DF Data
        # print(dir(baseDF))
        print('Start compare')
        baseDF = baseDF.replace(np.nan, '', regex=True)
        actualDF = actualDF.replace(np.nan, '', regex=True)
        baseDict = baseDF.to_dict()
        actualDict = actualDF.to_dict()
        failureList = []
        for baseKey, actualKey in zip(baseDict, actualDict):
            if (skipHeaders == False):
                assert str(baseKey).strip() == str(
                    actualKey).strip(), f'Files headers do not match. Base is |{baseKey}|. Actual is |{actualKey}|'

            for key in baseDict[baseKey]:
                baseValue = baseDict[baseKey][key]
                actualValue = actualDict[actualKey][key]
                # checking for timestamp/date (snapshot)
                for exp in self.to_ignore:
                    if re.search(exp, str(baseValue)):
                        # print("Skip timestamp/date")
                        break
                else:
                    if self._convert_to_float(str(baseValue).strip()) != self._convert_to_float(
                            str(actualValue).strip()):
                        failureList.append(
                            f'Row \'{key + 1}\', Column \'{baseKey}\' Base is \'{baseValue}\'. Actual is \'{actualValue}\'')

        if failureList:
            errorCount = len(failureList)
            print(f'{errorCount} Differences found:')
            for error in sorted(failureList, key=lambda x: int(re.match(r'Row \'(\d+)', x).groups()[0])):
                print('ERROR:', error)
            assert False, ('Differences found.  See list above with ', errorCount, ' errors.')
        else:
            print('Compare complete, no differences found.')

    def compare_csv_files_inTestFolder(self, base, actual, delimiter='', encoding='', header=0):
        """
        This component will compare two csv files.  Looks first for differences
        in row and column count followed by a cell by cell comparison.
        Differences recorded in log.

        : param base : Relative folder path to base file ("C:\\base\\baseline_file.csv") or additional folder path to the base file starting from \\GlobalComplianceBaselineFiles\\ folder ("Dashboard Baselines\\Baseline_File_Example.csv")
        : param actual : Name of actual file, including file extension. Defaults to locating file in C:\\test\\_data\\ folder. Ex) "Actual_File_Example.csv"
        : param delimiter : Type of delimiter/separator. OPTIONAL - leave blank/default if not needed. Ex) '|' or ',' or ';'
        : param encoding : Type of character encoding. OPTIONAL - leave blank/default if not needed. Ex) 'utf-8' or 'ISO-8859-1'
        : return : None
        """
        # check if base path is defaulted baseline folder or another path location
        if "C:\\" in str(base):
            base = str(base)
        else:
            base = str(Path(self._get_relative_path()) / '_data' / base.replace('\\', '/'))
            # print(base)

        # check if actual path is defaulted download folder or another path location
        if "C:\\" in str(actual) or "C:/" in str(actual):
            actual = str(actual)
        else:
            actual = str(Path(self._get_relative_path()) / '_data' / actual.replace('\\', '/'))

        # Load data into pandas DF
        if delimiter == '' and encoding == '':
            baseDF = pandas.read_csv(base, header=header)
            actualDF = pandas.read_csv(actual, header=header)
        elif delimiter == '':
            baseDF = pandas.read_csv(base, encoding=encoding, header=header)
            actualDF = pandas.read_csv(actual, encoding=encoding, header=header)
        elif encoding == '':
            baseDF = pandas.read_csv(base, delimiter=delimiter, header=header)
            actualDF = pandas.read_csv(actual, delimiter=delimiter, header=header)
        else:
            baseDF = pandas.read_csv(base, encoding=encoding, delimiter=delimiter, header=header)
            actualDF = pandas.read_csv(actual, encoding=encoding, delimiter=delimiter, header=header)

        # Compare DF sizes
        assert baseDF.shape == actualDF.shape, \
            f'The number of columns or rows does not match in the two files.\n' \
            f'Base: {baseDF.shape[0]} rows, {baseDF.shape[1]} columns.\n' \
            f'Actual: {actualDF.shape[0]} rows, {actualDF.shape[1]} columns. '

        # Compare DF Data
        # print(dir(baseDF))
        print('Start compare')
        baseDF = baseDF.replace(np.nan, '', regex=True)
        actualDF = actualDF.replace(np.nan, '', regex=True)
        baseDict = baseDF.to_dict()
        actualDict = actualDF.to_dict()
        failureList = []
        for baseKey, actualKey in zip(baseDict, actualDict):
            assert baseKey == actualKey, 'Files headers do not match. Base is {base}. Actual is {actual}'.format(
                base=baseKey, actual=actualKey)
            for key in baseDict[baseKey]:
                baseValue = baseDict[baseKey][key]
                actualValue = actualDict[actualKey][key]
                # checking for timestamp/date (snapshot)
                for exp in self.to_ignore:
                    if re.search(exp, str(baseValue)):
                        # print("Skip timestamp/date")
                        break
                else:
                    if baseValue != actualValue:
                        failureList.append(
                            'Difference found.  Base is {base}. Actual is {actual}'.format(base=baseValue,
                                                                                           actual=actualValue))

        if failureList:
            errorCount = len(failureList)
            print('Differences found:')
            for error in failureList:
                print('ERROR:', error)
            assert False, ('Differences found.  See list above with ', errorCount, ' errors.')
        else:
            print('Compare complete, no differences found.')

    def copy_csv_to_max_MiB(self, baseFile, newFile, maxMiB):
        """
        This component will take the csv data from the base file specified and continuously copy it into the new file
        until the desired max file size in MiB is reached.

        : param baseFile : Additional folder path to the base file (Starting after ..\\GlobalComplianceBaselineFiles\\ folder). Ex) "Dashboard Baselines\\Baseline_File_Example.csv"
        : param newFile : Name of new file, including file extension. Ex) "newFile.csv"
        : param maxMiB : Max size in new file can be in Mebibytes. Ex) 100
        : return : None
        """

        # Read base file and caputure size in MiB of data
        baseFile = str(Path(self._get_baseline_relative_path()) / 'GlobalComplianceBaselineFiles' / baseFile)
        newFile = str(Path(self._get_relative_path()) / '_data' / newFile)
        baseDF = pandas.read_csv(baseFile)
        baseSize = bitmath.getsize(baseFile)
        baseMiB = baseSize.to_MiB()

        # Set counter for file size and copy data into new file until reach max size without going over
        sizeMiB = 0
        while sizeMiB <= float(maxMiB):
            if (float(maxMiB) - sizeMiB) >= baseMiB:
                baseDF.to_csv(newFile, mode='a')
                sizeBytes = bitmath.getsize(newFile)
                sizeMiB = sizeBytes.to_MiB()
            else:
                break
        print('Final file size is ', sizeMiB)

    def compare_other_files(self, base, actual, encoding=None):
        """
        Compares files line-by-line that doesn't follow the csv format/standards (due to how it was built in VITR)
        or does not have equal amounts of rows/columns throughout the file (E.g. AP/AR Ledgers, etc.).

        Note: Try using compare_csv_files component first before using compare_other_files.

        : param base : Relative folder path to base file ("C:\\base\\baseline_file.csv") or additional folder path to the base file starting from \\GlobalComplianceBaselineFiles\\ folder ("Dashboard Baselines\\Baseline_File_Example.csv")
        : param actual : Name of actual file, including file extension. Defaults to locating file in C:\\test\\_data\\ folder. Ex) "Actual_File_Example.csv"
        : return : None
        """
        # check if base path is defaulted baseline folder or another path location
        if "C:\\" in str(base):
            base = str(base)
        elif "_data" in str(base):
            base = str(Path(self._get_relative_path()) / base.replace('\\', '/'))
        else:
            base = str(
                Path(self._get_baseline_relative_path()) / 'GlobalComplianceBaselineFiles' / base.replace('\\', '/'))

        # check if actual path is defaulted download folder or another path location
        if "C:\\" in str(actual) or "C:/" in str(actual):
            actual = str(actual)
        else:
            actual = str(Path(self._get_relative_path()) / '_data' / actual.replace('\\', '/'))

        line = 0
        failureList = []

        with open(base, 'r', encoding=encoding) as t1, open(actual, 'r', encoding=encoding) as t2:
            while True:
                baseFile = t1.readline()
                actualFile = t2.readline()
                line += 1
                if baseFile or actualFile:
                    for exp in self.to_ignore:
                        if re.search(exp, str(baseFile)):
                            break
                    else:
                        if baseFile != actualFile:
                            failureList.append("Difference in Line " + str(
                                line) + ": \nBase is:\n" + baseFile + "\nActual is:\n" + actualFile)
                else:
                    t1.close()
                    t2.close()
                    break

        if failureList:
            errorCount = len(failureList)
            print('Differences found:')
            for error in failureList:
                print('ERROR:', error)
            assert False, ('Differences found.  See list above with ', errorCount, ' errors.')
        else:
            print('Compare complete, no differences found.')

    def unzip_file(self, zipFile):
        """
        Unzips a zip file specified in the relative folder path.

        : param zipFile : Name of downloaded zip file, including zip extension. Ex) "zipFile.zip"
        : return : Extracted file(s)
        """
        zipFile = Path(self._get_relative_path()) / '_data' / zipFile
        with ZipFile(zipFile, 'r') as zip:
            zip.printdir()
            zip.extractall(path=Path(self._get_relative_path()) / '_data')
            zip.close()
            os.remove(zipFile)

    def write_efile_to_file(self, efileResp, fileName):
        """
        Converts the efile download response to bytes and writes into specified filename and extension.

        : param efileResp : Response from efile download
        : param filename : Name of the file including file extension. (Ex: NetherlandsEfile.xbrl)
        """

        filePath = Path(self._get_relative_path()) / '_data' / fileName
        with open(filePath, 'wb') as file:
            file.write(bytes(efileResp, 'utf8'))
        file.close()

    def write_txt_to_file(self, data, filename, isVertexImport='false', encoding=''):
        """
        Writes the response text into specified filename and extension.

        : param data : Response text retrieved from API call (string type)
        : param filename : Name of the file, including file extension. Ex) "Monthly Regression.csv"
        : param isVertexImport : Set 'true' if 'Vertex Import' was used. Otherwise, keep default as 'false'
        : return : None
        """
        filePath = Path(self._get_relative_path()) / '_data' / filename
        if 'str' in str(type(data)):
            # check if it is vertex import type and replace any commas
            if isVertexImport.lower() == 'true':
                data = re.sub(",", "_", data)
            # check for commas with trailing space and replace with underscores
            if ", " in data:
                data = re.sub(", ", "_", data)
            # removes any blank rows before writing into csv file
            if encoding:
                with open(filePath, 'w', newline='', encoding=encoding) as file:
                    file.write(data)
            else:
                with open(filePath, 'w', newline='') as file:
                    file.write(data)
        else:
            with open(filePath, 'wb') as file:
                file.write(data)
        file.close()

    def rename_file(self, oldName, newName):
        """
        Renames a file

        : param oldName : Current, existing file name, including file extension. Ex) "fileName.csv"
        : param newName : New file name, including file extension. Ex) "fileName.csv"
        : return : None
        """
        oldName = Path(self._get_project_relative_path()) / '_data' / oldName
        newName = Path(self._get_project_relative_path()) / '_data' / newName
        if os.path.exists(oldName):
            print('File exists')
        else:
            assert False, ("File does not exist here: {}").format(oldName)
        # renames file
        os.rename(oldName, newName)

    def rename_file_by_keyword(self, keyword, newName):
        """
        Renames a file, based on just part of the file name.

        : param standardName : Current, existing file name, including file extension, but a part of the name that is consistent
            no matter what other parts of the filename that could be randomized on download.
        : param newName : New file name, including file extension. Ex) "fileName.csv"
        : return : None
        """
        newName = Path(self._get_relative_path()) / '_data' / newName
        filelist = os.listdir(Path(self._get_relative_path()) / '_data')
        for file in filelist:
            filename = os.fsdecode(file)
            if keyword in filename:
                os.rename(Path(self._get_relative_path()) / '_data' / filename, newName)
                return
        else:
            assert False, f'No file with the keyword {keyword} found in the _data folder. Here is the list of files in the _data dir {filelist}'

    def _create_or_delete_folder(self, action, folder_path, strip=True):
        """ please enter the folder_path separator with '\\' ex: 'C:\\test',
            If param pass action = delete, Delete all files in a directory,
            if param pass action = create, Create empty directory
        :type action: 'str'
        :type folder_path: 'str'
        """
        self.action = str(action).strip().lower()
        folder_path = Path(self._get_relative_path()) / '_data' / folder_path
        if strip:
            self.path = str(folder_path).strip().lower().replace(' ', '')
        else:
            self.path = str(folder_path)
        is_directory_created = False
        is_directory_deleted = False

        if len(self.path) > 0 and len(self.action) > 0:
            if self.action == 'create':
                if not os.path.exists(self.path):
                    try:
                        os.makedirs(self.path)
                        print("Directory '%s' created successfully." % self.path)
                        is_directory_created = True
                    except OSError:
                        print("Creation of the directory '%s' failed." % self.path)
                else:
                    print("Directory already exist.")
                return is_directory_created
            elif self.action == 'delete':
                if os.path.exists(self.path):
                    try:
                        if len(os.listdir(self.path)) == 0:
                            os.rmdir(self.path)
                        else:
                            rmtree(self.path)  # remove dir and all contains
                        print("Directory is deleted.")
                        is_directory_deleted = True
                    except OSError as error:
                        print('Error while deleting directory. ' + str(error))
                else:
                    print("Directory doesn't exists. Delete can't perform.")
            else:
                raise TypeError("Invalid action='{}'. Please select 'create' or 'delete'".format(self.action))
        else:
            raise TypeError("Empty parameter passed.")
        return is_directory_deleted

    def delete_file(self, file_path):
        """
        Delete specified file name from _data folder

        : param file_path : String. File path starting at _data folder. E.g. '_data/fileName.csv'
        : return : Boolean.
        """
        file_path = str(Path(self._get_baseline_relative_path_for_gha()) / file_path.replace('\\', '/'))
        is_file_deleted = False

        if len(file_path) > 0:
            if os.path.isfile(file_path):
                try:
                    os.remove(file_path)
                    print("File '%s' deleted successfully." % file_path)
                    is_file_deleted = True
                except OSError as error:
                    assert False, 'Error while deleting file. ' + str(error)
            elif os.path.isdir(file_path):
                assert False, f"TypeError: Only folder path passed - {file_path}. File delete can't perform."
            else:
                assert False, f"Error: File not found at {file_path}."
        else:
            assert False, "Empty parameter passed."
        return is_file_deleted

    def update_file_with_unique_invoice_number(self, file_path, encoding='utf-8'):
        """Component to append timestamp to invoice number in import file in order to create a unique invoice rowNumber
        Will look for string 'timestamp' in import file as postiong to append timestamp

        : param file_path :  Path and name of file to append timestamp to (ex: _data/Recieved_Invoices_Spain.csv)
        """

        data_folder = str(Path(self._get_project_relative_path()) / '_data' / file_path.split('/')[-1])
        self.file_path = str(Path(self._get_project_relative_path()) / file_path)
        timestamp = ''
        is_file_updated = False

        timestamp = datetime.today().strftime('%y%m%d%H%M%S%f')
        # print("Current date is....", current_date)

        if len(self.file_path) > 0:
            if os.path.isfile(self.file_path):
                if self.verify_file_type_csv_or_txt(self.file_path):
                    try:
                        with open(self.file_path, "r", encoding=encoding) as reader:
                            reader = ''.join([i for i in reader]).replace('timestamp', timestamp)
                        with open(data_folder, 'w+', encoding='utf-8') as writer:
                            writer.writelines(reader)
                        print("File updated successfully.")
                        is_file_updated = True
                    except OSError as error:
                        print('Error while updating file. ' + str(error))
            elif os.path.isdir(self.file_path):
                raise TypeError("Only folder path passed. File can't update.".format(self.file_path))
            else:
                raise TypeError("Error: File not found at '{}'.".format(self.file_path))
        else:
            raise TypeError("Empty parameter passed.")

        return timestamp

    def update_file_with_current_date(self, file_path: str, year='', month='', encoding='utf-8', separator='') -> bool:
        """
        Processes given file and outputs a copy to '_data' folder with '######' replaced
        with a year and month. Will use the current date, unless given a year and month.

        Please enter the folder_path separator with '\\' ex: 'C:\\test',
            file type should be .csv or .txt, others type will throw NameError.

        :param file_path: Path and name of file to update dates in
        :param year: Year to update to (Format: YYYY)
        :param month: Month to update to (Format: MM)
        :param encoding: Optional. Character encoding to use. Defaults to 'utf-8'
        :param separator: Optional. Additional separator (Ex: '-' outputs 'YYYY-MM-')
        :return: Whether dates were updated in the file
        """
        data_folder = str(Path(self._get_project_relative_path()) / '_data' / file_path.split('/')[-1])
        self.file_path = str(Path(self._get_baseline_relative_path()) / file_path)
        self.year = str(year).strip().lower()
        self.month = str(month).strip().lower()
        # self.file_path = str(file_path).strip().lower()
        current_date = ''
        is_file_updated = False

        if len(self.year) == 0 and len(self.month) == 0:
            current_date = datetime.today().strftime(f"%Y{separator}%m{separator}")
        elif len(self.year) == 4 and len(self.month) == 2 and self.month.isnumeric() and self.year.isnumeric():
            current_date = self.year + separator + self.month + separator
        else:
            raise TypeError("Error: Invalid year='{}', month='{}'.".format(year, month))

        if len(self.file_path) > 0:
            if os.path.isfile(self.file_path):
                if self.verify_file_type_csv_or_txt(self.file_path):
                    try:
                        with open(self.file_path, "r", encoding=encoding) as reader:
                            reader = ''.join([i for i in reader]).replace("######", current_date)
                        with open(data_folder, 'w+', encoding='utf-8') as writer:
                            writer.writelines(reader)
                        print("File updated successfully.")
                        is_file_updated = True
                    except OSError as error:
                        print('Error while updating file. ' + str(error))
            elif os.path.isdir(self.file_path):
                raise TypeError("Only folder path passed. File can't update.".format(self.file_path))
            else:
                raise TypeError("Error: File not found at '{}'.".format(self.file_path))
        else:
            raise TypeError("Empty parameter passed.")

        return is_file_updated

    def update_file_with_current_company_code(self, filePath, newCompanyCode, uniqueID='', companyCodeToken='11235',
                                              encoding='utf-8'):
        """
        Will update the given file with a new company code. Will replace the given token with the new company code
        This will save the updated file in the _data folder with the unique ID added to the end of the filename.

        :param filePath: relative path of the file to update. Path should be relative from vitr-testing-vat-compliance. Eg: "vitr-testing-vat-compliance-data/Test_Data/GLOBAL_REGRESSION/Global Compliance Import Files/CountryRegression/Belgium/Belgium Regression Data Import 2.csv"
        :param newCompanyCode: new company code to use in the file.
        :param uniqueID: uniqueID to add to the end of the file.
        :param companyCodeToken: current companyCodeToken in the file. For all virt import files this  will be 11235.
        :param encoding: encoding format to use for reading and writing of files. Most countries with special characters with with 'cp1252'
        :return:
        """
        # add unique ID to filename
        fileName = filePath.split('/')[-1].split('.')
        fileName[0] = fileName[0] + uniqueID
        fileName = '.'.join(fileName)

        data_folder = str(Path(self._get_project_relative_path()) / '_data' / fileName)
        filePath = str(Path(self._get_baseline_relative_path_for_gha()) / filePath)

        if len(filePath) > 0:
            if os.path.isfile(filePath):
                if self.verify_file_type_csv_or_txt(filePath):
                    try:
                        with open(filePath, "r", encoding=encoding) as reader:
                            reader = ''.join([i for i in reader]).replace(companyCodeToken, newCompanyCode)
                        with open(data_folder, 'w+', encoding='utf-8') as writer:
                            writer.writelines(reader)
                        print("File updated successfully.")
                        is_file_updated = True
                    except OSError as error:
                        print('Error while updating file. ' + str(error))
            elif os.path.isdir(filePath):
                raise TypeError("Only folder path passed. File can't update.".format(filePath))
            else:
                raise TypeError("Error: File not found at '{}'.".format(filePath))
        else:
            raise TypeError("Empty parameter passed.")

    def verify_file_type_csv_or_txt(self, file_path):
        # Ensure the file has the right extension
        file_path = str(file_path).strip().lower()
        is_file_csv_or_txt = False
        if not (file_path.endswith('.csv') or (file_path.endswith('.txt'))):
            raise NameError("File must be a '.csv' or '.txt' extension")
        else:
            is_file_csv_or_txt = True
        return is_file_csv_or_txt

    def verify_export_csv(self, columns, json_data, csv_data):
        """
        Shared component to compare a json response and csv response from the api.
        Can accept either a single row and single json response, or an entire csv file and json array.
        Columns are expected as a list of tuples i.e. [(json_col, csv_col), ...]

        hint: to get list of csv rows from pandas csv dataframe do csvData.to_dict('records')
        """
        if type(json_data) is not list:
            json_data = [json_data]
        if type(csv_data) is not list:
            csv_data = [csv_data]
        failures = []
        if len(json_data) != len(csv_data):
            assert False, f'Failed to compare json data and csv data for export file, number of rows mismatched. Json rows:{len(json_data)} Csv rows:{len(csv_data)}'
        for index, json_object in enumerate(json_data):
            csv_row = csv_data[index]
            for jsonKey, csvKey in columns:
                if csvKey not in csv_row.keys():
                    failures.append((jsonKey, f'{csvKey} not present in list of keys from csv. {csv_row.keys()}'))
                    continue
                if json_object[jsonKey] != csv_row[csvKey]:
                    failures.append((jsonKey, json_object[jsonKey], csv_row[csvKey]))
        assert not failures, f'Export csv did not match response from api. Failures: {failures}'

    def set_saved_unique_id(self):
        """
        Generates a unique ID and saves to a pickle file within _data folder to be read

        NOTE: Used for API E2E tests since unique ID within names needs to be the same

        :Workflow:
        set_saved_unique_id (required to generate a new ID as needed)
        get_saved_unique_id (can be run multiple times)

        : param : None
        : return : Pickle file within _data folder
        """
        now = datetime.now()
        uniqueID = now.strftime('%y%m%d%H%M%S')
        print('Using Unique ID:', uniqueID)

        filePath = str(Path(self._get_relative_path()) / "_data" / "savedUniqueID.pkl")

        with open(filePath, "wb") as file:
            pickle.dump(uniqueID, file)

    def get_saved_unique_id(self):
        """
        Reads an pickle file from _data folder and returns saved unique ID

        NOTE: Used for API E2E tests since unique ID within names needs to be the same

        :Workflow:
        set_saved_unique_id (required to generate a new ID as needed)
        get_saved_unique_id (can be run multiple times)

        : param : None
        : return : Pickle file within _data folder
        """
        filePath = str(Path(self._get_relative_path()) / "_data" / "savedUniqueID.pkl")
        # validate that pickle file called shareUniqueID.pkl exists in _data folder
        if os.path.exists(filePath):
            print('Shared Unique Id file does exists.')
            pass
        else:
            assert False, "Shared Unique Id file does not exist in _data folder."

        with open(filePath, "rb") as file:
            uniqueID = pickle.load(file)

        return uniqueID

    def verify_if_file_is_empty(self, filePath, isEmpty=True):
        """
        Verify if the file is empty or not by checking if the file contains more than 1 line. Used to validate if the
        downloaded file or file written from JSON response object from VVC has data or not.

        NOTE: If file contains column headers or 'EMPTY FILE' only (in which is takes up one line), it is considered to
        be an empty file.

        params:
            filePath: String. Relative path to the file for validation, including file extension.
                (E.g. '_data/fileName.csv')
            expectedValue: Boolean. Expectation of whether the file is empty or not. Defaults to True.
        """

        filePath = str(Path(self._get_relative_path()) / filePath.replace('\\', '/'))

        with open(filePath, 'r') as file:
            lines = file.readlines()

            if isEmpty:
                assert len(lines) == 0 or len(lines) == 1, "File was expected to be empty but it was not."
            else:
                assert len(lines) > 1, "File was expected to be not empty but it contained some data."

    #######################  FROM DATA INTEGRITY LIBRARY/DEPRECATED  ################################

    def compare_csv_files1(self, base, actual):
        """
        This component will compare the two files given. Will first check for the same number of rows and columns.
        If they match it will then check cell by cell for differences.
        If difference are found a diff file will be created.

        :param base: relative path to the base file. Example: \\Upload\\baseFile.csv
        :param actual: relative path to the actual file. Example: \\Downloads\\actualFile.csv
        :return: None
        """
        # Load data into pandas DF
        base = str(Path(self._get_relative_path()) / base.replace('\\', '/'))
        actual = str(Path(self._get_relative_path()) / actual.replace('\\', '/'))
        baseDF = pandas.read_csv(base)
        actualDF = pandas.read_csv(actual)

        # Compare DF sizes
        assert baseDF.shape == actualDF.shape, 'The number of columns or rows do not match in the two files.'

        # Compare DF Data
        # print(dir(baseDF))
        baseDF = baseDF.replace(np.nan, '', regex=True)
        actualDF = actualDF.replace(np.nan, '', regex=True)
        baseDict = baseDF.to_dict()
        actualDict = actualDF.to_dict()
        failureList = []
        for baseKey, actualKey in zip(baseDict, actualDict):
            assert baseKey == actualKey, 'Files headers do not match. Base is {base}. Actual is {actual}'.format(
                base=baseKey, actual=actualKey)
            for key in baseDict[baseKey]:
                baseValue = baseDict[baseKey][key]
                actualValue = actualDict[actualKey][key]
                if baseValue != actualValue:
                    failureList.append(
                        'Found miss match data in file. Base is {base}. Actual is {actual}'.format(base=baseValue,
                                                                                                   actual=actualValue))

        if failureList:
            for error in failureList:
                print('ERROR:', error)

            assert False, 'Miss match found in files. Check the above lies for errors.'

    def get_unique_identifier1(self):
        """
        Returns an unique identifier to be used when creating repeatable tests.

        :return: str: 14 character string timestamp.
        """
        now = datetime.now()
        uniqueID = now.strftime('%y%m%d%H%M%S%f')[:-3]
        print('Using Unique ID:', uniqueID)
        return uniqueID

    def JSON_to_CSV1(self, json, columns, fileName):
        # print(json)
        columnArray = columns.split("|")

        with open(Path(self._get_relative_path()) / '_data' / fileName + ".csv", "w") as file:
            for i in range(0, len(json)):
                lineString = ""
                for j in range(0, len(columnArray)):
                    lineString = lineString + str(json[i][columnArray[j]])
                    if j < len(columnArray) - 1:
                        lineString = lineString + ","
                # print(lineString)

                file.writelines(lineString + "\n")

    def _read_csv_bytes(self, byteContent):
        if type(byteContent) is not bytes:
            assert False, f'Content type must be bytes, but was "{type(byteContent)}".'
        return pandas.read_csv(BytesIO(byteContent))

    def _read_csv_file(self, filePath):
        dataFrame = pandas.read_csv(filePath)
        return dataFrame

    def _get_csv_column_values(self, columnName, dataFrame):
        columnValues = dataFrame[columnName]
        return columnValues

    def _get_latest_file_name(self):
        time.sleep(10)
        list_of_files = glob.glob(self._get_relative_path() + '_data/*.csv')
        # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        return latest_file

    def _get_random_float_value(self, precision):
        return round(random.uniform(1000.5, 9999.5), precision)

    def _get_jenkins_downloaded_path(self):
        """
        returns the relative path to the scripts folder for the current OS
        """
        if os.name == 'nt':
            return 'C:\\test\\_data'  # Windows
        else:  # other (unix)
            x = Path(__file__).parent.absolute()
            basePath = str(x).split('vitr-na-ng-testing')[0]
            download_dir = str(Path(basePath))
            return download_dir

    def _get_project_relative_path(self):
        """
        returns the relative path to the project folder for the current OS
        """
        if os.name == 'nt':
            return 'C:\\test\\'  # Windows
        else:
            x = Path(__file__).parent.absolute()
            basePath = str(x).split('vitr-na-ng-testing')[0]
            return f'{basePath}/'  # other (unix)

    def _get_baseline_relative_path(self):
        """
        returns the relative path to the GC data folder for the current OS
        """
        if os.name == 'nt':
            return 'C:\\test\\PycharmProjects\\NextGen\\vitr-na-ng-testing\\ng-automation\\ng_tests' \
                   '\\test_data\\'  # Windows
        else:
            x = Path(__file__).parent.absolute()
            basePath = str(x).split('vitr-na-ng-testing')[0]
            # This will remove the /lib from the base path
            return f'{basePath}/vitr-na-ng-testing/ng-automation/ng_tests/test_data/'  # other (unix)

    def _get_baseline_relative_path_for_gha(self):
        """
        returns the relative path to the GC data folder for the current OS
        """
        if os.name == 'nt':
            return 'C:\\test\\PycharmProjects\\NextGen\\vitr-na-ng-testing\\ng-automation\\ng_tests' \
                   '\\test_data\\'  # Windows
        else:
            x = Path(__file__).parent.absolute()
            basePath = str(x).split('vitr-na-ng-testing')[0]
            # This will remove the /lib from the base path
            return f'{basePath}/vitr-na-ng-testing/vitr-na-ng-testing/ng-automation/ng_tests/test_data/'  # other (unix)

    def generate_random_string_with_given_characters_and_length(self, characters, length):
        return ''.join(random.choices(characters, k=length))

    def get_formatted_date_without_time(self, fmt='%Y%m%d%H%M%S', date=datetime.now()):
        """
        Gets the current date in the format you provide. The time portion (if its there) will be the equivalent of 0 minutes, 0 seconds, 0 hours.
        """
        if type(date) == str:
            date = datetime.strptime(date, fmt)
        return date.date().strftime(fmt)

    def convert_int_month_to_string(self, monthNumber):
        """
        Will take a month number and turn it into the short form of a month name. Example input of 1 will return Jan

        :param monthNumber: The number of the month to convert
        """
        monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return monthList[int(monthNumber) - 1]

    def get_thismonth_lastmonth(self):
        """This component passes a list with the current year, current month, last day of the month, last month, and last day of last month."""
        thisMonth = time.gmtime()[1]
        thisYear = time.gmtime()[0]

        # Roll January back to December of the previous year
        if thisMonth == 1:
            lastMonth = 12
            lastYear = thisYear - 1
        else:  # Not December, just add 1
            lastMonth = thisMonth - 1
            lastYear = thisYear

        # Roll December up to January of the next year
        if thisMonth == 12:
            nextMonth = 1
            nextYear = thisYear + 1
        else:
            nextMonth = thisMonth + 1
            nextYear = thisYear

        lastMonthRange = str(calendar.monthrange(lastYear, lastMonth)[1])
        thisMonthRange = str(calendar.monthrange(thisYear, thisMonth)[1])
        nextMonthRange = str(calendar.monthrange(nextYear, nextMonth)[1])

        thisYear = str(thisYear)
        thisMonth = str(thisMonth)
        lastMonth = str(lastMonth)
        lastYear = str(lastYear)
        nextMonth = str(nextMonth)
        nextYear = str(nextYear)
        currentDay = str(time.gmtime()[2])

        # Add leading zero of month is single digit
        if len(thisMonth) == 1:
            thisMonth = "0" + thisMonth

        if len(lastMonth) == 1:
            lastMonth = "0" + lastMonth

        if len(nextMonth) == 1:
            nextMonth = "0" + nextMonth

        dateList = [thisYear, thisMonth, currentDay, thisMonthRange, lastYear, lastMonth, lastMonthRange, nextYear,
                    nextMonth, nextMonthRange]
        return dateList

    def json_keys_to_csv_keys(self, jsonKeys):
        """
        Convert from camelCase to Title Case
        """
        ret_val = []
        for key in jsonKeys:
            parts = re.findall(r'[A-z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', key)
            parts[0] = parts[0].title()
            ret_val.append(' '.join(parts))
        return ret_val

    def sort_csv_by_specific_column(self, filename, rowNumOne, encoding, dialect='excel', rowNumTwo=None):
        """
        Sorts a CSV file by the specified column index(s).  This will overwrite the contents
        of the supplied file with the sorted data.

        :param filename: The filename of the file to be sorted.
        :param rowNumOne: The index of the column to sort by.
        :param encoding: The encoding to use when opening a file.
        :param dialect: (optional) The dialect of the file to supply to the csv reader.  Default is excel.
        :param rowNumTwo: (optional) A secondary column index to sort by. The file is sorted by the column specified in rowNumOne first, then by the column specified by rowNumTwo.
        """
        filePath = Path(self._get_relative_path()) / '_data' / filename
        with open(filePath, newline='') as csvfile:
            reader = csv.reader(csvfile, dialect, quoting=csv.QUOTE_MINIMAL, quotechar='"')
            next(reader, None)  # skip the headers
            if rowNumTwo:
                sortedlist = sorted(reader, key=lambda row: (row[rowNumOne], row[rowNumTwo]), reverse=False)
            else:
                sortedlist = sorted(reader, key=lambda row: row[rowNumOne], reverse=False)
            with open(filePath, 'r', newline='', encoding=encoding) as file:
                d_reader = csv.DictReader(file)
                headers = d_reader.fieldnames
            with open(filePath, 'w', newline='', encoding=encoding) as fileWriter:
                writer = csv.writer(fileWriter, quoting=csv.QUOTE_MINIMAL, quotechar='"')
                writer.writerow([header for header in headers])  # write all the headers
                writer.writerows(sortedlist)

    ##################
    # AWS Components #
    ##################

    def download_file_from_s3(self, bucketName, key):
        """
        Will download the given file into the _data directory.

        :param bucketName: Name of the bucket that the file is in. This is limited to the dev instance
        :param key: key of the file to download.
        """
        if platform.system() == 'Linux':
            filename = key.split('/')[-1]
            path = str(Path(self._get_project_relative_path()) / '_data' / filename)
            s3 = boto3.resource('s3')
            s3.Bucket(bucketName).download_file(key, path)
        else:
            print(
                'download of s3 is only for linux. For local running the file is expected to already be in the _data directory.')

    def _is_float(self, stringValue):
        """
        Checks whether an string value can ve converted to a float number and returns True
        if possible and False if not possible.

        :param stringValue: String value to check if can be converted to float.
        :return: Boolean value True if the String can be converted to float, False otherwise.
        """
        try:
            float(stringValue)
            return True
        except ValueError:
            return False

    def _convert_to_float(self, stringValue):
        """
        Returns received String value converted to float number if it is possible, else it
        returns the same String value as String.

        :param stringValue: String value to try to convert to float.
        :return: Float number of the String value passed if it can be converted, otherwise returns
        the same String received.
        """
        if self._is_float(stringValue):
            fl_result = float(stringValue)
            return fl_result
        else:
            return stringValue

    def get_max_width_of_two_csv(self, base, actual, delimiter=','):
        """
        Returns the max width between two csv files where width is the number of columns

        :param base: Path to the baseline file
        :param actual: Path to the actual file
        :param delimiter: The delimiter used on the file by default it is ','
        :return: Integer number which corresponds to the Higher quantity of Columns between the two files
        """
        base_file_width = max(open(base, 'r'), key=lambda x: x.count(delimiter)).count(delimiter)
        actual_file_width = max(open(actual, 'r'), key=lambda x: x.count(delimiter)).count(
            delimiter)
        return max(base_file_width, actual_file_width)

    def execute_db_query(self, statement: str, auto_commit: bool = False):
        """
        :param statement: The SQL statement to be executed
        :param auto_commit: If True, all queries are Transactional by default
        :return: The current cursor
        """
        conn = psycopg2.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"))
        conn.autocommit = auto_commit
        # print("Debug 'API_Returns.execute_db_query':", conn.get_dsn_parameters())
        cursor = conn.cursor()
        cursor.execute(statement)
        try:
            return cursor.fetchall()
        except ProgrammingError as e:
            return

    def rand_str(self, stringLength: int, chars=string.ascii_lowercase + string.digits):
        """
        Will create a random string of `stringLength` consisting of characters defined in `chars`
        :param stringLength: The length of the random string to create
        :param chars: The chars the random string can consist of
        :return: A random string
        """
        return ''.join(random.choice(chars) for char in range(stringLength))

    def download_file_by_url_in_download_directory(self, url: str = None, fileName: str = None) -> str:
        """Downloads file form Url and save it locally with fileName.
        :param url: Required[str], url for file download
        :param fileName: Optional[str], name with which file will be saved. If not provided filename will be current timestamp
        :return: filename
        """
        if url is None:
            raise AssertionError('Please provide the url to download the file')
        response = requests.get(url)
        if not response.ok:
            raise Exception(response)
        content = response.content
        if fileName is None:
            fileName = (datetime.utcnow().strftime("%Y%m%d%H%M%S%f"))[:-3]
        fileName = f"{self._get_baseline_relative_path_for_gha()}/{fileName}"
        with open(fileName, 'wb') as fo:
            fo.write(content)
        return fileName

    def validate_number_of_files_in_zip(self, fileName=None, count=None):
        """
        This component will validate the number of files in the arvhive
        :param fileName: archive file name from test data folder. Test data folder path will be appended to file name
        :param count: number of files as expected in the archive
        :return: None
        """
        if fileName is None:
            fileName = (datetime.utcnow().strftime("%Y%m%d%H%M%S%f"))[:-3]
            print(fileName)
        filePath = f"{self._get_baseline_relative_path_for_gha()}/{fileName}"

        if count is None:
            count = 0

        with ZipFile(filePath, 'r') as zip:
            if len(zip.filelist) == count:
                pass
            else:
                raise AssertionError(f"Archive file is having {len(zip.filelist)} instead of {count} files")

    def validate_return_names_downloaded_in_zip(self, fileName, returnNames):
        """
        This component will validate all the return names are downloaded in the archive
        :param fileName: Archive file name
        :param returnNames: list of all the return names.
        :return: None
        """
        if fileName is None:
            fileName = (datetime.utcnow().strftime("%Y%m%d%H%M%S%f"))[:-3]
        filePath = f"{self._get_baseline_relative_path_for_gha()}/{fileName}"
        returns = returnNames.split('|')
        with ZipFile(filePath, 'r') as zip:
            for returnName in returns:
                for files in zip.filelist:
                    if returnName == files.filename:
                        break
                else:
                    raise AssertionError(f'return named {returnName} not found in archive.')

    def delete_file_from_test_data(self, fileName):
        """
        Delete specified file name from test_data folder

        : param fileName : String. Name of the file to be deleted
        """
        filePath = f"{self._get_baseline_relative_path_for_gha()}{fileName}"

        if len(filePath) > 0:
            if os.path.isfile(filePath):
                try:
                    os.remove(filePath)
                    print("File '%s' deleted successfully." % filePath)
                except OSError as error:
                    assert False, 'Error while deleting file. ' + str(error)
            elif os.path.isdir(filePath):
                assert False, f"TypeError: Only folder path passed - {filePath}. File delete can't perform."
            else:
                assert False, f"Error: File not found at {filePath}."
        else:
            assert False, "Empty parameter passed."

    def move_file_from_data_folder(self, fileName: str):
        """
        Moves the file from C:\\test\\_data to
        C:\\test\\PycharmProjects\\NextGen\\vitr-na-ng-testing\\ng-automation\\ng_tests\\test_data\\Imports_File

        :param fileName: Name of the file to be moved
        :return: None
        """

        startPath = str(Path(self._get_project_relative_path()) / '_data' / fileName)
        endPath = str(Path(self._get_baseline_relative_path_for_gha()) / 'Imports_File' / fileName)

        try:
            shutil.move(startPath, endPath)
            print(f"File moved successfully from {startPath} to {endPath}")
        except FileNotFoundError:
            print(f"File not found at {startPath}")
        except FileExistsError:
            print(f"File already exists at {endPath}")
        except Exception as e:
            print(f"Error while moving file: {e}")


def debug():
    tu = TestingUtil()


if __name__ == "__main__":
    debug()
