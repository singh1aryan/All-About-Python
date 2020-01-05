import collections
def minimum_window(s, t):
	need = collections.Counter(t)
	l,r,i,j, missing = 0,0,0,0,len(t)

	while r<len(s):
		# print(need)
		if need[s[r]]>0: 
			missing -=1
		need[s[r]] -=1
		r+=1

		while missing == 0:
			if j==0 or r-l < j-i:
				print(s[i:j])
				i,j = l,r
			need[s[l]] += 1
			if need[s[l]]>0: 
				missing+=1
			l+=1
	return s[i:j]

# a = minimum_window("acbdnssaracbn", "abn")
# print(a)

import collections
def groupThePeople(groupSizes):
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)

       	# print(count)
        # return [l[i:i + s]for s, l in count.items() for i in range(0, len(l), s)]
        b = []
        for s, l in count.items():
        	# print(s, l)
        	for i in range(0, len(l), s):
        		b.append(l[i:i+s])
        # print(b)
        return b

a = groupThePeople([3,3,3,3,3,1,3])
print(a)