# Python Practice Exercises

This beginner-friendly project collects my Python exercises while I learn
functions, lists, loops, conditions, strings, and basic Git/GitHub workflow.

## Exercises

- `analyze_numbers(numbers)` returns the largest and smallest values.
- `calculate_discount(price, discount)` returns the price after a percentage discount.
- `find_even(numbers)` returns the even values in a list.
- `even_or_odd(number)` identifies whether a number is even or odd.
- `string_to_array(string)` splits a sentence into words.
- `count_sheep(number)` and `greet(name)` practice formatted strings.

## Run the exercises

From the project folder, start Python:

```bash
python3
```

Then try:

```python
from exercises.numbers import analyze_numbers
from exercises.discount import calculate_discount

print(analyze_numbers([12, 5, 8, 21, 4, 17, 8]))
print(calculate_discount(1000, 20))
```

Expected output:

```text
(21, 4)
800.0
```

## Run the tests

This project uses Python's built-in `unittest`, so no extra packages are
required:

```bash
python3 -m unittest discover -v
```

## Note about corrections

The original `calculate_discount` idea was correct after changing the
discount calculation to:

```python
discount_amount = (price * discount) / 100
```

The repository keeps the same beginner-friendly loop and condition logic.
It adds only a clear error for an empty list in `analyze_numbers`, because
there is no first value to use as the initial largest and smallest value.

