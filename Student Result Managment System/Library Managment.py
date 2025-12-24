import pandas as pd
import numpy as np
n=int(input("Enter the no. of books for storing the books in the library : "))
list = []
for i in range(n):
    m=input(f"Enter the name of the book {i+1} for storing in the storage in the library : ")
    list.append(m)
print("")    
print("The list of your stored books with the allocated desk number is given down as follows : ")    
lst = np.array(list) 
index_series = pd.Series(list,index=range(1,n+1))
print(index_series)
a=input("Now enter the name of the book u wanna search in the library to locate where it is : ")
for i in range(len(list)):
   if list[i] == a:
    print("Book found at desk {}".format(i+1))
    break
else:
     print("Book not found in the library.")