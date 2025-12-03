total_stock_value = 0
total_expiring_meds = 0
total_price = 0

medicine = int(input("Enter total number of medicines: "))

most_expensive_price = 0
most_expensive_name = ""

for meds in range(1, medicine + 1):
    med_name = input(f"\nEnter the name of the medicine {meds}: ")
    med_quantity = int(input(f"Enter {med_name} quantity: "))
    price_per_unit = float(input(f"Enter price per unit of medicine {meds}: "))
    expiry_year = int(input("Enter expiry year of the medicine: "))

    total_stock_value += med_quantity * price_per_unit

    if expiry_year == 2025:
        total_expiring_meds += 1

    if price_per_unit > most_expensive_price:
        most_expensive_price = price_per_unit
        most_expensive_name = med_name

    total_price += price_per_unit

average_price = total_price / medicine

print(f"\nTotal stock value: {total_stock_value}")
print(f"Medicines expiring this year: {total_expiring_meds}")
print(f"Most expensive medicine: {most_expensive_name} (${most_expensive_price})")
print(f"Average Price: ${average_price}")
