# Playback Speed

This Python program is an implementation to [CS50’s Introduction to Programming with Python Week 0 - Playback Speed Problem Set](https://cs50.harvard.edu/python/2022/psets/0/playback/), named `playback.py`, prompts the user for input and then outputs the same input, replacing each space with three periods (`...`). This simulates a slower playback speed or deliberate pausing between words, similar to certain speech patterns observed in videos.

## Program Code

```python
# playback.py

# Prompt input
user_input = input("Enter some text: ")

# Replace spaces with ... & print
modified_input = user_input.replace(" ", "...")
print(modified_input)
```

## How to Test

1. Run the program as mentioned in the "How to Run the Program" section.
2. Enter various types of input with spaces.
3. The program should output the input text with spaces replaced by ....

## Sample Test Cases

1. **Input:** This is CS50
   **Output:** This...is...CS50

2. **Input:** This is our week on functions
   **Output:** This...is...our...week...on...functions

3. **Input:** Let's implement a function called hello
   **Output:** Let's...implement...a...function...called...hello
