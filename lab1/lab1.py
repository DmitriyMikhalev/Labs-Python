import csv
import os
from functools import reduce

TO_PERCENTS = 100


def filter_rows(data: 'list[list]') -> 'list[list]':
    """Delete rows with 'Unknown' answer about smoking.
    Required params:
        data: list (12 strings)

    Return new list without wrong rows.
    """
    if any(len(row) != 12 for row in data):
        raise ValueError('Dataset must have 12 elements.')

    return list(filter(lambda row: row[10] != 'Unknown', data))


def get_valid_data(filename: str) -> 'list[list[str, int, int]]':
    """Return list of lists with 3 elements:
        residence type: str
        smoke status: int (0 for 'no' else 1)
        has stroke: int (1 for 'yes' else 0)
    Required params:
        filename: str
    """
    return transform_data(retrieve_cols(filter_rows(read_data(filename))))


def get_percent_smoke_stroke(data: 'list[list[str, int, int]]') -> float:
    """Return percent value of people who smokes and has stroke. If value
    is -1, general count is 0.
    """
    if (general_count := get_count_smokers(data)) != 0:
        return TO_PERCENTS * get_count_smokers_stroke(data) / general_count

    return -1


def get_count_stroke(data: 'list[list[str, int, int]]') -> int:
    """Return count of people who has stroke."""
    return reduce(
        sum_two,
        list(map(lambda row: row[2], data))
    )


def get_count_smokers(data: 'list[list[str, int, int]]'):
    """Return count of people who smokes."""
    return reduce(
        sum_two,
        list(map(lambda row: row[1], data))
    )


def get_count_smokers_stroke(data: 'list[list[str, int, int]]'):
    """Return count of people who smokes and has stroke."""
    return reduce(
        sum_two,
        list(map(lambda row: row[1] * row[2], data))
    )


def get_count_urban(data: 'list[list[str, int, int]]'):
    """Return count of people lives in city."""
    return reduce(
        sum_two,
        list(map(lambda row: int(row[0] == 'Urban'), data))
    )


def get_count_urban_stroke(data: 'list[list[str, int, int]]'):
    """Return count of people lives in city and has stroke."""
    return reduce(
        sum_two,
        list(map(lambda row: (int(row[0] == 'Urban') * row[2]), data))
    )


def get_percent_urban_stroke(data: 'list[list[str, int, int]]'):
    """Return percent value of people who lives in city and has stroke.
    If value is -1, general count is 0.
    """
    if (general_count := get_count_urban(data)) != 0:
        return TO_PERCENTS * get_count_urban_stroke(data) / general_count

    return -1


def replace_cols(row: 'list[str, str, str]'
                 ) -> 'list[str, int, int]':
    """Return new list with the same first value and casted to int 2nd and 3rd
    values.
    Required params:
        row: list[str, str, str]


    """
    return [
        row[0],
        int(row[1] == 'never smoked'),
        int(row[2])
    ]


def transform_data(data: 'list[list[str, str, str]]'
                   ) -> 'list[list[str, int, int]]':
    """Get prepared data to be analyzed.
    Required params:
        data: list[list[str, str, str]]
    Example:
        data = [
            ['Urban', 1, 1],
            ['Rural', 1, 0],
            ...
        ]

    Return list of lists with 3 elements:
        residence type: str
        smoke status: int (0 for 'no' else 1)
        has stroke: int (1 for 'yes' else 0)
    """
    return list(map(replace_cols, data))


def read_data(filename: str) -> 'list[list]':
    """Get data from .csv file.
    Required params:
        filename: str

    Return list of lists (nested lists have 12 strings) from <filename> file
    located at directory where program was started. Table header is ignored.
    """
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
    with open(path, 'r') as file:
        return list(csv.reader(file, delimiter=','))[1:]


def sum_two(x, y):
    return x + y


def retrieve_cols(data: 'list[list]') -> 'list[list[str, str, str]]':
    """Get predetermined columns from dataset.
    Required params:
        data: list (12 strings)

    Return new list created from 8 (residence type), 11 (smoking status),
    12 (has stroke) columns.
    """
    return list(map(lambda row: [row[i] for i in (7, 10, 11)], data))


def main() -> None:
    data = get_valid_data('healthcare-dataset-stroke-data.csv')
    print(get_percent_urban_stroke(data) * 100)


if __name__ == '__main__':
    main()
