import csv
import os


def retrieve_cols(data: list):
    return list(map(lambda row: [row[i] for i in (7, 10, 11)], data))


def validate_row(row: list):
    return row[10] != 'Unknown'


def filter_rows(row: list):
    return list(filter(validate_row, row))


def read_data(filename: str) -> list:
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
    with open(path, 'r') as file:
        return list(csv.reader(file, delimiter=','))[1:]


def get_valid_data(filename: str) -> list:
    return retrieve_cols(filter_rows(read_data(filename)))


def main():
    data = get_valid_data('healthcare-dataset-stroke-data.csv')
    for val in data:
        print(val)


if __name__ == '__main__':
    main()
