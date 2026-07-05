Problem 1 – Nested while:
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        if (i + j) % 2 == 0:
            print(f"({i},{j})")
        j += 1
    i += 1

Problem 2 – Nested while:
i = 1
count = 0
while i <= 10:
    j = 1
    while j <= 10:
        if i * j > 30:
            print(f"({i},{j}) -> {i*j}")
            count += 1
        j += 1
    i += 1
print("Total pairs:", count)

Problem 3 – For inside While:
num = int(input("Enter a number: "))  # first input

while num != 0:  # while loop keeps running until 0
    factors = []
    total_sum = 0
    
    for i in range(1, num + 1):  # for loop inside while
        if num % i == 0:  # factor condition
            factors.append(i)
            total_sum += i
    
    print(f"Number: {num}")
    print(f"Factors: {factors}")
    print(f"Sum of factors: {total_sum}")
    print()
    
    num = int(input("Enter a number: "))  # take next input

print("Program ended")

Problem 4 – While inside For:
numbers = [12, 7, 20, 9]

for num in numbers:
    print(f"\n{num} -> ", end="")
    
    i = 1
    even_count = 0
    
    while i <= num:
        print(i, end=" ")
        if i % 2 == 0:
            even_count += 1
        i += 1
        
    print(f" Even count: {even_count}")
