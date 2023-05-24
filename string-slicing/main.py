### slicing
# string[start:end:step]
# start: inclusive
# end: exclusive
# step: optional, default is 1

string = "a brown fox jumped over a lazy dog"
print(string[2:5]) # start at index 2, end at index 5
print(string[2:]) # start at index 2, end at the end of the string
print(string[:5]) # start at the beginning of the string, end at index 5

print(string[::2]) # start at the beginning of the string, end at the end of the string, step 2
print(string[::-1]) # start at the end of the string, end at the beginning of the string, step -1

print(string[-1]) # start at the end of the string, end at the end of the string, step 1

print(string[-1:-5:-1]) # start at the end of the string, end at index -5, step -1
print(string[-1:-5:1]) # start at the end of the string, end at index -5, step 1
print(string[-5:-1:-1]) # start at index -5, end at index -1, step -1
print(string[-5:-1:1]) # start at index -5, end at index -1, step 1

print(string[-1::-1]) # start at the end of the string, end at the beginning of the string, step -1
print(string[-1:0:-1]) # start at the end of the string, end at index 0, step -1
print(string[-1:0:1]) # start at the end of the string, end at index 0, step 1

name = "John Doe"
fName = name[:4]
lName = name[5:]
print(name)
print(fName)
print(lName)

reversedName = name[::-1]
print(reversedName)

website = "http://google.com"
slice = slice(7, -4)
print(website[slice])

website2 = "http://wikipedia.com"
print(website2[slice])