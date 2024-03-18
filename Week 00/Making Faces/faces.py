# Prompt input
user_input = input("Enter some text: ")

# Convert emoticons to emoji
converted_input = user_input.replace(":)", "🙂").replace(":(", "🙁")

# Printing the result
print(converted_input)
