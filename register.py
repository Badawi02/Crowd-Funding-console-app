import re

def register():
    while True :
        fname = input("Enter your first name :")
        if fname.isalpha() :
            break
        print("plz enter valid name , must be string")

    while True :
        lname = input("Enter your last name :")
        if lname.isalpha() :
            break
        print("plz enter valid name , must be string")

    while True :
        email = input("Enter your eamil :")
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
        if re.search(regex,email) :
            break
        print("plz enter valid eamil")

    while True :
        password = input("please enter your password: ")
        if len(password) > 4 :
            confirmpassword = input("please enter your confirm password: ")
            if password == confirmpassword :
                break
            print("You entered wrong password")
        print("plz enter valid password , must be longer than 3 characters")


    while True :
        phone = input("enter your egyptain phone number :")
        nphone = list(phone)
        if phone.isdigit() and len(nphone) == 11 :
            if nphone[0:3]==['0','1','1'] or nphone[0:3]==['0','1','0'] or nphone[0:3]==['0','1','2'] or nphone[0:3]==['0','1','5']:
                break
        print("plz enter valid egyptain phone number , must be equal 11 numbers")



    try:
        operation = open("users.text", "a")
    except Exception as err:
        print(err)
    else:
        userinfo = f"{fname}:{lname}:{email}:{password}:{phone}\n"
        operation.write(userinfo)
        print ("================== Create Account successfuly ====================")
        operation.close()

