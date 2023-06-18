from utils import get_data, get_executed_operations, get_last_operations, get_formatted_data

COUNT_LAST_OPERATIONS = 3


def main():
    data = get_data()
    data = get_executed_operations(data)
    data = get_last_operations(data, COUNT_LAST_OPERATIONS)
    data = get_formatted_data(data)

    for row in data:
        print(row, end="\n\n")


if __name__ == '__main__':
    main()
