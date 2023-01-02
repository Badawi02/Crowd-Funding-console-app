from register import register
# from crudop import projectsMenu


def login():
    print("----------- Login Here ---------")
    uemail = input("please enter your email: ")
    upassword = input("please enter your password: ")
    try:
        operation = open("users.text", "r")
    except Exception as err :
        print(err)
    else:
        users = operation.readlines()
        for user in users:
            userdata = user.strip("\n")
            userinfo = userdata.split(":")
            if userinfo[2] == uemail and userinfo[3] == upassword:
                print("logged in successfully")
                return True
        else:
            print("May your password or youe email is wrong ")
            print("No such user , you can register here ")
            register()

