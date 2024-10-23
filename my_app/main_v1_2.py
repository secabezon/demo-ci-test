from typing import List, Any


def process_data(data):
    return data


def concatenate_strings(string: List[str])-> str:
    return ''.join(string)


def display_message(message: str):
    print(message)


def main():
    data = process_data('example')
    print(data)


if __name__=="__main__":
    main()