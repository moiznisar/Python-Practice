critical = 0
non_critical = 0
days_present = 0

patients = int(input("Enter number of patients: "))

for p in range(1, patients + 1):
    age = int(input(f"\nEnter age of the patient {p}: "))
    severity_level = int(input(f"Enter severity level of the patient {p}: "))
    days = int(input(f"Enter days the patient {p} was admitted for: "))
    days_present += days

    if severity_level >= 7:
        critical += 1
    else:
        non_critical += 1

average_days = days_present / patients

print(f"\nTotal critical patients: {critical}")
print(f"Total non critical patients: {non_critical}")
print(f"Average days patient spend: {average_days}")