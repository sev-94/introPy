i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

#guessing game----------------------------

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word:
    guess = input("Enter guess: ")
    guess_count += 1
    if(guess_count == 3):
        guess = secret_word

if(guess_count == 3):
    print("You Lose")
else:
    print("You win!")