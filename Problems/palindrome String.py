letter = input("Enetr your word : ")
rvs_letter = letter[::-1]
print(letter)
print(rvs_letter)
if letter.lower() == rvs_letter.lower():
    print("palindrome")
else:
    print("not palindrome")
