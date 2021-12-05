def split_word_to_array(unsplitted_word):
    """
    This method splits a word into an array and will convert the letters to uppercase
    @:parameter word
    @:return splitted_word
    """
    splitted_word = []
    for i in unsplitted_word:
        splitted_word.append(i.upper())
    return splitted_word


def show_word_underscores(splitted_word):
    """
    This method will return a string with underscores of the length of the given list
    @:parameter splitted_word
    @:return list
    """
    underscore = []
    for i in range(len(splitted_word)):
        underscore.append('_')
    return underscore


def check_guessed_char(guessed_char):
    """
    Check if guessed char is in the word
    :param guessed_char: list
    :return: void
    """
    for i in range(len(word_array)):
        if word_array[i] == guessed_char.upper():
            underscored_list[i] = guessed_char.upper()


def char_allready_guessed(guessed_char):
    """
    Check if typed char has allready been used
    :param guessed_char: char
    :return: boolean
    """
    if guessed_char in list_of_guessed_chars:
        print(f'Du hast bereits das {guessed_char} verwendet')
        return True
    else:
        list_of_guessed_chars.append(guessed_char)
        return False


def all_guessed():
    """
    Check if all chars has been guessed by the user
    :return: void
    """
    if '_' in underscored_list:
        return False
    else:
        return True


print('Willkommen zu Hangman')

# Guessed word as string
word = str(input('Gebe bitte dein Wort ein: '))

# Guessed word as list and every char has it own index
word_array = split_word_to_array(word)

word_not_gussed = True

underscored_list = show_word_underscores(word_array)

list_of_guessed_chars = []

while word_not_gussed:
    if all_guessed():
        print('Du hast alle Buchstaben erraten :)')
        print(f'Das Wort war: {word}')
        break
    current_guesed_char = input('Gib einen Buchstaben ein: ')

    if current_guesed_char == 'beenden':
        print('Hangman wurde abgebrochen')
        break

    if not char_allready_guessed(current_guesed_char):
        check_guessed_char(current_guesed_char)

        for i in range(len(underscored_list)):
            print(underscored_list[i], end=' ')
        print('\n')