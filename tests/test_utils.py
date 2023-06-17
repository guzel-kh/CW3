import pytest
from utils import get_executed_operations, get_last_operations, get_formatted_data, encode_bill_info


def test_get_executed_operations(test_data):
    data = get_executed_operations(test_data)
    assert len(data) == 3


def test_get_last_operations(test_data):
    data = get_last_operations(test_data, 2)
    assert [x['date'] for x in data] == ["2021-12-20T16:43:26.929246", "2019-08-26T10:50:58.294041"]


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.',
                    '20.12.2021 Перевод организации\nСчет **5355 -> Счет **6366\n70946.18 USD',
                    '11.07.2018 Открытие вклада\nСчет **6215\n79931.03 руб.',
                    '12.01.2018 Перевод организации\nVisa Platinum 1246 37** **** 3588 -> Счет **1657\n67314.70 руб.']


@pytest.mark.parametrize("test_input, expected", [
    ("Visa Platinum 1246377376343588", "Visa Platinum 1246 37** **** 3588"),
    ('Счет 14211924144426031657', 'Счет **1657')])
def test_encode_bill_info(test_input, expected):
    assert encode_bill_info(test_input) == expected
