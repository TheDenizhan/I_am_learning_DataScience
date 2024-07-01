import numpy as np

#matrix çarpımları daha kolaydır
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
print(a*b)
c = np.array([4.2,5.6,7,6,1,8])
print(c,type(c))
d = np.array([4.2,5.6,7,6,1,8], dtype=int)
print(d,type(d))

e = np.zeros(10,dtype=int)
f = np.ones((3,5),dtype=float)
g = np.full((5,5),7,dtype=int)
print(e,'\n',f,'\n',g)
x = np.arange(0,31,3)
print(x)
x2 = np.linspace(0,1,10)
print(x2)
x3 = np.random.normal(10,4,(3,4))
print(x3)
x4 = np.random.randint(0,10,(3,3))
print(x4)
print(x4.ndim,x4.dtype,x4.size,x4.shape)
x4.reshape((1,9))
print(x4)
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.concatenate([x,y])
print(z)
z = np.concatenate([[x,y]])
print(z)
z = np.concatenate([z,z], axis=1)
print(z)
x = np.array([1,2,3,99,99,3,2,1])
y = np.split(x,[3,5])
print(y)
a,b,c = np.split(x,[3,5])
print(b)
x = np.arange(16).reshape(4,4)
print(x)
y1,y2 = np.vsplit(x,[2])
print(y1,y2)
y = np.hsplit(x,[2])
print(y)
x = np.array([1,8,3,6,4,7,2,1,6])
y = np.sort(x)
print(y)