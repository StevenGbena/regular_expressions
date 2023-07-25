#ASSIGNMENT for find using regex
import re


with open('video.txt')as file:
    read_me_text=file.read()
    print(read_me_text)

user_inputs=input('Search for any text or string :')
find=re.findall(user_inputs,read_me_text)
print(find)
print('There are', len(find) )
if find:
    print('Search found') 
else:
    print('Search not in the string')       


#ASSIGNMENT for replacing using regex
import re

with open('video2.txt')as file:
    replace_me_text=file.read()
    print(replace_me_text)


user_keyword=input('Enter keyword you want to replace :')
user_replace=input('Enter character or string to replace :')
replace=re.sub(user_keyword,user_replace,replace_me_text)
print(replace)  
if replace:
    print('Replace verified')
else:
    print('Replace cannot be verified,replace again')     
