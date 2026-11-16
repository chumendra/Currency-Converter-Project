 Currency-Converter-Project
A Python 3 console currency converter for INR, USD, EUR, and GBP using fixed exchange rates.


Project detail 
 Information 

 Project title - Currency Converter 
 Student name - Chumendra Patel
 PS number    - 35
 Course       - B.Tech Computer Science and Engineering, 1st Semester
 Language     - Python 3 

 Problem statement

Build a console-based program that converts an amount between INR, USD, EUR, and GBP. Store the fixed exchange rates in a dictionary, route each conversion through INR, validate the amount and currency codes, and display the result rounded to two decimal places.

 Exchange rates

These are the fixed sample rates used by this project, not live market rates:

1 USD = 83 INR
1 EUR = 90 INR
1 GBP = 105 INR
1 INR = 1 INR

 Concepts used

Functions, conditions,operators, dictionaries.

 Conversion logic

The program first converts the source amount to INR using `convert_to_inr()` . It then converts that INR amount to the target currency using `convert_from_inr()` . `convert_currency()` combines these steps and rounds the result to two decimal places. The console interface checks that the amount is numeric and non-negative, and that both currency codes are supported.

 Run the program

Open a terminal in the project folder and run:

```text
python currency_converter.py
```

Enter the amount, source currency, and target currency when prompted. Currency codes are case-insensitive.

## Test cases

| Case | Input (amount, from, to) | Expected result |
|---|---|---|
| Normal input | `166`, `INR`, `USD` | `166 INR = 2.00 USD` |
| Minimum input | `0`, `USD`, `INR` | `0 USD = 0.00 INR` |
| Unsupported currency | From: `JPY` | `Unsupported currency 'JPY'. Available: INR, USD, EUR, GBP` |
| Non-numeric amount | Amount: `abc` | `Invalid amount. Enter a number.` |
| Negative amount | Amount: `-50` | `Amount cannot be negative.` |
| Valid conversion | `100`, `USD`, `EUR` | `100 USD = 92.22 EUR` |
| Valid conversion | `2`, `GBP`, `INR` | `2 GBP = 210.00 INR` |
| Valid conversion | `45`, `EUR`, `USD` | `45 EUR = 48.80 USD` |

## Files

- `currency_converter.py` — Python console application
- `README.md` — project documentation and test cases
