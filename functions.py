def sum_digits(number):
    
    n = abs(number)
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10
    return total_sum


def average(numbers):
    
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):

    words = text.split()
    return " ".join(words)
