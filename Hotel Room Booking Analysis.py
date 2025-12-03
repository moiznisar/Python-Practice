total_rooms_booked = 0
total_income = 0
suites_booked = 0
highest_price = 0

while True:
    room_type = input("\nEnter room type (blank to stop): ")
    if room_type == "":
        break

    nights_stayed = int(input("Enter number of nights: "))
    price_per_night = float(input("Enter price per night: $"))

    total_rooms_booked += 1
    income_per_room = nights_stayed * price_per_night
    total_income += income_per_room

    if room_type == "suite":
        suites_booked += 1

    if price_per_night > highest_price:
        exp_room = room_type
        highest_price = price_per_night

if total_rooms_booked > 0:
    average_income = total_income / total_rooms_booked
else:
    average_income = 0

print(f"\nTotal rooms booked: {total_rooms_booked}")
print(f"Total income generated: ${total_income}")
print(f"Suites booked: {suites_booked}")
print(f"Average income per room: ${average_income}")

print(f"Highest priced room per night was {exp_room} at ${highest_price}")
