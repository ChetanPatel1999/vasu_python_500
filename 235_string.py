s="i am enjoing coding and learning while runing and swiming"

words= s.split()
ing_word=[]
for word in words:
    if word.endswith("ing"):
        ing_word.append(word)

print(ing_word)

