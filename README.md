# Final Project - Crypto Consult
#### Video Demo:  <https://www.youtube.com/watch?v=9OEzxx4hgXA>
#### Description:

# Cryptocurrency Management Program

This Python program allows users to manage their cryptocurrency activities conveniently. It offers several functionalities using data fetched from the CoinGecko API.

## Features

1. **View Crypto Prices in USD/BRL**
   - Users can check the current price of any cryptocurrency supported by CoinGecko in either USD or BRL.

2. **Record Purchases in CSV**
   - Users can log their cryptocurrency purchases, storing details such as cryptocurrency name, amount purchased, and purchase price in USD.

3. **View Purchase History and Compare**
   - Users can access their entire purchase history stored in a CSV file (`history.csv`), view recent entries, and compare their purchase prices with the current market value of the cryptocurrencies.

## Usage

Upon running `main.py`, the program prompts the user to select from the following options:

- **Option 1:** View current cryptocurrency prices.
- **Option 2:** Record a new cryptocurrency purchase.
- **Option 3:** View purchase history and compare with current prices.

## Requirements

- Python 3.x
- `requests` library
- `pandas` library

## Example

Here’s an example of using the program to view the price of Bitcoin in USD:

```plaintext
What do you want to do?
Enter 1 to see the price of a cryptocurrency in BRL or USD.
Enter 2 to enter a new record of purchase of some cryptocurrency.
Enter 3 to see your history of purchases.
Enter any option: 1

Option 1 selected: See the price of a cryptocurrency.

Which cryptocurrency do you want to see? bitcoin

You want to see in USD price or in BRL price? usd

The current price of Bitcoin in USD is: $38880.37

```

## Credits

- This program uses the CoinGecko API for fetching cryptocurrency data.

- Built by Your Name.
