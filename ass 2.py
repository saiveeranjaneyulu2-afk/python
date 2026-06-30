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