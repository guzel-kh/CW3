from utils import get_data, get_executed_operations, get_last_operations, get_formatted_data


def main():
    COUNT_LAST_OPERATIONS = 5
    FILENAME = 'operations.json'

    data = get_data(FILENAME)
    data = get_executed_operations(data)
    data = get_last_operations(data, COUNT_LAST_OPERATIONS)
    data = get_formatted_data(data)

    for row in data:
        print(row, end="\n\n")


if __name__ == '__main__':
    main()
