def select_numbers(numbers, threshold):
    
    result = []
    for num in numbers:
        if num % 2 == 0 and num > threshold:
            result.append(num)
    return result
