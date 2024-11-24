numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

rounded_numbers = [round(num/10)*10 for num in numbers]

max = rounded_numbers[0]
min = rounded_numbers[0]

for number in rounded_numbers:
    if number > max:
        max = number
    if number < min:
        min = number

mean_number = int(sum(rounded_numbers) / len(rounded_numbers))

print(f"max is {max}")
print(f"min is {min}")
print(f"mean is {mean_number}")
