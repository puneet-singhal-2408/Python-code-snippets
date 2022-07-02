string = "ABC"
stuart_score = 0
kevin_score = 0
for i in range(len(string)):
	if string[i] in "AIEOU":
		kevin_score += (len(string)-i) 
	else:
		stuart_score += (len(string)-i)
if kevin_score>stuart_score:
	print("Kevin " + str(kevin_score))
elif kevin_score<stuart_score:
	print("Stuart " + str(stuart_score))
else:
	print("Draw")

# Hint: score will be length of string minus the index value where the vowel or constant occur as all the substring will be from the remaining string"
# Example: if string is BANANA then for S[i] where i = 0.  we will have sub strings as B, BA, BAN, BANA, BANAN, BANANA.
#the no string is 6 , so when we give 1 point for each substring and add it , that is actually equal to len. of string.
# similarly when i = 2 , we will have substrings N, NA, NAN, NANA, so we need to add 4 to score , however if we see that is also
# Length of sting minus the index value.
# instead of focusing on what are the possible substrings we can determine the score simpliy.
