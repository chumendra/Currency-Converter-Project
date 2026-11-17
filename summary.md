# Currency Converter — Project Summary

## Project Overview
* **Project:** Currency Converter
* **Institution:** Rungta International Skills University
* **School:** School of Computer Science and Engineering
* **Student Name:** Chumendra Patel
* **Class / Section:** B.Tech CSE (Section L)
* **ERP / Roll No:** RU-26-00914
* **PS Number:** 35
* **Course:** B.Tech Computer Science and Engineering, 1st Semester
* **Programming Language:** Python 3

---

## Objective
The project is a console-based Python application designed to convert monetary amounts accurately between major currencies: **Indian Rupees (INR), US Dollars (USD), Euros (EUR), and British Pounds (GBP)** using fixed exchange rates.

---

## Fixed Exchange Rates
The program uses the following fixed base rates relative to INR (for demonstration purposes):

| Currency | Code | Value in INR |
| :--- | :--- | :--- |
| Indian Rupee | `INR` | 1 |
| US Dollar | `USD` | 83 |
| Euro | `EUR` | 90 |
| British Pound | `GBP` | 105 |

---

## How the Program Works
1. The user enters the amount to be converted.
2. The program validates that the input is numeric and non-negative.
3. The user enters the source currency code (`From`) and target currency code (`To`).
4. Both currency codes are normalized to uppercase and verified against supported currencies.
5. `convert_to_inr()` converts the source amount into its equivalent INR value.
6. `convert_from_inr()` converts that INR value into the target currency.
7. `convert_currency()` orchestrates both functions and rounds the final output to 2 decimal places.
8. The final formatted result is displayed on the console.

---

## Main Functions & Concepts Used
* **`convert_to_inr(amount, from_currency)`**: Converts the input amount into INR.
* **`convert_from_inr(amount_in_inr, to_currency)`**: Converts the INR amount into the desired target currency.
* **`convert_currency(amount, from_currency, to_currency)`**: Combines both steps and rounds the result.
* **`main()`**: Manages user prompts, input validation, error messages, and console output.
* **Python Concepts Used:** Functions, Dictionaries, Conditional Statements (`if/else`), Arithmetic Operators, String Manipulation (`.upper()`, `.strip()`), and Exception Handling (`try/except`).

---

## Difficulties Faced & How I Overcame Them

1. **Handling Direct Multi-Currency Conversions:**
   * **Difficulty:** Writing separate conversion formulas for every possible currency pair (e.g., USD to EUR, EUR to GBP, GBP to USD) would have made the code repetitive and hard to maintain.
   * **Solution:** I used **INR as a common base currency**. By creating two modular functions (`convert_to_inr` and `convert_from_inr`), any currency can be converted to INR first and then to the target currency cleanly.

2. **Program Crashing on Invalid User Inputs:**
   * **Difficulty:** Entering text (like `"abc"`) instead of a number for the amount caused a `ValueError` crash, and entering negative numbers produced unrealistic currency values.
   * **Solution:** I implemented a `try/except ValueError` block to catch non-numeric inputs gracefully and added conditional checks (`amount < 0`) to reject negative numbers with clear error messages.

3. **Case-Sensitivity in Currency Codes:**
   * **Difficulty:** If a user typed `"usd"` or `"inr"` in lowercase, the dictionary lookup failed because keys were stored in uppercase (`"USD"`, `"INR"`).
   * **Solution:** I applied `.strip().upper()` to all currency inputs so that lowercase or spaced inputs are automatically standardized before validation.

---

## Working Test Cases & Output Screenshots

| Test Case | Input (Amount, From, To) | Expected Output | Status |
| :--- | :--- | :--- | :--- |
| **Normal Conversion** | `166`, `INR`, `USD` | `166 INR = 2.00 USD` | Pass |
| **Zero / Minimum Input** | `0`, `USD`, `INR` | `0 USD = 0.00 INR` | Pass |
| **Unsupported Currency** | `From: JPY` | Unsupported currency error message | Pass |
| **Non-Numeric Amount** | `Amount: abc` | Invalid amount error message | Pass |
| **Negative Amount** | `Amount: -50` | Negative amount error message | Pass |
| **Cross Conversion 1** | `100`, `USD`, `EUR` | `100 USD = 92.22 EUR` | Pass |
| **Cross Conversion 2** | `2`, `GBP`, `INR` | `2 GBP = 210.00 INR` | Pass |
| **Cross Conversion 3** | `45`, `EUR`, `USD` | `45 EUR = 48.80 USD` | Pass |

### Test Case Execution Screenshots
*(Note: Drag and drop your terminal screenshots below or upload them to a `Screenshots/` folder in your repository)*

* **Valid Conversions & Edge Cases:**
  `![Test Cases Output](Screenshots/testcases.png)`

---

## Project Files
* `currency_converter.py` — Main Python console application source code.
* `README.md` — Repository overview, setup instructions, and documentation.
* `summary.md` — Detailed project summary, challenges faced, and test case verification.
