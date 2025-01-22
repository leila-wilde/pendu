import words
from random import randrange

def initiate():
    """
    Selects randomly and returns a word
    within variable list_of_words inside words.py file
    """
    print("Bienvenue au jeu du pendu !")
    list_words = words.list_of_words
    nbWords = len(list_words)
    play_word = list_words[randrange(nbWords)]
    return play_word


def guessing(play_word):
    # we keep record of letters already played so we display this in order to help players
    # list of letters used by player. Initially empty
    list_of_letters = []
    len_word = len(play_word)

    # we use a list to store letters that are part of the word to guess
    # initially, this is a list of "_" character
    tab_play_word = ["_"] * len_word
    print("".join(tab_play_word))

    # integer to count number of false letters entered
    # if a false letter has already have been input, counter does not increase
    counter = 0
    finished = False

    # games stops either after 7 errors, either when correct word is guessed
    while not finished and counter < 7 :


        erreur = True

        print("Lettres déjà jouées :")
        print(list_of_letters)
        letter = input_letter()
        for id_letter in range(len_word) :
            if play_word[id_letter] == letter.lower() :

                # boolean value. there is an error if letter is not part of the word to guess
                erreur = False

                # uppercase & lowercase are handled equally
                if tab_play_word[id_letter] == "_" :
                    tab_play_word[id_letter] = letter.lower()
        if letter not in list_of_letters :
            list_of_letters.append(letter)

            # error counter is incremented only if a bad letter hasn't been used already
            if erreur :
                counter += 1
        print(f"compteur : {counter}")
        print("".join(tab_play_word))

        if "_" not in "".join(tab_play_word):
            print("gagné")
            finished = True
    
    if counter == 8 :
        print("Perdu !")
        print(f"Le mot à trouver était : {play_word}")

def input_letter():
    """
    User cannot enter an input different from a single letter.
    """
    letter = ""
    while len(letter) != 1 or not letter.isalpha() :
        try :
            print("veuillez entrer une lettre :")
            letter=input()
        except TypeError :
            print("il faut entrer une lettre")
        except ValueError :
            print("il faut entrer une lettre")
    return letter


# créér un fichier score

def main():
    play_word = initiate()
    guessing(play_word)

main()