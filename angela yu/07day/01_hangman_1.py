import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
# print(chosen_word)

len_chosen_word = len(chosen_word)
# print(len_chosen_word)

display = []
for words in range(len_chosen_word):
# for words in chosen_word:
     display += "_"
print(display)

end_of_game = False
while not end_of_game :
    guess = input("Enter your lettre here :").lower()
    print(guess)


    for position in range(len_chosen_word):
    # for position in chosen_word:
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter 
    print(display)

    if "_" not in display:
        end_of_game = True 
print("Hurray! you won the game ")