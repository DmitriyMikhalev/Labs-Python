import csv
import os
from functools import reduce
from pprint import pprint


def retrieve_cols(data: list):
    return list(map(lambda row: [row[i] for i in (7, 10, 11)], data))


def filter_rows(data: list):
    return list(filter(lambda row: row[10] != 'Unknown', data))


def read_data(filename: str) -> list:
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
    with open(path, 'r') as file:
        return list(csv.reader(file, delimiter=','))[1:]


def get_valid_data(filename: str) -> list:
    return retrieve_cols(filter_rows(read_data(filename)))


def get_percent_smoke_stroke(data: list):
    """['Urban', 1/0, 1/0]
       [city?,  smoke?, stroke?]
       """
    return get_count_smokers_stroke(data)/get_count_smokers(data)


def get_count_stroke(data: list):
    return reduce(
        lambda count, next_value: count + next_value,
        list(map(lambda row: row[2], data))
    )


def get_count_smokers(data: list):
    return reduce(
        lambda count, next_value: count + next_value,
        list(map(lambda row: row[1], data))
    )


def get_count_smokers_stroke(data: list):
    return reduce(
        lambda count, next_value: count + next_value,
        list(map(lambda row: row[1] * row[2], data))
    )


def get_count_urban(data: list):
    return reduce(
        lambda count, next_value: count + next_value,
        list(map(lambda row: int(row[0] == 'Urban'), data))
    )


def get_count_urban_stroke(data: list):
    return reduce(
        lambda count, next_value: count + next_value,
        list(
            map(
                lambda row: (int(row[0] == 'Urban') * row[2]),
                data
            )
        )
    )


def get_percent_urban_stroke(data: list):
    return get_count_urban_stroke(data)/get_count_urban(data)


def replace_cols(row: list):
    return [
        row[0],
        int(row[1] == 'never smoked'),
        int(row[2])
    ]


def transform_data(data: list):
    return list(map(replace_cols, data))


def main():
    data = transform_data(get_valid_data('healthcare-dataset-stroke-data.csv'))
    print(get_percent_urban_stroke(data) * 100)


if __name__ == '__main__':
    main()
