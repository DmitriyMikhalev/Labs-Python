import csv
import os
from pprint import pprint


def retrieve_cols(data: list):
    return list(map(lambda row: [row[i] for i in (7, 10, 11)], data[1:]))


def filter_rows(data: list):
    return list(filter(None, data))


def read_data(filename: str):
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
    with open(path, 'r') as file:
        data = list(csv.reader(file, delimiter=','))

    return data


def main():
    data = read_data('healthcare-dataset-stroke-data.csv')
    pprint(data[0:15])


if __name__ == '__main__':
    main()
