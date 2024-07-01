import pandas as pd

x = pd.Series([10,88,15,25,1,2,3])
print(x,type(x),x.axes,x.size,x.ndim,x.values,x.head(3),x.tail(3))
x= pd.Series([10,20,40,80,10,30,50],index= ["a","b","c","d","e","f","g"])
print(x)