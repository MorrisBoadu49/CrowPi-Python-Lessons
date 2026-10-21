import random
import time
from gpiozero import Buzzer

# Set up the buzzer
buzzer = Buzzer(18)

# Pick two random numbers between 1 and 15
a = random.choice(range(1, 16))
b = random.choice(range(1, 16))

# Ask the question
print("What is", a, "*", b, "?")
answer = input("Enter your answer: ")
answer = int(answer)

# Check the answer
if answer == a * b:
    print("Correct! You got it right!")

    buzzer.on()
    time.sleep(0.5)
    buzzer.off()

else:
    print("Wrong answer!")
    print("The correct answer is", a * b)

    buzzer.on()
    time.sleep(10)
    buzzer.off()

buzzer.close()
