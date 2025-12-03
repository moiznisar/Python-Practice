overall_total = 0
overall_above_1000 = 0

customers = int(input("Enter number of customers: "))

for cust in range(1, customers+1):
    total_amount_withdrawn = 0
    withdrawals_above_1000 = 0

    num_withdrawals = int(input(f"\nCustomer {cust}, number of withdrawals: "))

    for withdraw in range(1, num_withdrawals+1):
        amount = int(input(f"Customer {cust}, withdrawal {withdraw} amount: "))

        if amount > 1000:
            withdrawals_above_1000 += 1
            overall_above_1000 += 1
        
        total_amount_withdrawn += amount
        overall_total += amount
    
    print(f"Customer {cust} - Total withdrawn: ${total_amount_withdrawn}, Withdrawals > 1000: {withdrawals_above_1000}")

print(f"\nOverall total withdrawn: ${overall_total}")
print(f"Total withdrawals > 1000: {overall_above_1000}")