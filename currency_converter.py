rates_to_inr = {
    'INR': 1.0,
    'USD': 83.0,
    'EUR': 90.0,
    'GBP': 105.0
}

def convert_to_inr(amount, from_currency):
    """Converts the given amount from a source currency to INR."""
    return amount * rates_to_inr[from_currency]

def convert_from_inr(amount_in_inr, to_currency):
    """Converts an amount in INR to the target currency."""
    return amount_in_inr / rates_to_inr[to_currency]

def convert_currency(amount, from_currency, to_currency):
    """Converts amount from_currency to to_currency going through INR."""
    amount_in_inr = convert_to_inr(amount, from_currency)
    final_amount = convert_from_inr(amount_in_inr, to_currency)
    return round(final_amount, 2)

def main():
    print("--- Console Currency Converter ---")
    
    # 1. Input Amount validation
    amount_input = input("Amount: ")
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Enter a number.")
        return

    if amount < 0:
        print("Amount cannot be negative.")
        return

    # 2. From Currency validation
    from_currency = input("From: ").upper()
    supported = list(rates_to_inr.keys())
    if from_currency not in supported:
        print(f"Unsupported currency '{from_currency}'. Available: {', '.join(supported)}")
        return

    # 3. To Currency validation
    to_currency = input("To: ").upper()
    if to_currency not in supported:
        print(f"Unsupported currency '{to_currency}'. Available: {', '.join(supported)}")
        return

    # Perform Conversion
    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount:g} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()