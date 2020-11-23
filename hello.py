# this is a test
name = "Zen"
age = 22
print("my name is", name,"and I'm", age)
# print("my name is " + name+"and Im"+age)

first_name = "Zen"
last_name = "Coder"
age = 27

answer = 'yes'
# F-Strings (Literal String Interpolation)
print(f"My name is {first_name} {last_name} and I'm {age} years old.")
print(f"can this work without a var?")
print(f'{answer}', answer)
print(answer)


# alt way string.format()
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# %-formatting
# % symbol is used to indicate a placeholder
# %s for a string and 
# %d for a number. 
# After the string, a single % separates the string to be interpolated from the values to be inserted into the string, like so:
hw = "Hello %s" % "world"
py = "I love Python %d" % 3
print(hw, py)

# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

print("---------------\n")
myXstring = "hello WOrld!! 1123 #$$ % ..."
allNumString = "43434343"
onlyStrings = "hithere"
print(myXstring.title())
# output:
# "Hello World"
print(myXstring.upper()) # returns a copy of the string with all the characters in uppercase.
print(myXstring.lower()) # returns a copy of the string with all the characters in lowercase.
print(myXstring.count("1")) # returns number of occurrences of substring in string.
print(myXstring.split()) # string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
print(myXstring.find("12")) # string.find(substring): returns the index of the start of the first occurrence of substring within string.
print(allNumString.isalnum()) # string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
print(onlyStrings.isalpha()) # string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# print(myXstring.join(list)) # returns a string that is all strings within our set (in this case a list) concatenated.
print(onlyStrings.endswith('e')) # returns a boolean based upon whether the last characters of string match substring.
