# Ask the user how many students are registering.
# For loop that runs for num_students amount of students and asks for the student ID of each student.
# Write each of the ID numbers to a Text File called reg_form.txt
# Include a dotted line to sign because this document will be used as an attendance register which the students will sign when they arrive at the exam venue.

# Ask the user how many students are registering.
num_students = int(input("How many students are registering for the exam?"))

# Create a dictionary to hold student details.
student_number_d = {}

ofile = open('reg_form.txt', 'w')  # Create reg_form.txt, 'w' overwrites reg_form.txt if it already exists.
ofile.write("Please sign the dotted line next to your student ID number to register your arrival.\n\n")  # Creates header for text file.

# For loop that runs for num_students amount of students.
for i in range(0, num_students):
    student_number_d["num_students{0}".format(i)] = int(input(f"Please enter the student ID for {i+1} of {num_students} students:"))  # Create student ID variable for each student.
    ofile.write(f"Student {student_number_d['num_students{0}'.format(i)]} ......................\n\n")  # Write each of the ID numbers to reg_form.txt and add a dotted line

# Close reg_form.txt
ofile.close()