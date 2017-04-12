#myPhrase = "The quick brown fox jumps over the lazy dog"
'''
myPhrase = input("enter the string:")

def is_pangram(phrase):
    c = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters = ""
    for char in phrase:
        for letter in alphabet:
            if char == letter and char not in phraseLetters:
                phraseLetters += char
    for char in phraseLetters:
        for letter in alphabet:
            if char == letter:
                c += 1
    if c == 26:
        return True
    else:
        print (phraseLetters, alphabet)
        return False
print (is_pangram(myPhrase))

'''












def panagram(x):
    string1 ="abcdefghijklmnopqrstuvwxyz"
    for i in string1:
        if(i in x):
            continue
        else:
            return False
    return True           
n=input("Enter Any Text:")
if(panagram(n.lower())):
    print("Yes It is a Pangram")
else:

            print("No It is not a Pangram")
