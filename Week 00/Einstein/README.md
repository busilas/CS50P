# Einstein

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Einstein Problem Set](https://cs50.harvard.edu/python/2022/psets/0/einstein/), named `einstein.py`, calculates the energy equivalent (in Joules) of a given mass (in kilograms) using Einstein's mass-energy equivalence formula, E = mc^2. The program prompts the user for mass as an integer (in kilograms) and outputs the equivalent energy in Joules.

## Program Code

```python
# einstein.py

# Prompt mass
mass = int(input("m: "))

# Speed of light
speed_of_light = 300000000

# Calculating energy using Einstein's famous formula
joules = mass * speed_of_light ** 2

# Outputting the equivalent energy in Joules
print("E:", joules)
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various mass values in kilograms.
3. The program should output the energy equivalent in Joules based on Einstein's mass-energy equivalence formula.

## Sample Test Cases

1. **m:** 1
   **E:** 90000000000000000

2. **m:** 14
   **E:** 1260000000000000000

3. **m:** 50
   **E:** 4500000000000000000

