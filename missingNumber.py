def find_missing(lst_1, lst_2):
	if not lst_1 and not lst_2
		return 0
	if not set(lst_1) ^ set(lst_2)
		return 0
	else:
		return list(set(lst_1) ^ set (lst_2))[0]