def interleaving(s1,s2,curr_string,result):
	if len(s1) == 0:
		result.append( curr_string+s2 )
		return
	if len(s2) == 0:
		result.append( curr_string+s1 )
		return

	interleaving(s1[1:],s2,curr_string+s1[0],result)
	interleaving(s1,s2[1:],curr_string+s2[0],result)

if __name__ == "__main__":
	
	string1 = "ab"
	string2 = "wx"
	result = []
	interleaving(string1, string2, "", result)
	print( result )