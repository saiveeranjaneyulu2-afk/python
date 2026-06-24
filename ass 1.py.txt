num=int(input("Enter a positive number: "))
start = 1
sum = 0
while num <= 0:
    if num<0:
        print("Error, you have entered a negative number.")
    elif num==0:
        print("You have entered zero.")
    num=int(input("Enter a positive number: "))
    if num > 0:
        break
while start <= num:
    sum += start
    start +=1
print(f"The total sum of numbers from 1 to {num} is {sum}")