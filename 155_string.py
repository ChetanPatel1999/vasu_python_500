#Write a program to display each word length in string.
s="hello my name is chetan patel" 
words=s.split()
for word in words:
    print(f"{word} = {len(word)}")        