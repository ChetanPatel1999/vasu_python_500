#Write a program to find the largest word in a string.
s="hello my name is chetan patel" 
words=s.split()
largest=""
for word in words:
    if len(largest)<len(word):
        largest=word
print(largest)        