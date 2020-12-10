import random
import string
import re
import time

# Welcome
def welcome():
    print("Hi, Welcome to ACT! Please select the service you need help with")
    print("1.ACT Broadband")
    print("2.Cable TV")
    print("3.Need a new connection")
    ch = int(input("Enter your choice: "))
    while(ch > 3 or ch < 1):
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
    pattern = re.compile("[7-9][0-9]{9}")
    return pattern.match(phone)

# Validating mail id
def validate_mail(mail):
    patern= re.compile("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    return pattern.match(mail)

# Get random text
def generate_text():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(5))

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
    phone = get_phone()
    random_text = generate_text()
    print(random_text)
    user_text = input("Enter the text shown above: ")
    if random_text == user_text:
        return True
    else:
        print("The captcha entered was incorrect.")
        authenticate()

# Provide feedback
def feedback():
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
        pass
    elif ch == 2:
        pass
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch == 5:
        pass
    elif ch == 6:
        pass
    elif ch == 7:
        how_to_pay()
    elif ch == 8:
        pass
    elif ch == 9:
        pass
    elif ch == 10:
        pass
    elif ch == 11:
        payment_receipt()
    elif ch == 12:
        pass
    elif ch == 13:
        power_issues()
    else:
        new_offers()

# How to pay bill
def how_to_pay():
    if(not auth):
        auth = authenticate()
    print("You can make the payment through our ACT Fibernet app or on our website.")
    print("To know more you can also refer the FAQs section")
    feedback()

# Payment receipt
def payment_receipt():
    to = input("Enter the mail id to send the latest receipt: ")
    if(validate_mail(to)):
        print("Payment receipt has been sent to", to)
    else:
        print("Wrong mail id. Try again.")
        payment_receipt()

# Power issues
def power_issues():
    print("We are checking the connectivity from backend. This might take about 10 seconds.")
    time.sleep(10)
    print("Thank you for your patience. We sincerely regret the inconvenience.", end=" ")
    print("Please be assured that we are working towards resolving this at the earliest.", end=" ")
    print("Your ticket number is", generate_ticket())
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
    print("Would you like us to assist you with any other offer details, Yes/No? ")
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
    if(not auth):
        auth = authenticate()
        print("Done. Our representatives will get back to you soon on", phone)
        start_again()

# Main function
if __name__ == "__main__":
    auth = False
    welcome()