
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170,
    "MSFT": 420
}

# Initialize total investment
total = 0

print("===================================")
print("       STOCK PORTFOLIO TRACKER")
print("===================================")

# Get number of stocks
n = int(input("Enter number of stocks: "))

# Get stock details
for i in range(n):

    print("\nStock", i + 1)

    name = input("Enter stock name: ").upper()

    quantity = int(input("Enter quantity: "))

    # Check stock availability
    if name in stock_prices:

        price = stock_prices[name]

        investment = price * quantity

        total = total + investment

        print("\nStock Name:", name)
        print("Stock Price:", price)
        print("Quantity:", quantity)
        print("Investment Value:", investment)

    else:
        print("Stock not found!")

# Display total investment
print("\n===================================")
print("       PORTFOLIO SUMMARY")
print("===================================")

print("Total Investment:", total)

print("===================================")
print("       THANK YOU!")
