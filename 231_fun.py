def largestValue(*data): #(12,56)
    max=data[0]
    for num in data:
        if max<num:
            max=num
    return max         



print(largestValue(12,56))
print(largestValue(600,12,56))
print(largestValue(6,12,56,23))