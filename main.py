# Stroop Test

# Initialize variables
correct_answers = 0
incorrect_answers = 0

# Display instructions for the test
print("Welcome to the Stroop Test!")
print("In this test, you will be shown a series of words that are printed in different colors.")
print("Your task is to name the color of the word, NOT the meaning of the word.")
print("For example, if the word 'BLUE' is printed in red, you should say 'red'.")
print("Press enter to begin the test.")
input()

# Start the test
while True:
  # Generate a random word and color
  import random
  colors = ['red', 'green', 'blue', 'yellow']
  word = random.choice(colors)
  color = random.choice(colors)

  # Display the word and color to the user
  print(f"The word is: {word}")
  print("What is the color of the word?")

  # Get the user's answer
  answer = input().lower()

  # Check if the answer is correct
  if answer == color:
    print("Correct!")
    correct_answers += 1
  else:
    print(f"Incorrect. The correct answer was: {color}")
    incorrect_answers += 1

  # Ask the user if they want to continue
  print("Press enter to continue the test, or type 'exit' to stop the test.")
  user_input = input().lower()
  if user_input == 'exit':
    break

# Display the results
print("Test complete!")
print(f"Correct answers: {correct_answers}")
print(f"Incorrect answers: {incorrect_answers}")


