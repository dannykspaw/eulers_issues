sum_of_squares = 0
square_of_sum = 0
for i in range(101):
    sum_of_squares = sum_of_squares + i**2
for i in range(101):
    square_of_sum = square_of_sum + i
square_of_sum = square_of_sum**2
print(abs(sum_of_squares - square_of_sum))

