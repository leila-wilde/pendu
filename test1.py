

def play_pendu(incorrect_guesses, letter):
    secret_word, word_in_progress = first_display()
    

    for i in range(0, len(word_in_progress)):
        if letter == secret_word[i]:
            word_in_progress[i] = letter
            is_in_word = True



    if is_in_word == False:
        incorrect_guesses = incorrect_guesses + 1


    if "_" not in "".join(word_in_progress):
        print("you win ! ")

    return incorrect_guesses, " ".join(word_in_progress) 
