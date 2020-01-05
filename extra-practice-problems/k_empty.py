# 
def twoSumK(a, k):
	a.sort()
	n = len(a)
	l,r, m = 0, n-1, -1
	while l<r:
		if a[l]+a[r] < k:
			m = max(a[l]+a[r], m)
			l+=1
		else:
			r-=1

	return m


print(twoSumK([34, 23, 1, 24, 75, 33, 54, 8],60))
print(twoSumK([10,20,30],15))