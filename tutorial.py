import numpy as np

#commun function in numpy

"""a = np.array([1,2 ,3])

print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a[1])
sum = a * np.array([5, 3, 4]) work also with + - /
print(sum)"""

# list vs array

l = [1, 2, 3 ,4 ,5]
arr = np.array([1, 2 ,3 ,4, 5])
l *= 2
arr *= 2
arr = np.sqrt(arr)
print(l)
print(arr)

#dot product



#list   
l1 = [1,2,3]
l2 = [3,4,5]

dot = 0

for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

#array
arr1 = np.array(l1)
arr2 = np.array(l2)

dot = np.dot(arr1, arr2)
print(dot)

sum1 = arr1 * arr2 # [1, 2 ,3] * [3, 4 ,5] = [3, 8 ,15]
dot = np.sum(sum1)
print(dot)
dot = (arr1 * arr2).sum() #same as sum(arr1 * arr2)

print(dot)

dot = arr1 @ arr2
print(dot)

x = np.random.randn(5)
print(x)

#note: array is way faster than list 


#multidimention array

arr = np.array([[1 ,2,3], [3,4,5]])
print(arr)
print(arr.shape)
print(arr[1, 2])
print(arr[:, 1]) # all elemet in row1
print(arr[1, :]) # all elemet in column1
print(arr.T)

sqarr = np.array([[2,3], [4,5]])
print(np.linalg.inv(sqarr))
print(np.linalg.det(sqarr))

print(np.diag(sqarr))

c = np.diag(sqarr)
print(np.diag(c))

b = sqarr[1, :]
print(b)

a = np.array([[1, 2 ,3], [4, 5 ,6]])

bool_idx = a%2 == 0

print(bool_idx)
print(a[bool_idx]) # or a[a%2 == 0]
b = np.where(a % 2 == 0, a, -1)
print(b)
w = np.array([12, 54 ,65 ,84 ,16 ,31 ,51])

q = [1 ,3 ,5]
print(w[q]) #fancing indexing 

even = np.argwhere(a%2 == 0).flatten() # flatten make 1dim array
print(w[even])

print(a.flatten())

a = np.arange(1, 7)
print(a)
print(a.shape)
b = a.reshape(2, 3)
print(b, b.shape)
b = a[np.newaxis, :] 
print(b, b.shape)
print(a[0:3, np.newaxis])
p = np.concatenate((a, [1])) # adding two array with same dimension
print(p)
a1 = np.array([[1,2], [3,4]])
a2 = np.array([[5,6], [7,8]])
print(np.concatenate((a1,  a2), axis = None))    
print(np.hstack((a1,a2)))
print(np.vstack((a1,a2)))

print(a1.sum(axis = 1 ))
print(a1.mean())