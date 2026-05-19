import pandas as pd
mydataset = {
    
 'cars': ["BMW", "Ford", "Volvo"],
 'passings':[3,7,2] 
}

myvar = pd.DataFrame(mydataset)
print (myvar)

print(myvar.iloc[1])

print(myvar["cars"])

a = [1, 7, 2]

myvar2 = pd.Series(a, index = ["x", "y", "z"])

print(myvar2["z"])