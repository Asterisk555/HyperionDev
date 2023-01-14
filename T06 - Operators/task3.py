print("Welcome! Here I'll help you find out which award you've qualified for. Please enter your completion times for each event in minutes: ")
time_swimming = int(input("Swimming: "))
time_cycling = int(input("Cycling: "))
time_running = int(input("Running: "))

time_total = time_swimming + time_cycling + time_running
qulifying_time = 100

if time_total > qulifying_time + 10:
    print("Thank you for participating! Unfortunately you aren't eligible for any awards.")
elif time_total > qulifying_time + 5:
    print("Congratulations! You're eligible for the Provincial Scroll.")
elif time_total > qulifying_time:
    print("Congratulations! You're eligible for the Provincial Half Colours.")
else:
    print("Congratulations! You're eligible for the Provincial Colours.")