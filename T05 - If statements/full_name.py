# Asks user for name and checks if the input is valid based on character and word count.

name_full = input("Full name please: ")
name_list = name_full.split(' ')
name_chara_len = len(name_full)
name_num_len = len(name_list)

print("You have entered " + str(name_num_len) + " names, of " + str(name_chara_len) + " character length.")

if name_chara_len < 1:
    print("Please enter your full name.")
elif name_num_len < 2:
    print("Please make sure you have entered your name and surname.")
elif name_chara_len > 25:
    print("Please make sure you have only entered your full name.")
else:
    print("Thank you for entering your name!")