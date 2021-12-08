word_to_count={}
text = input("Text :")
word = text.split()
for i in word:
    many_words = word_to_count.get(i,0)
    word_to_count[i] = many_words +1

word = list(word_to_count.keys())
word.sort()

max_length = max((len(i) for i in word))
for i in word:
    print(f"{i:{max_length}} : {word_to_count[i]}")