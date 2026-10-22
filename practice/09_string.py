#String Basics:
#1. Write a Python program to reverse a string without using slicing.

s1 = input("Enter a string:")
reverse =""

for i in s1:
    reverse = i + reverse
    print("Answer string:",reverse)

# 2. Write a Python program to check if a string is palindrome or not.

string = input("Enter a string:")
reverse ="" 
for char in string:
    reverse = char + reverse
if string==reverse:
    print("palindrome string..")
else:
    print("palindrome not string...")

#3. Write a Python program to count the occurrences of a character in a string.

string = input("Enter string:")
char =input("Enter a character string:")

count=0

for i in string:
    if i == char:
     count += 1

print("Occurrences of a character:",char,"=",count)


#String Manipulation:
#1. Write a Python program to count the number of vowels and consonants in a string.

s1 =input("Enter character:").lower()

vowels=0
consonants=0

for char in s1:
    if char.isalpha():
        if char in "aeiou":
            vowels +=1
        else:
            consonants +=1

print("Enter a vowels",vowels)
print("Enter a consonants",consonants)

#2. Write a Python program to find the frequency of each character in a string (ignore case sensitivity).

str1 = "hello"
l1 = list(str1)
print(l1)
s1 = set(l1)
print(s1)

for i in s1:
    print(i, "=",str1.count(i))

#3. Write a Python program to capitalize the first letter of each word in a sentence.


sentence =input("Enter a sentence:")

resulte = sentence.title()

print("capitalize sentence:",sentence)


#Substring Operations:
#1. Write a Python program to check if one string is a rotation of another.

s1 =input("Enter a First:")
s2 =input("Enter a Second:")

if len(s1)==len(s2) and  s2 in (s1+ s2):
    print("rotation")
else:
    print("another")

#2. Write a Python program to find all occurrences of a substring in a given string.

string =input("Enter the main string:")
substring = input("Enter the substring:")

positions =[]
start = 0


while True:
    index = string.find(substring, start)
    
    if index == -1:
        break
        
    positions.append(index)
    start = index + 1

print("Substring found at positions:", positions)


#3. Write a Python program to remove all leading and trailing whitespace characters from a string.

text = input("Enter a string:")

resulte = text.strip()

print("after remove a string:",resulte)

#String Sorting and Searching:

#1. Write a Python program to sort words in a sentence alphabetically.

sentence = input("Enter a sentence: ")

words = sentence.split()

words.sort()

print("Words in alphabetical order:")

for word in words:
    print(word)

#2. Write a Python program to find the longest word in a sentence.

sentence = input("Enter a sentence: ")

 
words = sentence.split()

 
longest_word = max(words, key=len)

print("Longest word:", longest_word)

#3. Write a Python program to check if a string contains only digits.


text = input("Enter a string: ")

if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")

#Advanced String Handling:

#1. Write a Python program to find the most occurring character in a string.


text = input("Enter a string: ")

max_char = ''
max_count = 0

for char in text:
    count = text.count(char)
    
    if count > max_count:
        max_count = count
        max_char = char

print("Most occurring character:", max_char)
print("Number of occurrences:", max_count)

#2. Write a Python program to check if two strings are anagrams of each other.

str1 = input("Enter first string:")
str2 = input("Enter second string:")

if sorted(str1.lower()) ==sorted(str2.lower()):
    print("string are anagrams..")
else:
    print("the string are not anagrams...")


#3. Write a Python program to find the first non-repeating character in a string.


text = input("Enter a string: ")

for char in text:
    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found.")



#Regular Expressions:
#1. Write a Python program to validate an email address using regular expressions.

