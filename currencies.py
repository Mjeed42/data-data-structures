# pylint: disable=missing-docstring

RATES = {
    'USDEUR': 0.85,
    'GBPEUR': 1.13,
    'CHFEUR': 0.86,
    'EURGBP': 0.885
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """

    original_amount, original_currency = amount

    rate_key = f"{original_currency}{currency}"


    if rate_key not in RATES:
        return None

    rate = RATES[rate_key]

    converted_amount = original_amount * rate

    converted_amount_rounded = round(converted_amount)

    return converted_amount_rounded

print(convert((100, "EUR"), "USD"))
