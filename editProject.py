from deleteProject import displayAllprojects
import datetime


def editproject():
    allprojects = displayAllprojects()  
    projectedit = input("please enter the Title of the project you want to edit : ")
    for l in allprojects:
        pro_info = l.strip("\n")
        pro_info = pro_info.split(":")
        print(pro_info)
        if pro_info[0] == projectedit:
            print("Projectfound")

            part_to_edit = input("please choose:\nt) for edit Title \nd) for edit details  \nm) for edit Target  \nst) for edit start date \net) for edit End date  \na) for edit All ")
            if part_to_edit == "t":
                newTitle = input("please enter your Title ")
                pro_info[0] = newTitle
            elif part_to_edit == "d":
                newDetails = input("please enter your Details ")
                pro_info[1]= newDetails
            elif part_to_edit == "m":
                while True :
                    newTarget = input("please enter your Target ")
                    if newTarget.isdigit() :
                        break
                    print("plz enter valid target price , must be number")
                pro_info[2] = newTarget
            
            elif part_to_edit == "st":
                while True :
                    date_string = input("Enter Start date for your project :")
                    date_format = '%Y-%m-%d'
                    try:
                        date_obj = datetime.datetime.strptime(date_string, date_format)
                        break
                    except ValueError:
                        print("Incorrect data format, should be YYYY-MM-DD")
                pro_info[3] = date_string

            elif part_to_edit == "et":
                while True :
                    date_string2 = input("Enter End date for your project :")
                    date_format = '%Y-%m-%d'
                    try:
                        date_obj = datetime.datetime.strptime(date_string2, date_format)
                        break
                    except ValueError:
                        print("Incorrect data format, should be YYYY-MM-DD")
                pro_info[4] = date_string2

            elif part_to_edit == "a":
                newTitle = input("please enter your Title ")
                pro_info[0] = newTitle
                newDetails = input("please enter your Details ")
                pro_info[1]= newDetails
                while True :
                    newTarget = input("please enter your Target ")
                    if newTarget.isdigit() :
                        break
                    print("plz enter valid target price , must be number")
                pro_info[2] = newTarget

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
                        pro_info[3] = inputDate
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
                        pro_info[4] = inputDate2
                        break
                    else:
                        print("Input date is not valid..")

            print(pro_info)
            updated_project=":".join(pro_info)
            updated_project = f"{updated_project}\n"
            projectindex = allprojects.index(l)
            print(projectindex)
            allprojects[projectindex] = updated_project
            break
    else:
        return editproject()

    w = open("projects.text", "w")
    w.writelines(allprojects)
    w.close()
