import json
import sys
import requests

if len(sys.argv) == 2:
    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = response.json()
    price = response["bpi"]["USD"]["rate"].replace(",", "")
    print(f"${number_of_bitcoins * float(price):,.4f}")

elif len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
