dic={"name":"shahnawaz khan","city":"patna","age":19, "gender":"male"}
# print(dic["name"])
# print(dic.get("city"))
# dic1={'name':'sahil','from':'sabalpur','age':'18'}
# dic.update({'city':'newyork'})
# print(dic)
# dic.update(dic1)
# # print(dic)
# # dic.pop("age")
# # print(dic)

# # dic.popitem()
# # print(dic)

# # print(dic['age'])

# # for key in dic.keys():
#     # print(dic[key])

# # 1. Write a Python program to generate a dictionary where the keys are
# # numbers between 1 and 5 and values are their squares.
# dic={}  
# # key=[1,2,3,4,5]
# key=('enter th number 1 to 5')
# for i in range(1,5):
#     dic[i]=i**2
# # dic.update({key:value})
# print(dic)

# # 2. Write a Python program to clear all elements from a dictionary.
# dic1={0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# dic1.clear()
# print(dic1)

# 3. Write a Python program to create a dictionary of words and their lengths from a given sentence.
# key=input('enter the words: ')
# # d1={}
# # for word in key.split():
# #     d1[word]=len(word)
# # print(d1)


# # # 4. Write a Python program to create a dictionary with numbers as keys and their cubes as values.
# dic={}  
# # key=[1,2,3,4,5]
# key=('enter th number 1 to 5')
# for i in range(1,5):
#     dic[i]=i**3
# # dic.update({key:value})
# print(dic)

# # 5. Write a Python program to count the frequency of each character in a
# # given string.
# key=input('enter the words: ')
# d1={}
# for letter in key.split():
#     d1[letter]=len(letter)
# print(d1)


# Write a Python program to count the frequency of each character in a 
# given string.
# d1=['a','b','c','d','a','b','c','d','d' ]
# d2={}                                                                                                                                                                                                                                                                                                  

# for i in d1:
#     if i not in d2:
#         d2[i]=d1.count(i)
# for key,value  in d2.items():
#     print(key,value)

# 6. Write a Python program to find the frequency of each word in a given 
# sentence.

d1=['apple','ball','cat','dog','apple','ball','cat','dog','dog' ]
d2={}                                                                                                                                                                                                                                                                                                  

for i in d1:
    if i not in d2:
        d2[i]=d1.count(i)
for key,value in d2.items():
    print(key,value)