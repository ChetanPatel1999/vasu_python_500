#Write a program to find the smalest word in a string.
s="hello my name is chetan patel" 
words=s.split()
smallest=words[0]
for word in words:
    if len(smallest)>len(word):
        smallest=word
print(smallest)        