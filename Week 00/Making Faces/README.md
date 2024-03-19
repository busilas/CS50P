# Making Faces

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Making Faces Problem Set](https://cs50.harvard.edu/python/2022/psets/0/faces/), named `faces.py`, provides functionality to convert emoticons like :) and :( to their corresponding emoji equivalents, namely 🙂 (slightly smiling face) and 🙁 (slightly frowning face). The program includes a `convert` function that performs the conversion, and a `main` function that prompts the user for input, calls the `convert` function, and prints the result.

## Program Code

```python
# faces.py

# Prompt input
user_input = input("Enter some text: ")

# Convert emoticons to emoji
converted_input = user_input.replace(":)", "🙂").replace(":(", "🙁")

# Printing the result
print(converted_input)
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various types of input containing :) and :( emoticons.
3. The program should output the input text with the corresponding emoji conversions.

## Sample Test Cases

1. **Input:** Hello :)
   **Output:** Hello 🙂

2. **Input:** Goodbye :(
   **Output:** Goodbye 🙁

3. **Input:** Hello :) Goodbye :(
   **Output:** Hello 🙂 Goodbye 🙁
