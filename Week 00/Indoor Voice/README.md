# Indoor Voice

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Indoor Voice Problem Set](https://cs50.harvard.edu/python/2022/psets/0/indoor/), named `indoor.py`, prompts the user for input and then outputs the same input in lowercase, while preserving punctuation and whitespace. It is designed to provide a more calm and polite "indoor voice" experience when handling user input.

## Program Code

```python
# indoor.py

# Prompting the user for input
user_input = input("Enter some text: ")

# Converting input to lowercase and printing
lowercase_input = user_input.lower()
print(lowercase_input)
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various types of input, including text with uppercase letters, numbers, punctuation, and whitespace.
3. The program should output the input in lowercase while keeping the punctuation and whitespace unchanged.

## Sample Test Cases

1. **Input:** HELLO
   **Output:** hello

2. **Input:** THIS IS CS50
   **Output:** this is cs50

3. **Input:** 50
   **Output:** 50
