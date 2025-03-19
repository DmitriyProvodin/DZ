from . import masks


def mask_account_card(nums: str) -> str:
    if 'Счёт' in nums:
        return masks.get_mask_account(nums)
    else:
        cards = masks.get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card

print(mask_account_card('Visa Platinum 7000792289606361'))