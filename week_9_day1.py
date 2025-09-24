customer = {
    "name": "Godiya",
    "order_amount": 25000,
    "loyalty_card": True,
    "is_student": False
}

discount = 0
freebie = False

if customer["loyalty_card"]:
    discount += 10

    if customer["order_amount"] > 20000:
        discount += 5
else:
   
    if customer["order_amount"] > 20000:
        freebie = "free soft drink"

if customer["is_student"]:
    discount += 5

final_amount = customer["order_amount"] * (1 - discount / 100)

summary = {
    "name": customer["name"],
    "original_price_to_pay": customer["order_amount"],
    "discount": f"{discount}%",
    "final_amount_to_pay": final_amount,
    "freebie": freebie
}

print("Summary:")
print(f"Customer: {summary['name']}\n Original Price to pay: {summary['original_price_to_pay']} NGN\n Discount: {summary['discount']}\n Final Amount to pay: {summary['final_amount_to_pay']} NGN")
if summary['freebie']:
    print(f"Freebie: {order_summary['freebie']}")