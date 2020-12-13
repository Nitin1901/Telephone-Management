# Importing the libraries
import random # To generate random text
import string # To select all the characters
import re     # To match the strings  (regular expressions)
import time   # To pause for some time

# Declaring the variables
num_to_month = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
auth = False
ticket = 0
phone = 0

# Welcome
def welcome():
    print("Hi, Welcome to ACT! Please select the service you need help with.")
    print("1.ACT Broadband.")
    print("2.Cable TV.")
    print("3.Need a new connection.")
    ch = int(input("Enter your choice: ")) # Taking input
    while(ch > 3 or ch < 1): # Validating the input
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if ch == 1:
        broadband()
    elif ch == 2:
        cable()
    else:
        new_connection()

# Get phone number
def get_phone():
    phone = input("Enter your 10 digit mobile number: ")
    if validate_number(phone):
        return phone
    else:
        print("Wrong input. Try again.")
        get_phone()

# Validating phone number
def validate_number(phone):
    if len(phone) == 10:
        pattern = re.compile("[7-9][0-9]{9}") # Using re pattern to match the phone number
        return pattern.match(phone)
    return False

# Validating mail id
def validate_mail(mail):
    pattern = re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$") # using regex pattern to match email id
    return pattern.match(mail)

# Get random text
def generate_text():
    letters = string.ascii_letters + string.digits # Storing all the available charatcter and digits
    return ''.join(random.choice(letters) for i in range(5)) # Generating a string of length 5 from the stored variable

# Generate a random ticket number
def generate_ticket():
    digits = string.digits
    return 'SR' + ''.join(random.choice(digits) for i in range(10))

# Start again
def start_again():
    ch = input("Start a new chat, Yes/No? ")
    if ch[0].lower() == 'y':
        welcome()
    else:
        print("Thank you.")

# Authenticate
def authenticate():
    print("As a process of authentication, I would require you to provide your 10 digit mobile number.")
    global phone
    phone = get_phone()
    random_text = generate_text()
    print(random_text)
    user_text = input("Enter the text shown above: ")
    if random_text == user_text:
        print("Verification is successful.")
        return True
    else:
        print("The captcha entered was incorrect.")
        authenticate()

# Provide feedback
def feedback():
    time.sleep(2) # Pausing for 2 seconds to generate the feedback form
    print("Please provide your feedback.")
    print("How helpful was this conversation on a scale of 1-5?")
    ch = int(input("Enter your choice: "))
    while(ch > 5 or ch < 1):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    print("Thank you for providing your feedback.")
    start_again()

# ACT Broadband
def broadband():
    global auth # making the authentication variable global so that the user need not enter it many times
    if(not auth):
        auth = authenticate()
    print(" 1.New connection")
    print(" 2.Internet not working")
    print(" 3.Router configuration")
    print(" 4.Forgot password")
    print(" 5.Account details")
    print(" 6.Bill details")
    print(" 7.How do I pay my bill")
    print(" 8.Reconnection")
    print(" 9.Shifting request")
    print("10.Check service ticket status")
    print("11.Payment receipt")
    print("12.Change my plan")
    print("13.My connection goes off when power goes off")
    print("14.New offers")
    ch = int(input("Enter your choice: "))
    while(ch > 14 or ch < 1):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if ch == 1:
        new_broadband()
    elif ch == 2:
        internet_not_working() 
    elif ch == 3:
        configure_router()
    elif ch == 4:
        forgot_password()
    elif ch == 5:
        account_details()
    elif ch == 6:
        bill_details()
    elif ch == 7:
        how_to_pay()
    elif ch == 8:
        reconnection() 
    elif ch == 9:
        shift()
    elif ch == 10:
        check_status()
    elif ch == 11:
        payment_receipt()
    elif ch == 12:
        change_plan()
    elif ch == 13:
        power_issues()
    else:
        new_offers()

# New broadband connection
def new_broadband():
    new_connection()

# Internet not working
def internet_not_working():
    global ticket
    print("We are checking the connectivity from backend. This might take about 10 seconds.")
    time.sleep(10)
    print("Please confirm if you are able to open www.google.com")
    print("1.Yes\n2.No")
    ch = int(input("Enter your choice: "))
    while(ch > 2 or ch < 1):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if ch == 1:
        print("Please select your issue")
        print("1.I am facing slow speed/buffering\n2.I am facing issue opening specific sites")
        ch1 = int(input("Enter your choice: "))
        while(ch1 > 2 or ch1 < 1):
            print("Wrong input. Try again.")
            ch1 = int(input("Enter your choice: "))
        if ch1 == 1:
            print("Regret the inconvenience. Request you to follow these simple troubleshooting steps –")
            print("- Please restart your router")
            print("- Please clear browse cache/cookies")
            print("- Please connect to 5Ghz for better speeds")
            print("- You might experience slow speed on VPN. Please disconnect from VPN and check your speed")
            print("Is the issue resolved?\n1.Yes\n2.No")
            ch2 = int(input("Enter your choice: "))
            while(ch2 > 2 or ch2 < 1):
                print("Wrong input. Try again.")
                ch2 = int(input("Enter your choice: "))
            if ch2 == 1:
                print("Great! Looks like your service have been restored. Thank you for your patience.")
            else:
                print("Request you to provide the comments")
                print("Thank you for your patience. We sincerely regret the inconvenience.", end=" ")
                print("Please be assured that we are working towards resolving this at the earliest.", end=" ")
                ticket = generate_ticket()
                print("Your ticket number is", ticket)
        else:
            input("Please enter the site with which you are having trouble: ")
            ticket = generate_ticket()
            print("Your ticket number is", ticket)
    else:
        print("Request you to provide the comments")
        print("Thank you for your patience. We sincerely regret the inconvenience.", end=" ")
        print("Please be assured that we are working towards resolving this at the earliest.", end=" ")
        ticket = generate_ticket()
        print("Your ticket number is", ticket)
    feedback()

# Configure router
def configure_router():
    global ticket
    global phone
    print("We are checking the connectivity from backend. This might take about 10 seconds.")
    time.sleep(10)
    print("Please select the router issue you are facing to help us resolve your issue.")
    print("1.Need to change the WiFi name or password.")
    print("2.Auto-login of the internet.")
    print("3.Need to change my router login password.")
    print("4.Need to configure my new router.")
    print("5.Forgot my WiFi password.")
    ch = int(input("Enter your choice: "))
    while(ch > 5 or ch < 1):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if ch == 1:
        print("A link has been sent to", phone)
    elif ch == 2:
        print("Please select the remember me option on the login page.")
    elif ch == 3:
        print("A link has been sent along with the instructions to", phone)
    elif ch == 4:
        print("We will send you the configuration steps to", phone)
    else:
        forgot_password()
        return
    feedback()

# Forgot password
def forgot_password():
    print("Your ACT account credentials are sent to your registered mobile number.")
    feedback()

# Account details
def account_details():
    print("Your current active package is A-Max 700 6M with quota of 500 GB and speed of 50 Mbps.")
    print("Would you like me to assist you with any further details?")
    print("1.Due amount")
    print("2.Usage details")
    print("3.Due date")
    print("4.No thank you")
    ch = int(input("Enter your choice: "))
    while(ch > 4 or ch < 1):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if ch == 1:
        print(f"Your current due amount is Rs {random.randint(0,5000)}.")
    elif ch == 2:
        print(f"You have currently used {random.randint(0,100)} GB of the 100 GB.")
    elif ch == 3:
        print(f"Your payment due date is {random.randint(1,30)} {num_to_month[random.randint(0,11)]} {2021}")
    else:
        feedback()
        return
    other_details()

# Other details
def other_details():
    ch = input("Would you like me to assist you with any further details, Yes/No? ")
    if ch[0].lower() == 'y':
        account_details()
    else:
        feedback()

# Bill details
def bill_details():
    to = input("Enter the mail id to send the latest receipt: ")
    if(validate_mail(to)):
        month = int(input("Please select the month number to send the bill: "))
        while(month > 12 or month < 1):
            print("Wrong input. Try again.")
            month = int(input("Please select the month number to send the bill."))
        print(f"We have sent the bill for the month {num_to_month[month-1]} to your registered mail id {to}")
        feedback()
    else:
        print("Wrong mail id. Try again.")
        bill_details()

# How to pay bill
def how_to_pay():
    print("You can make the payment through our ACT Fibernet app or on our website.")
    print("To know more you can also refer the FAQs section")
    feedback()

# Reconnection
def reconnection():
    print("Great! Looks like your account is already active. For any further queries, restart the chat again.")
    start_again()

# Shift connection
def shift():
    print("Okay, I will need a few details to proceed further.")
    print("1.Sure\n2.Not now")
    ch = int(input("Enter your choice: "))
    while(ch > 2 or ch < 1):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if(ch==1):
        print("We would need a few details. Redirecting you to other screen for the same.")
        print("For any further queries, restart the chat again.")
    else:
        print("I hope to see you soon! For any further queries connect with us through our ACT Fibernet app")
    feedback()

# Check status
def check_status():
    if ticket != 0:
        print("These are the service requests open for you.")
        print(ticket)
    else:
        print("There are no tickets open for you.")
    feedback()

# Payment receipt
def payment_receipt():
    to = input("Enter the mail id to send the latest receipt: ")
    if(validate_mail(to)):
        print("Payment receipt has been sent to", to)
        feedback()
    else:
        print("Wrong mail id. Try again.")
        payment_receipt()

# Change plan
def change_plan():
    print("Okay, I will need a few details to proceed further")
    print("1.Sure\n2.Not now")
    ch = int(input("Enter your choice: "))
    while(ch > 2 or ch < 1):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if ch == 1:
        print("We would need a few details. Redirecting you to other screen for the same.")
        print("For any further queries, restart the chat again.")
    else:
        print("I hope to see you soon! For any further queries connect with us through our ACT Fibernet app.")
    start_again()

    
# Power issues
def power_issues():
    print("We are checking the connectivity from backend. This might take about 10 seconds.")
    time.sleep(10)
    print("Thank you for your patience. We sincerely regret the inconvenience.", end=" ")
    print("Please be assured that we are working towards resolving this at the earliest.", end=" ")
    global ticket
    ticket = generate_ticket()
    print("Your ticket number is", ticket)
    feedback()

# New offers
def new_offers():
    print("Choose from the below to know more about products and offers.")
    print("1.Act Stream TV 4K")
    print("2.Netflix")
    print("3.Zee5")
    print("4.SonyLiv")
    print("5.Hungama")
    print("6.Yuppmaster")
    print("7.Gaming")
    print("8.Act shield")
    print("9.No thank you")
    ch = int(input("Enter your choice: "))
    while(ch > 9 or ch < 1):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if ch == 1:
        print("All your streaming apps on your TV screen! *Device rental @ Rs. 200/month.")
    elif ch == 2:
        print("Subscribe and get cashback up to Rs. 500.")
    elif ch == 3:
        print("Get your one-month free trial!")
    elif ch == 4:
        print("Add your SonyLiv subscription @ Rs. 299/month.")
    elif ch == 5:
        print("Add Hungama to your ACT bill @ Rs. 99/month.")
    elif ch == 6:
        print("Prepare yourself for the next step. NEET and IIT coaching at no cost!")
    elif ch == 7:
        print("300Mbps speed boost + bonus data + offers on gaming brands.")
    elif ch == 8:
        print("Secure your digital life starting @ Rs. 49/month.")
    else:
        feedback()
        return
    other_offer()

# Other offers
def other_offer():
    ch = input("Would you like us to assist you with any other offer details, Yes/No? ")
    if ch[0].lower() == 'y':
        new_offers()
    else:
        feedback()

# Cable TV
def cable():
    print("1.New user")
    print("2.Existing user")
    ch = int(input("Enter your choice: "))
    while(ch > 2 or ch < 0):
        print("Wrong input. Try again.")
        ch = int(input("Enter your choice: "))
    if ch == 1:
        global auth
        if(not auth):
            auth = authenticate()
        print("Done. Our representatives will get back to you soon on", phone)
        start_again()
    else:
        reg = input("Enter your 5 digit registration number: ")
        while(len(reg) != 5):
            print("Wrong input. Try again.")
            reg = input("Enter your 5 digit registration number: ")
        print("We have raised a ticket on your ID. Our representatives will get back to you in 24 hours.")
        start_again()

# New Connection
def new_connection():
    global auth
    if(not auth):
        auth = authenticate()
    print("Done. Our representatives will get back to you soon on", phone)
    start_again()

# Driver function (main function)
if __name__ == "__main__":
    welcome()
