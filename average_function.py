

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

numbers = [70, 85, 90]
result = average(numbers)
print ("The average is:", round(result, 3))