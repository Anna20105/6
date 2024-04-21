def is_palindrom(word):
    return word == word[ :: -1]

word = input("madam: ")

if is_palindrom(word):
    print("madam.")
else:
    print("good.")