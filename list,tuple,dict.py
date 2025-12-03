numbers = [12, 7, 19, 24, 5, 17, 8]
even_count = 0
odd_count = 0

for digit in numbers:
    if digit % 2 == 0:
        print(f"{digit} is even")
        even_count += 1
    else:
        print(f"{digit} is odd")
        odd_count += 1

print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")