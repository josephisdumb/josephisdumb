secret = 67
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    
    if guess == secret:
            print("You got it right!")
            break
else:
      print("Game over. The secret number was",secret)