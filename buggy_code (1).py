"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
#correcting the name from deftract to def extract and correcting indentation#
def extract_and_rearrange(string):
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize()
    str_2 = "".join(string[6:13].split('ro'))#
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17]))#added underscore to str3 and "". to the start of the line
    str_4 = "".join(string[21:29].split(string[23:28]))
#added missing quotations to complete the return#
    return str_1 + " " + str_2 + " " + str_3 + " " + str_4

def ultra_extract_and_rearrange(string):#correctd ultra_extrct to ultra_extract
    first_transform = extract_and_rearrange(string)
    return first_transform
#add missing brackets#

print(ultra_extract_and_rearrange("egthb quirock nwoGrb forijmpxv"))

