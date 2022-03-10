#mystring = "hello"
#i = 0
#f = 0

#if mystring == "hello":
 #   print("String: %s" % mystring)

# list = [2,3,5]
# list.append(10)
# #print(list) 

# print(list[3])
# for x in list:
#     #print(x)
#     print("This is %d" %x)


# numbers = []
# strings = []
# names = ["John", "Eric", "Jessica"]

# # write your code here
# second_name = names[1]
# # numbers.append(1)
# # numbers.append(2)
# # numbers.append(3)

# numbers.extend([1,2,3]) # Extenstion in single line
# numbers.extend(range(4,9)) #Put a range 
# strings.append("hello")
# strings.append("world")

# strings.extend(["Myself","Neetu"])

# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)


# remainder = 11 % 3
# print(remainder)
# print(8**2) #square
# print(7**3) #cube
# print("I am in class 12.\n" * 2)

# x = object()
# l = [x]*10
# print(len(l)) #length of list


# val = input("Enter your age:")
# print(val)
str = "hello world!"
# print(str.index("w"))  #location of w
# print(str[3:7])   #This prints a slice of the string, starting at index 3, and ending at index 6.
# print(str[3:7:2]) #This skips 1(2-1) character
# print(str[3:7:1]) #This skips 0(1-1) same as print(str[3:7])
print(str[:-3])
print(str[::-1]) #For reverse of the string
print(str.upper())
print(str.lower())
#To check wheteher string start with of end with
print(str.startswith("My")) 
print(str.endswith("world!"))
print(str.split(" ")) # split string in words
print(str[1::2]) #Print odd 
print(str[1:12:2]) #This also work
print(str[0::2]) #print even
