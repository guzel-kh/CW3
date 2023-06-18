import json
from datetime import datetime


def get_data() -> list:
    """возвращает данные файла .json в list"""
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_executed_operations(data: list) -> list:
    """
    Оставляет в списке только выполненные операции ("EXECUTED" по ключу "state")
    :param data: list
    :return: list
    """
    data = [x for x in data if 'state' in x and x['state'] == "EXECUTED"]
    return data


def get_last_operations(data: list, quantity: int) -> list:
    """
     возвращает выбранное количество самых последних операций (по дате)
    :param data: list
    :param quantity: int, количество операций для вывода
    :return: list
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:quantity]
    return data


def encode_bill_info(bill_info: str) -> str:
    """
    Возвращает замаскированный номер карты в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4,
    разбито по блокам по 4 цифры, разделенных пробелом)
    или номер счета в формате  **XXXX (видны только последние 4 цифры номера счета)
    :param bill_info: str информация по счету (название счета/карты и номер)
    :return: str
    """

    bill_info = bill_info.split()
    bill, info = bill_info[-1], ' '.join(bill_info[:-1])
    if len(bill) == 16:
        bill = f'{bill[:4]} {bill[4:6]}** **** {bill[-4:]}'
    else:
        bill = f'**{bill[-4:]}'

    return f"{info} {bill}"


def get_formatted_data(data: list) -> list:
    """
    Возвращает информацию по операции в формате:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    Пример вывода для одной операции:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    :param data:list список с данными
    :return: list форматированные данные
    """
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        if 'from' in row:
            sender = encode_bill_info(row['from'])
            sender = f'{ sender } -> '
        else:
            sender = ''

        to = encode_bill_info(row['to'])

        operations_amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'

        formatted_data.append(f"""\
{date} {description}
{sender}{to}
{operations_amount}""")
    return formatted_data
