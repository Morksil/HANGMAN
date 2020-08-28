import random
print("H A N G M A N")
list_of_words = ['python', 'java', 'kotlin', 'javascript']

while True:
    print('Type "play" to play the game, "exit" to quit:')
    choice = input()
    if choice == 'play':
        correct_word = random.choice(list_of_words)
        hidden_word = "-" * len(correct_word)
        index_of_letter = 0
        word = hidden_word
        correct_letters = []
        number_of_tries = 0
        typed_letters = []

        while True:
            print()
            print(word)
            letter = input(f'Input a letter: ')
            count = 0
            if letter in typed_letters:
                print("You already typed this letter")
                continue
            if len(letter) != 1:
                print("You should input a single letter")
                continue
            if letter < 'a' or letter > 'z':
                print("It is not an ASCII lowercase letter")
            else:
                typed_letters.append(letter)
                if letter in correct_word:
                    if letter not in correct_letters:
                        correct_letters.append(letter)
                        for litera in correct_word:
                            if letter == litera:
                                if count != len(correct_word) - 1:
                                    word = word[:count] + letter + word[count + 1:]
                                else:
                                    word = word[:count] + letter
                                count += 1
                            else:
                                count += 1
                    else:
                        print("You already typed this letter")
                        count += 1
                else:
                    print("No such letter in the word")
                    number_of_tries += 1
            if number_of_tries >= 8:
                break
            if word == correct_word:
                break

        if correct_word == word:
            print(word)
            print("You quessed the word!")
            print("You survived!")
        else:
            print("You are hanged!")
    elif choice == "exit":
        break
    else:
        continue
