#coding=utf-8
import os
import csv
import json

class Path:
    def __init__(self):
        self.filse=os.getcwd() + '/serve/files/' 
        self.origin_data=self.filse + 'latin_data/'   
        self.data_by_year=self.filse + 'data_by_year/' 
    

path = Path()

def open_csv(path,encoding='utf-8-sig'):
    if path.find('.csv') == -1:
        path += '.csv'

    if isFile(path) is False:
        raise RuntimeError(f'csv文件路径错误：{path}')
        
            
    with open(path,'r',encoding=encoding) as file:
        csv_data = csv.reader(file)
        array = []
        for line in csv_data:
            array.append(line)
        return array


def open_json(path):
    if path.find('.json') == -1:
        path += '.json'

    if isFile(path) == False:
        raise RuntimeError(f'json文件路径错误：{path}')

    with open(path,'r') as f:
        json_data = json.load(f)
        return json_data


def save_csv(data,path):
    if path.find('.csv') == -1:
        path += '.csv'

    with open(path, 'w') as file:
        csv_writer = csv.writer(file)
        for line in data:
            csv_writer.writerow(line)


def save_json(data,path):
    if path.find('.json') == -1:
        path += '.json'

    with open(path,'w') as f:
        json.dump(data, f, ensure_ascii=False)


def isFile(path):
    return os.path.isfile(path)
