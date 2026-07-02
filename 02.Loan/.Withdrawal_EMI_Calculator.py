"""
Loan/Withdrawal EMI Calculator

Given a withdrawal amount and a tenure (11-21 months), computes the
applicable interest rate, total payable amount, and monthly EMI.
"""

# Interest rate table: tenure (months) -> annual interest rate (%)
# NOTE: preserved exactly as given in the original code. The rates rise by
# ~1.02% per month EXCEPT at month 16 (15.18 -> 17, a 1.82% jump) and the
# following step (17 -> 18.12, only +1.12%). This breaks the otherwise
# linear pattern - confirm whether that's an intentional business rule or
# a data entry error in the source you're working from.
RATE_TABLE = {
    11: 11.00,
    12: 12.12,
    13: 13.14,
    14: 14.16,
    15: 15.18,
    16: 17.00,
    17: 18.12,
    18: 19.14,
    19: 20.16,
    20: 21.18,
    21: 22.00,
}


def get_positive_amount(prompt: str) -> float:
    """Repeatedly prompt until the user enters a positive number."""
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("  Please enter a valid number.")
            continue
        if value <= 0:
            print("  Amount must be greater than 0.")
            continue
        return value


def get_valid_month(prompt: str) -> int:
    """Repeatedly prompt until the user enters an integer in [11, 21]."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if value not in RATE_TABLE:
            print("  Month must be between 11 and 21.")
            continue
        return value


def main():
    amount = get_positive_amount("Enter withdrawal amount: ")
    month = get_valid_month("Enter tenure in months (between 11 and 21): ")

    rate = RATE_TABLE[month]
    interest = amount * rate / 100
    total_amount = amount + interest
    emi = total_amount / month

    print(f"\nWithdrawal amount : ₹{amount:,.2f}")
    print(f"Interest rate     : {rate}%")
    print(f"Interest amount   : ₹{interest:,.2f}")
    print(f"Total payable     : ₹{total_amount:,.2f}")
    print(f"Monthly EMI       : ₹{emi:,.2f}")


if __name__ == "__main__":
    main()
