str_manip = input("Write a sentence about your favourite game!")

print(len(str_manip))   #string length

#turn all occurences of the last letter into @
last_letter = (str_manip[-1])
str_manip_replace = str_manip.replace(last_letter, "@")
print(str_manip_replace)

#print last 3 letters of sentence backwards
test_length = (len(str_manip)) - 4
print(str_manip[:test_length:-1])

#made up word using letters in specific positions of the sentence
print(str_manip[0] + str_manip[1] + str_manip[2] + str_manip[-2] + str_manip[-1])

#every word on a newline
str_manip_newline = str_manip.replace(" ", "\n")
print(str_manip_newline)