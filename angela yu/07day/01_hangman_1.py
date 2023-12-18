

import random
from hangman_word_list import word_list
# word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
# print(chosen_word)

len_chosen_word = len(chosen_word)
# print(len_chosen_word)

lives =6

display = []
for words in range(len_chosen_word):
# for words in chosen_word:
     display += "_"
print(display)



from hangman_art import stages,logo
print(logo)


end_of_game = False
while not end_of_game :
    guess = input("Enter your lettre here :").lower()
    # print(guess)
    

    if guess in display :
        print(f"you alredy guessed the letter {guess}")

    for position in range(len_chosen_word):
    # for position in chosen_word:
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter 
    
    if guess not in chosen_word :
      print(f"you guessed a wrong letter {guess},you are losing a life ")
      lives -=1
      if lives == 0:
        end_of_game = True
        print("you lose ")
    print(display)


    if "_" not in display:
        end_of_game = True 
        print("Hurray! you won the game ")

    print(stages[lives])