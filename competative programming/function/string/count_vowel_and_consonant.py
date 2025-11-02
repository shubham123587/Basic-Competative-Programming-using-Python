str=input("enter the string")
vowel_count=0
consonant_count=0

for ch in range(len(str)):
    if ch in ('a','e','i','o','u','A','E','I','O','U'):
        vowel_count+=1
    else:
        consonant_count+=1
print(vowel_count)
print(consonant_count)            
    

