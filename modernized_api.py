
def calculate_interest(principal, rate, term):
    # Modern implementation of financial logic
    from decimal import Decimal, ROUND_HALF_UP
    p = Decimal(str(principal))
    r = Decimal(str(rate))
    t = Decimal(str(term))
    
    # Logic: I = P * R * T / 12
    # Using strict Decimal arithmetic for banking compliance
    interest = (p * (r / 100) * t) / 12
    return interest.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
