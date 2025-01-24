# j'ai codé cette fonction pour faire fonctionner le pendu
# elle prend en paramètre le mot à deviner
# et les lettres déjà entrées par le joueur
# elle va calculer le nombre d'erreurs
# on peut lui faire appeler la fonction qui affiche le pendu
# et lui entrer en paramètre le nombre d'erreurs

# en gros on la lance et on récupère 2 valeurs à la fois
# dans 2 variables différentes
# word_to_display, number_of_errors

# elle renvoie le mot formé de lettres et de "_"
# donc on peut lancer la fonction qu'on veut
# pour afficher le mot


# on peut se servir de cette fonction pour terminer la boucle while True  :

    # soit : il y a trop d'erreurs
    # on gère ça avec number_of_errors
    # (nombre qu'on renvoie et qu'on stocke dans la variable number_of_errors)


# soit : quand on a deviné le mot

# ligne 54
#    if "_" not in word_to_display:
#        termine = True


def play_hangman(secret_word, played_letters):

    counter = 0

    # calculer nombre erreurs
    for l in played_letters:
        if l not in secret_word :
            counter += 1

    # afficher le pendu
    display_hangman(counter)

    # créér le mot
    word_to_display = ""
    for letter in secret_word :
        if letter in played_letters:
            word_to_display += letter
        else :
            word_to_display += "_"
    print(word_to_display)

    # on termine parce qu'on a deviné le mot
    # et on sort de la boucle
    if "_" not in word_to_display:
        termine = True

    return (counter, word_to_display)

# exemple de fonctionnement de la fonction
secret_word = "caramel"
played_letters = ["a", "b", "c", "d"]

word_to_display, number_of_errors = play_hangman(secret_word, played_letters)
