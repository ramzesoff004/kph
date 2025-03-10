from functools import reduce

def square_numbers(numbers: list) -> list:
    return list(map(lambda num: num ** 2, numbers))

def filter_even_numbers(numbers: list) -> list:
    return list(filter(lambda num: True if num % 2 == 0 else False, numbers))

def multiply_numbers(numbers: list) -> int:
    return reduce(lambda x, y: x * y, numbers)

def sum_of_squares_of_even_numbers(numbers: list) -> int:
    return reduce(lambda x, y: x + y,
                  map(lambda num: num ** 2, filter(lambda num: True if num % 2 == 0 else False, numbers)))

def result(string):
    return dict(map(lambda item: (item, len(item)), string.split()))
