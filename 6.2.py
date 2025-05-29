sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_words = [word[::-1] for word in words]

new_sentence = " ".join(reversed_words)
print("Reversed words sentence:", new_sentence)
