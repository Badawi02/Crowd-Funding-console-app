
import datetime

def createProject() :
    print("Hello let's create your project")
    con = input("Are you sure want to continue y/n ?")
    if con == "n" :
        print("back to main menu")

    elif con == "y" :
        title = input("Enter Title for your project :")

        details = input("Enter Details for your project :")

        while True :
            target = input("Enter price target for your project :")
            if target.isdigit() :
                break
            print("plz enter valid target price , must be number")


        while True :
                    inputDate = input("Enter the start date in format 'dd/mm/yy' : ")
                    day, month, year = inputDate.split('/')
                    isValidDate = True
                    try:
                        datetime.datetime(int(year), int(month), int(day))
                    except ValueError:
                        isValidDate = False
                    if(isValidDate):
                        print("Input date is valid ..")
                        break
                    else:
                        print("Input date is not valid..")


        while True :
                    inputDate2 = input("Enter the End date in format 'dd/mm/yy' : ")
                    day, month, year = inputDate2.split('/')
                    isValidDate = True
                    try:
                        datetime.datetime(int(year), int(month), int(day))
                    except ValueError:
                        isValidDate = False
                    if(isValidDate):
                        print("Input date is valid ..")
                        break
                    else:
                        print("Input date is not valid..")    



        try:
            operation = open("projects.text", "a")
        except Exception as err:
            print(err)
        else:
            projectinfo = f"{title}:{details}:{target}:{inputDate}:{inputDate2}\n"
            operation.write(projectinfo)
            print("You created project Successfully")
            operation.close()
