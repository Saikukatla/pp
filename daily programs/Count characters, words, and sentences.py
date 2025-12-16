n = input("enter a string:")
char_count = 0
word_count = 0
sentence_count = 0
for char in n:
    char_count += 1
    if char == " ":
        word_count += 1
        if char == [".","!","?"]:
            sentence_count += 1
word_count += 1
print("no of characters:", char_count)
print("no of words:", word_count)
print("no of sentences:",sentence_count)

