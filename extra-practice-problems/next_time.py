# 01:59 - 05:00
# 18:34 - 18:38
# 12:59 - 15:11
# 12:54 - 12:55
# 18:34 - 
# 23:59 - 22:22

def next_time(t):
	a,b,c,d = int(t[0]), int(t[1]), int(t[3]), int(t[4])
	min_t = min(a,b,c,d)
	max_t = max(a,b,c,d)

	l = [a,b,c,d]
	t = [a,b,c,d]
	t.sort()
	d = {}
	for i in range(len(t)-1):
		d[t[i]] = t[i+1]
	d[t[len(t)-1]] = -1

	# print(d, l)


	for i in range(len(t), -1, -1):
		if i==3:
			# print(d[l[i]])
			if d[l[i]] != -1 and d[l[i]]<=9: 
				l[i] = d[l[i]]
				return l

			else: l[i] = min_t
		if i==2: 
			if d[l[i]] != -1 and d[l[i]]<6: 
				l[i] = d[l[i]]
				return l
			else: l[i] = min_t

		if i==1:
			if l[0]==0 or l[0]==1:
				if d[l[i]] != -1 and d[l[i]]<=9: 
					l[i] = d[l[i]]
					return l
				else: l[i] = min_t
			else:
				if d[l[i]] != -1 and d[l[i]]<=4: 
					l[i] = d[l[i]]
					return l
				else: l[i] = min_t


		if i==0:
			if d[l[i]] != -1 and d[l[i]]<=2: 
				l[i] = d[l[i]]
				return l
			else: l[i] = min_t

	return l

print(next_time("18:34"))
print(next_time("12:59"))
print(next_time("09:23"))
print(next_time("01:59"))
print(next_time("12:45"))
print(next_time("10:59"))
print(next_time("12:54"))
print(next_time("23:59"))