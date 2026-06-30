# Program to print even numbers from 1 to 10
# Stops when the number 8 is encountered
i = 1
while i <= 10:
    if i == 8:
        print("Encountered 8, stopping the loop.")
        break
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1

===================== ASSMENT 3 ======================
#1 Program to accept ages until user enters -1
# Ignore ages below 1 and above 120 using continue
# Count only valid ages (without using break)
count = 0
age = 0
while age != -1:
    age = int(input("Enter age: "))
    if age < 1 or age > 120:
        if age != -1:
            print("Invalid age ignored.")
        continue
    if age == -1:
        continue
    count += 1
    print(f"Valid age accepted: {age}")
print(f"Total valid ages entered: {count}")

#2
total_sum = 0
while True:
     num = int(input("enter a number (0 to stop): "))
     if num ==0:
          continue
     if num % 5 != 0:
          continue
     total_sum += num
print(f'sum: {total_sum}')

#3
text = "PyTHon ProGRAM"
count = 0
for char in text:
    if not char.isupper():
        continue
    count += 1
print(f'uppercase letter count:{count}')

#4
sales=[500, 0, 1200, 0, 700]
total_sales=0
for sale in sales:
    if sale ==0:
        continue
    total_sales += sale
print("total sales amount:",total_sales)