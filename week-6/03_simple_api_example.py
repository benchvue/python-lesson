# This example shows API structure without requiring internet access.

exchange_rate_response = {
    "base": "USD",
    "target": "EUR",
    "rate": 0.92
}

usd_amount = 100
eur_amount = usd_amount * exchange_rate_response["rate"]

print("USD:", usd_amount)
print("EUR:", eur_amount)
