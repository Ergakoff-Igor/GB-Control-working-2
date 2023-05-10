from note import Note
import csv

def read_data_from_file(file):
    with open(file, encoding='utf-8') as r_file:
        dataList = []
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            dataList.append(Note(row[0], row[1], row[2], row[3]))
        return dataList
        