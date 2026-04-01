# Write a program to make a list of word from given string.
text="hello this is     book book write by sahaj and book read by me"
l1=[]
word=""
for char in text:
    if char !=" ":
        word+=char
    else:
      if word !="" : 
        l1.append(word)
        word=""   
l1.append(word)         

print(l1)  
   

