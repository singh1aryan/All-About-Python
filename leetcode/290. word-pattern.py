def pattern(pattern, s):
	b= {}
	s_parts = s.split(' ')
	# if len(st) != len(pattern):
	# 	return False
	p_dict = dict([(c,None) for c in pattern])
	print(p_dict)
	for i, p in enumerate(pattern):
		word = s_parts[i]
		if p_dict[p] == None:
			p_dict[p] = word
		else:
			if not(p_dict[p] == word):
				return False
	print(p_dict)
	# additional check on patterns' mutual exclusiveness
	val_set = set(p_dict.values())
	if not (len(val_set) == len(p_dict)):
		return False

	# there it is
	return True



patte = "abba", 
str = "dog cat cat dog"
pattern(patte, str)
