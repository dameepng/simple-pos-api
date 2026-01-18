from decimal import Decimal, ROUND_HALF_UP

MONEY_PLACES = Decimal("0.01")

def to_decimal(value) -> Decimal:
    # Convert aman dari int/float/str ke Decimal
    # str(value) mencegah float binary issue masuk ke Decimal
    return Decimal(str(value))

def quantize_money(amount: Decimal) -> Decimal:
    return amount.quantize(MONEY_PLACES, rounding=ROUND_HALF_UP)
