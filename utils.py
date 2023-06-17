import json
from datetime import datetime


def get_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_executed_operations(data):
    data = [x for x in data if 'state' in x and x['state'] == "EXECUTED"]
    return data


def get_last_operations(data, quantity):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:quantity]
    return data


def encode_bill_info(bill_info):
    bill_info = bill_info.split()
    bill, info = bill_info[-1], ' '.join(bill_info[:-1])
    if len(bill) == 16:
        bill = f'{bill[:4]} {bill[4:6]}** **** {bill[-4:]}'
    else:
        bill = f'**{bill[-4:]}'

    return f"{info} {bill}"


def get_formatted_data(data):
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

#         formatted_data.append(f"""
# {date} {description}
# {sender} {to}
# {operations_amount}""")
        formatted_data.append(f"""\
{date} {description}
{sender}{to}
{operations_amount}""")
    return formatted_data
