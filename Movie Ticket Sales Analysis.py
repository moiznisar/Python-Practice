total_revenue = 0
total_child = 0
total_adult = 0
total_senior = 0

num_shows = int(input("Enter number of shows: "))

for show in range(1, num_shows + 1):
    print(f"\nShow {show}:")
    show_revenue = 0
    child_tickets = 0
    adult_tickets = 0
    senior_tickets = 0

    num_tickets = int(input(f"Enter number of tickets for show {show}: "))

    for ticket in range(1, num_tickets + 1):
        age = int(input(f"Show {show}, Ticket {ticket} age: "))

        if age <= 12:
            price = 8
            child_tickets += 1
        elif 13 <= age <= 59:
            price = 12
            adult_tickets += 1
        else:
            price = 10
            senior_tickets += 1

        show_revenue += price

    print(f"Show {show} - Revenue: ${show_revenue}, Child: {child_tickets}, Adult: {adult_tickets}, Senior: {senior_tickets}")

    total_revenue += show_revenue
    total_child += child_tickets
    total_adult += adult_tickets
    total_senior += senior_tickets

print("\nOverall Summary:")
print(f"Total Revenue: ${total_revenue}")
print(f"Total Child Tickets: {total_child}")
print(f"Total Adult Tickets: {total_adult}")
print(f"Total Senior Tickets: {total_senior}")