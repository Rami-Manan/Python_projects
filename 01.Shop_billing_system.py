"""
Shop billing system with GST/CGST/SGST calculation.
"""

items = []  # each entry: {"name": str, "qty": int, "price": float, "total": float}

# --- Item entry loop -------------------------------------------------------
while True:
    name = input("Enter the item name: ")
    qty = int(input("Enter the quantity: "))
    price = float(input("Enter the price per item: "))
    total = qty * price

    items.append({"name": name, "qty": qty, "price": price, "total": total})

    choice = input("Do you want to add more items? (yes/no): ").strip().lower()
    if choice != "yes":
        break

# --- GST variant selection ---------------------------------------------------
print("01. Hotel Bill (3% GST)")
print("02. Electronics Bill (18% GST)")
print("03. Grocery Bill (5% GST)")
print("04. Clothing Bill (12% GST)")
print("05. Stationery Bill (18% GST)")
print("06. Medical Bill (5% GST)")

gst_choice = int(input("choose bill variant (1-6): "))
print()

match gst_choice:
    case 1:
        print("you have chosen hotel bill")
        rate = 0.03
    case 2:
        print("you have chosen electronics bill")
        rate = 0.18
    case 3:
        print("you have chosen grocery bill")
        rate = 0.05
    case 4:
        print("you have chosen clothing bill")
        rate = 0.12
    case 5:
        print("you have chosen stationery bill")
        rate = 0.18
    case 6:
        print("you have chosen medical bill")
        rate = 0.05
    case _:
        print("invalid choice")
        rate = 0.0

# --- Totals -------------------------------------------------------------
items_subtotal = sum(item["total"] for item in items)
gst_amount = items_subtotal * rate
cgst = gst_amount / 2
sgst = gst_amount / 2
total_amount = items_subtotal + gst_amount

# --- Bill printout --------------------------------------------------------
print("-------------------------------")
print("      *** SHOP BILL ***")
print("-------------------------------")
print(f"{'Item':<12}{'Qty':>5}{'Price':>10}{'Total':>10}")
print("-------------------------------")
for item in items:
    print(f"{item['name']:<12}{item['qty']:>5}{item['price']:>10.2f}{item['total']:>10.2f}")
print("-------------------------------")
print(f"CGST : {cgst:.2f}")
print(f"SGST : {sgst:.2f}")
print("-------------------------------")
print(f"Total bill: {total_amount:.2f}")
print("-------------------------------")

print("THANK YOU FOR VISITING OUR SHOP!")
