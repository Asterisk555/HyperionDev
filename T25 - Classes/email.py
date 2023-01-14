#An Email Simulation

import os
import sys

temp_variable = None

class Email:  # Classes start with a capital later

    def __init__(self, email_contents, from_address, has_been_read=False, is_spam=False):  # Adding =False here means that by default it is set to False, but can be overriden when the object is initialised
        self.has_been_read = has_been_read
        self.is_spam = is_spam
        self.email_contents = email_contents
        self.from_address = from_address  # Return to this. The constructor should initialise the sender’s email address. So read from email list?

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = False

inbox = []

def add_email(contents, from_address):
    '''
     takes in the contents and email address from the received email to make a new Email object
    '''
    email = Email(contents, from_address)
    inbox.append(email)

def get_count():
    '''
    returns the number of messages in the store.
    '''
    return len(inbox)

def get_email(index):
    '''
    returns the contents of an email in the list.
    '''
    inbox[index].mark_as_read()
    return inbox[index]
    

def get_unread_emails():
    '''
    return a list of all the emails that haven’t been read.
    '''
    return [email for email in inbox if email.has_been_read == False]

def get_spam_emails():
    return [email for email in inbox if email.is_spam == True]

def delete(email):
    inbox.remove(email)

add_email("Blah", "luc@luc.luc")

user_choice = ""

while user_choice != "quit":
    print(f"Hello. You have {get_count()} emails. {len(get_unread_emails())} unread. {len(get_spam_emails())} spam.")
    user_choice = input("What would you like to do - read/mark spam/send/quit?")
    if user_choice == "read":
        while True:
            read_choice = input("Index of email: ")
            if not read_choice.isnumeric():
                print("Please enter a number.")
                continue
            if int(read_choice) > get_count() or int(read_choice) < 0:
                print("Not a valid number.")
                continue
            email = inbox[int(read_choice)]
            email.mark_as_read()
            print(f"From: {email.from_address}")
            print(f"{email.email_contents}")
            break
    elif user_choice == "mark spam":
        while True:
            spam_choice = input("Index of email: ")
            if not spam_choice.isnumeric():
                print("Please enter a number.")
                continue
            if int(spam_choice) > get_count() or int(spam_choice) < 0:
                print("Not a valid number.")
                continue
            email = inbox[int(spam_choice)]
            email.mark_as_spam()
    elif user_choice == "send":
        from_address = input("What is your email address? ")
        contents = input("What would you like to write in the email? ")
        add_email(contents, from_address)
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
