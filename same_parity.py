def same_parity(numbers):
    if len(numbers) < 2:
        return list(numbers)
    else:
        rest = numbers[0]%2 
        return [numbers[0]] + [numbers[i] for i in range(1, len(numbers)) if numbers[i]%2 == rest]


numbers = [1]
n2 = same_parity(numbers)
n2[0] = 444
print(numbers)