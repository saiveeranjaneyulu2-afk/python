#1
for i in range (1, 6):
    total = 0
    print(f'enter marks for students {i}:')
    for j in range (1, 4):
        mark = int(input(f'subject {j}:'))
        total += mark
    print(f'student {i} total = {total}\n')

#2
for product_num in range(1, 5):
    total_sales=0
    print(f'entering sales for product {product_num}:')
    for day in range (1, 8):
        sales=int(input(f' day  {day} sales: '))
        total_sales += sales
    print(f'product {product_num} total')

#3
for i in range (1, 5):
    print(f'enter marks for sub {i}:')
    max_mark = 0
    for j in range(1, 6):
        mark = int(input(f'subject {j} mark: '))
        if mark > max_mark:
            max_mark = mark
    print(f'higest mark for stdu {i} = {max_mark}\n')

#4
for row in range(1, 6):
    booked_count = 0
    print(f'enter booking status for row {row} :')
    for seat in range(1, 7):
        status = int(input(f' seat {seat}: '))
        if status == 1:
            booked_count += 1
    print(f'row {row} booked seats = {booked_count}\n') 