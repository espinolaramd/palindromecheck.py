#Diego Espinola
#01.04.20
# This porgram will use a recursive method to check if a world is palindrome or not.

def is_word_palindrome(n):
    word.strip()
    word.lower()


    if len(n)<1:
        return print("True")

    elif n[0] != n[-1]:
        return print("False")

    else:
        return is_word_palindrome(n[1:-1])

word = str(input("Type your word"))
is_word_palindrome(word)



