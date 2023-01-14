# Makes alternative letters or words upper or lowecase.

test_str_chara = "Hello World"
test_str_word = "I am learning to code."

test_list_word = test_str_word.split(' ')

# New upper and lower case characters will be added to these strings
alt_str_chara = ""
alt_list_word = ""

# For creating upper and lower case characters based on if the index of a character is an odd or even number
for i in range (len(test_str_chara)):
    if i % 2 == 0:
        alt_str_chara += test_str_chara[i].upper()
    else:
        alt_str_chara += test_str_chara[i].lower()

print ("Alternative letters test: " + alt_str_chara)

# For creating upper and lower case words based on if the index of a word in the list is an odd or even number
for i in range (len(test_list_word)):
    if i % 2 != 0:
        alt_list_word += test_list_word[i].upper()
    else:
        alt_list_word += test_list_word[i].lower()

print ("Alternative word test: " + ' '.join(alt_list_word))