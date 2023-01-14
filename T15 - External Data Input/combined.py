# Create a text file called numbers1.txt that contains Integers which are sorted from smallest to largest.
# Create another text file called numbers2.txt which also contains Integers that are sorted from smallest to largest.
# Write the numbers from both files to a third file called all_numbers.txt .
# All the numbers in all_numbers.txt should be sorted from smallest to largest.

ofile = open('numbers1.txt', 'w')  # Create text file, 'w' overwrites text file if the file already exists.
ofile.write("7 32 50 79 91")  # Write integers
ofile.close()  # Close the text file

ofile = open('numbers2.txt', 'w')  # Create text file, 'w' overwrites text file if the file already exists.
ofile.write("8 20 48 61 82")  # Write integers
ofile.close()  # Close the text file

# Empty variables to store contents of text files.
all_numbers_contents = ""

with open('numbers1.txt', 'r+') as f:  # Creates a new file 'object' named f that is linked to the DOB.txt file in this folder. r+ means reading and writing the file.
        for line in f:
                all_numbers_contents = all_numbers_contents + line + " "
# With open will also close the text file for you, so f.close() is not needed.

with open('numbers2.txt', 'r+') as f:  # Creates a new file 'object' named f that is linked to the DOB.txt file in this folder. r+ means reading and writing the file.
        for line in f:
                all_numbers_contents = all_numbers_contents + line

all_numbers_contents = all_numbers_contents.split(' ')  # split the numbers into a list
all_numbers_contents = list(map(int, all_numbers_contents))  # Changes all strings in the list to integers, so the numbers can be sorted properly even if they're double digits.
all_numbers_contents.sort()  # sort the numbers from smallest to largest
all_numbers_contents = list(map(str, all_numbers_contents))  # Change all integers in the list to strings, so numbers can be joined later.
all_numbers_contents = ' '.join(all_numbers_contents)  # Make list into string by joining the list of numbers using whitespace, so ofile.write will work.

ofile = open('all_numbers.txt', 'w')  # Create text file, 'w' overwrites text file if the file already exists.
ofile.write(all_numbers_contents)  # Write the numbers from both text files that have been sorted to all_numbers.txt
ofile.close()  # Close the text file