import numpy as np

# arr = np.array([12,34,56,77,9])
# arr= np.zeros(5)
# arr[1]=90

# arr= np.ones(5)

# arr=np.array([12,128,56,67,78],dtype=np.int8)

# print(arr)
# print(arr.size)
# print(arr.dtype)

rainfall_in_mm = np.array([50,70,80,20,100,60,40])

print(rainfall_in_mm)
# print(rainfall_in_mm>50)

print( "maximum rain fall : ",np.max(rainfall_in_mm))
print( "maximum rain fall : ",np.min(rainfall_in_mm))
print( "average rain fall : ",np.mean(rainfall_in_mm))
print( "above then 50 rain fall days: ",np.sum(rainfall_in_mm>50))
print( "decending order : ",np.sort(rainfall_in_mm)[::-1])


