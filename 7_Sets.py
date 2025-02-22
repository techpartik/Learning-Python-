# cities1={"tokyo","delhi","mumbai","bihar","dubai"}
# cities2={"banglaur","singapur","bihar","tokyo","sudia"}
# cities3=cities1.union(cities2)
# print(cities3)

# cities1={"tokyo","delhi","mumbai","bihar","dubai"}
# cities2={"banglaur","singapur","bihar","tokyo","sudia"}
# cities3=cities1.intersection(cities2)
# print(cities3)

# cities1={"tokyo","delhi","mumbai","bihar","dubai"}
# cities2={"banglaur","singapur","bihar","tokyo","sudia"}
# cities3=cities1.symmetric_difference(cities2)
# print(cities3)

# cities1={"tokyo","delhi","mumbai","bihar","dubai"}
# cities2={"banglaur","singapur","bihar","tokyo","sudia"}
# cities3=cities1.difference(cities2)
# print(cities3)

# cities1={"tokyo","delhi","mumbai","bihar","dubai"}
# cities2={"banglaur","singapur","bihar","tokyo","sudia"}
# print(cities1.difference(cities2))

# Create a set of even numbers from 1 to 20. 
# even_number=int(input("enter the number"))
# for even_number in range(0,21):
#     if even_number % 2 == 0:
#         print("the even number is",even_number)
# else:
#     print("odd number")


# s1 = {1,4,5,10,2,3,0,6,7,8,9,1}   
# s2 = sorted(s1)
# print(s2)

# # 1. Generate a set of squares of numbers from 1 to 10.
# num={1,2,3,4,5,6,7,8,9,10}
# for i in range(1,11):
#     squar=i
#     print(squar)

# Generate a set of characters from a string. 

# s1={0}
# string="shahawazkhan"
# for i in string:
#     s1.add(i)
# s1.remove(0)
# print(s1)

#  Generate a set of squares of numbers from 1 to 10.
# square= {i**2 for i in range(1,11)}
# print(square)

# Create a set of lowercase letters. 
# lowercase_letters = {chr(i) for i in range(97, 123)}
# print(lowercase_letters)

# Generate a set of uppercase letters
# capital_letters = {chr(i) for i in range(65, 90)}
# print(capital_letters)



# s1=int (input("enter the number: "))
# for i in range(s1):
#     if s1%2==0:
#         sqare={s1**2}
# print(sqare,"the number of squar")

# cube={s1**3}
# print(cube,"cube of number is")

# cube=set()
# for i in range(1,101):
#     cube.add(i**3)
# print(cube)
    

# words={"ser","met","wet","pet"}

# sorted_words=set()

# for word in words:
#     sorted_chars = sorted(words)
#     sorted_word="".join(sorted_chars)
#     sorted_words.add(sorted_word)
# print(sorted_words)

# words = {"apple", "banana", "cherry", "date", "grape"}

# # Initialize an empty set for sorted words
# sorted_words = set()

# # Process each word
# for word in words:
#     sorted_chars = sorted(word)          # Sort the characters of the word
#     sorted_word = "".join(sorted_chars)  # Join the sorted characters
#     sorted_words.add(sorted_word)        # Add the sorted word to the set

# # Print the final set
# print(sorted_words)