##################### Extra Hard Starting Project ######################
#imports
import datetime as dt
import pandas
import smtplib
import random

#This function will choose a random letter and change the name to that of the recepient
def change_name(name):
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt","r") as letter:
        let1=letter.read().replace("\n","\n").replace("[NAME]", name)
    return(let1)

#This function will send a birthdat message to correct user
def send_message(message_to_be_sent):
    my_email = "hihello2405@gmail.com"
    password="gdwaoiwzpupscepw"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=f"{person_email}",
                            msg=f"Subject:Happy Birthday!\n\n{message_to_be_sent}")

        
################################### MAIN #############################################
#checking today's time
now= dt.datetime.now()
now_month= now.month
now_day=now.day

#changing the birthdays.csv to a dictionary
data_file=pandas.read_csv("birthdays.csv")
data_dict= data_file.to_dict(orient="records")

#this for loop, loops through the brithday dictionary and check if it is someones birthday today
#if it is, then it will call the change_name function
#then will call the send_message function
for key in data_dict:
    person_name=(list(key.values())[0])
    person_email=(list(key.values())[1])
    person_month=(list(key.values())[3])
    person_day=(list(key.values())[4])
    if (person_day==now_day and person_month==now_month):
        message= change_name(person_name)
        send_message(message)








