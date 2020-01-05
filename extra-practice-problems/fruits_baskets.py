# [1,2,1] - 3 - 1,2,1
# [0,1,2,2] - 3 - 1,2,2
# [1,2,3,2,2] - 4 - 2,3,2,2
# [3,3,3,1,2,1,1,2,3,3,4] - 5 - 1,2,1,1,2

# we have to make a window of size 2 at the very max
# def fruits_into_baskets(fruits):
# 	n = len(fruits)
# 	d = {}
# 	for i in range(n):


# 		b = i
# 		while len(d)<=2:
# 			d.put(d.get(fruits[i], 1) + 1)
# 			i+=1


# fruits_into_baskets([0,1,2,2])

def fruits(f):
	a = 0
	j=0
	n = len(f)
	d = {}
	for i in range(n):
		if f[i] not in d: d[f[i]]=1
		else: d[f[i]]+=1
		# print(d)
		while len(d) >= 3:
			d[f[j]] -=1
			if d[f[j]] == 0:
				del d[f[j]]
			j+=1

		a = max(a, i-j+1)
	return a

a = fruits([1,2,1])
b = fruits([0,1,2,2])
c = fruits([1,2,3,2,2])
print(a,b,c)