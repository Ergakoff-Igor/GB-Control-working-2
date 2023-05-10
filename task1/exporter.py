import csv


def save_data_to_file(file, dataList):
    with open(file, mode="w", encoding='utf-8') as datafile:
        file_writer = csv.writer(datafile, delimiter = ";", lineterminator="\r")
        for line in dataList:
            file_writer.writerow([line.get_id(), line.get_date(), line.get_heading(), line.get_body()])
