#Diego Espinola
#01.04.20
# This porgram will use a recursive method to check if a world is palindrome or not.

def is_word_palindrome(word):
    word = word.strip()
    word = word.lower()

    if len(word)<1:
        return True

    elif word[0] != word[-1]:
        return False

    else:
        return is_word_palindrome(word[1:-1])




word = str(input("Type a word to check if it is palindrome \n>"))
is_word_palindrome(word)
if is_word_palindrome(word) == True:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")
while is_word_palindrome(word) == True or is_word_palindrome(word) == False:
    word = str(input("Type a word to check if it is palindrome \n>"))
    is_word_palindrome(word)
    if is_word_palindrome(word) == True:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not palindrome")






