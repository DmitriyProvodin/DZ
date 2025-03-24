"""импортируем файлы из masks"""
from . import masks

'создаём функцию шифрования данных'
def mask_account_card(nums: str) -> str:
    if "Счёт" in nums:
        return masks.get_mask_account(nums)
    else:
        cards = masks.get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


print(mask_account_card("Visa Platinum 7000792289606361"))

'возвращаем корректную дату'
def get_data(date: str) -> str:
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_data("2024-03-11T02:26:18.671407"))
