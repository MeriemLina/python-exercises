def is_palindrome(word):
    if len(word)==1:
        return True

    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return  False
    return True

text = input("enter a word")
if is_palindrome(text):
    print(f"{text} is a palindrome!")
else:
    print(f"{text} is not a palindrom :(")