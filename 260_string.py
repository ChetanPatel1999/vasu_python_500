# wap to skip  consonent using continue stmnt

text="programming"
for i in text:
    if i not in "aeiou":
        continue
    print(i)