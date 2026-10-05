word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

word1 = word1.lower()
word2 = word2.lower()

if sorted(word1) == sorted(word2):
    print("Words are Anagram")
else:
    print("Words are not Anagram")