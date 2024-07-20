# While loop : As long as the variable is true
number = 1

while number <= 10:
    if number % 2 == 0:
        print(number)
    number = number + 1

print("while loop ends")

# mini game : guess number

luckyNumber = 87
guess = 0

while guess != luckyNumber:
    guess = int(input("Guess a number"))
print("you have won 50 crores")