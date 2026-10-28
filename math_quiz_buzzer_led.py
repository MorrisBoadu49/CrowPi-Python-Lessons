import random
import time
from gpiozero import Buzzer, LED

# Set up the buzzer
buzzer = Buzzer(18)

# Example LED pins (not yet confirmed for CrowPi)
green_led = LED(17)
red_led = LED(27)

# Pick two random numbers between 1 and 16
a = random.choice(range(1, 17))
b = random.choice(range(1, 17))

# Pick a random operator
operator = random.choice(["+", "-", "*"])

# Calculate the correct answer
if operator == "+":
    correct_answer = a + b

elif operator == "-":
    correct_answer = a - b

else:
    correct_answer = a * b

# Ask the question
print("What is", a, operator, b, "?")
answer = int(input("Enter your answer: "))

# Check the answer
if answer == correct_answer:
    print("Correct! You got it right!")

    green_led.on()
    buzzer.on()

    time.sleep(0.5)

    green_led.off()
    buzzer.off()

else:
    print("Wrong answer!")
    print("The correct answer is", correct_answer)

    red_led.on()
    buzzer.on()

    time.sleep(10)

    red_led.off()
    buzzer.off()

# Clean up
buzzer.close()
green_led.close()
red_led.close()
