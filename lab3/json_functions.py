import json
import os


def read_json(path: str = None) -> dict:
    """Parse JSON file into Python dict.
    Optional params:
        path: str

    If path isn't specified, default file is info_read.json located at the same
    place where program was started.
    """
    if path is None:
        path = os.path.dirname(os.path.abspath(__file__)) + '/info_read.json'

    with open(encoding='utf-8', file=path, mode='r') as file:
        return json.load(fp=file)


def valid_data(data: dict) -> bool:
    """Answer the question "Is the parsed data valid?".
    Required params:
        data: dict

    Expected structure of JSON:
        {
            'upload': <str>,
            'animals': [
                {
                    'cls': <str>,
                    ...
                },
                ...
            ]
        }
    """
    if not isinstance(data, dict):
        return False

    if not all(key in data for key in ('upload', 'animals')):
        return False

    if not isinstance(data['animals'], list):
        return False

    if not all(isinstance(obj, dict) for obj in data['animals']):
        return False

    if not all('cls' in obj.keys() for obj in data['animals']):
        return False

    return True


def write_json(data: dict, path: str = None) -> None:
    """Write data into JSON file.
    Required params:
        data: dict
    Optional patams:
        path: str

    If data is a string variable, there will be an attempt to convert string to
    Python dict and then it will be written.
    If path isn't specified, default file is info_write.json located at the
    same place where program was started.
    """
    if path is None:
        path = os.path.dirname(os.path.abspath(__file__)) + '/info_write.json'

    if isinstance(data, str):
        data = json.loads(data)

    with open(file=path, mode='w', encoding='utf-8') as file:
        json.dump(ensure_ascii=False, fp=file, indent=4, obj=data)
