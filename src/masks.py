from typing import Union

def get_mask_card_number(card_number: Union[str, int]) -> Union[str]:
    """Возвращаем замаскированный номер карты"""
    len_number = 16
    if isinstance(card_number, int):
        card_number = str(card_number)
    if len(card_number) == len_number and card_number.isdigit():
        return f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    else:
        return "Вы ввели некорректные данные!"

def get_mask_account(account_number: Union[str, int]) -> Union[str]:
    """Возвращаем замаскированный номер счёта"""
    len_acc_number = 20
    if isinstance(account_number, int):
        account_number = str(account_number)
    if len(account_number) == len_acc_number and account_number.isdigit():
        return f'**{account_number[-4:]}'
    else:
        return "Вы ввели некорректные данные!"

if __name__ == "__main__":
    card_number: str = input("Введите номер карты:")
    account_number: str = input("Введите номер счета:")

    print(get_mask_card_number(card_number))
    print(get_mask_account(account_number))
