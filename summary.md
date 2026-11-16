# Currency Converter --- Project Summary

## Project Overview

**Project:** Currency Converter\
**Institution:** Rungta International Skills University\
**School:** School of Computer Science and Engineering\
**Student:** Chumendra Patel\
**PS Number:** 35\
**Course:** B.Tech Computer Science and Engineering, 1st Semester\
**Programming Language:** Python 3

## Objective

The project is a console-based application that converts an amount
between Indian Rupees (INR), US Dollars (USD), Euros (EUR), and British
Pounds (GBP).

## Fixed Exchange Rates

The program uses the following fixed sample rates (these are not live
market rates):

  Currency     Value in INR
  ---------- --------------
  INR                     1
  USD                    83
  EUR                    90
  GBP                   105

## How the Program Works

1.  The user enters an amount.
2.  The program checks that the amount is numeric and is not negative.
3.  The user enters the source and target currency codes.
4.  The program checks that both currency codes are supported.
5.  The source amount is converted to INR using `convert_to_inr()`.
6.  The INR amount is converted to the target currency using
    `convert_from_inr()`.
7.  `convert_currency()` combines the conversion steps and rounds the
    result to two decimal places.
8.  The result is displayed in the console.

## Main Functions

-   `convert_to_inr(amount, from_currency)`: Converts the source amount
    into INR.
-   `convert_from_inr(amount_in_inr, to_currency)`: Converts an INR
    amount into the target currency.
-   `convert_currency(amount, from_currency, to_currency)`: Performs the
    complete conversion through INR and rounds the answer.
-   `main()`: Handles user input, validation, and output.

## Python Concepts Used

Functions, dictionaries, conditional statements, arithmetic operators,
input/output, and exception handling (`try`/`except`).

## Input Validation

-   Non-numeric amounts are rejected with an error message.
-   Negative amounts are rejected.
-   Unsupported currency codes are rejected.
-   Currency codes are converted to uppercase, so lowercase input is
    also accepted.

## How to Run

Open a terminal in the project folder and run:

``` bash
python currency_converter.py
```

Then enter the amount, source currency, and target currency when
prompted.

## Sample Test Cases

  Input (amount, from, to)   Expected output
  -------------------------- ------------------------------
  `166, INR, USD`            `166 INR = 2.00 USD`
  `0, USD, INR`              `0 USD = 0.00 INR`
  From currency `JPY`        Unsupported currency message
  Amount `abc`               Invalid amount message
  Amount `-50`               Negative amount message
  `100, USD, EUR`            `100 USD = 92.22 EUR`
  `2, GBP, INR`              `2 GBP = 210.00 INR`
  `45, EUR, USD`             `45 EUR = 48.80 USD`

## Project Files

-   `currency_converter.py` --- Python console application.
-   `README.md` --- Project documentation and test cases.
-   `summary.md` --- Brief summary of the project.
