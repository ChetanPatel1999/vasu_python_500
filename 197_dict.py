# Write a program to count frequency of each word in a sentence using dictionary. 
text="hello this is book book write by sahaj and book read by me"
l1=text.split()
d1={}
for word  in l1:
   if word not in d1:
      d1[word]=1
   else:
      d1[word]+=1   

print(d1)      
   

