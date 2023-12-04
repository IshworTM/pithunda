import random
import time
list1 = []
# list2 = []
def fopen():
    with open('words.txt', 'r') as file:
        for line in file:
            splitted = line.strip()
            if len(splitted) == 5 and splitted.isalpha():
                list1.append(splitted)

def main():
    fopen()
    game()

def instruction():
    print("\nWelcome to a CLI based word guessing game.\n")
    time.sleep(.98)
    print("Instructions:")
    print("1. You need to guess a 5 letter word.")
    time.sleep(1/.95)
    print("2. You will be given 5 chances to correctly guess the word.")
    time.sleep(1/.95)
    print("3. If your guess has a letter in its correct position, it will be marked with (+).")
    time.sleep(1/.95)
    print("4. If your guess has a letter in an incorrect position, it will be marked with (*).")
    time.sleep(1/.95)
    print("5. If your guess and the correct word doesn't have any letter in common, it will be marked with (-).")
    time.sleep(1/2)
    print("And finally if you correctly guess the word you'll be the winner!!🎉\n")

def game():
    instruction()
    word = random.choice(list1).upper()
    chances = 5
    while chances > 0:
        print(f"Attempt: {6 - chances}.")
        user_input = input("Enter a 5 letter word to start the game:\n>> ").upper()
        if len(user_input) != 5 or not user_input.isalpha():
            print("Unknown error, re-starting the program.\n")
            continue
        result = check(user_input, word)
        print(result)

        chances -= 1
    if chances == 0 :
        print(f"Sorry, you ran out of chances :((\nThe correct word was {word}.")
        exit()

def check(user_input,word):
    result = []
    if user_input == word:
        print(f"Congrats! You did it, '{user_input}' was the correct word🎉🎉.")
        exit()
    else:
        for char in range(5):
            if user_input[char] == word[char]:
                result.append(user_input[char] + "+")
            elif user_input[char] in word:
                result.append(user_input[char] + "*")
            else:
                result.append(user_input[char] + "-")
        return result
    
if __name__ == "__main__":
    main()

