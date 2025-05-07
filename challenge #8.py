def double_evens(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num * 2)
        else:
            pass
output = double_evens([2, 3, 4, 5, 6])
print(output)
