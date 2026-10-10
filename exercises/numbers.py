"""Exercises for working with numbers and lists."""


def analyze_numbers(numbers):
    """Return the largest and smallest number in a non-empty list."""
    if not numbers:
        raise ValueError("numbers must not be empty")

    largest_num = numbers[0]
    smallest_num = numbers[0]

    for number in numbers:
        if number > largest_num:
            largest_num = number
        if number < smallest_num:
            smallest_num = number

    return largest_num, smallest_num


def find_even(numbers):
    """Return the even numbers from a list."""
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def even_or_odd(number):
    """Return whether a number is even or odd."""
    return "Even" if number % 2 == 0 else "Odd"

