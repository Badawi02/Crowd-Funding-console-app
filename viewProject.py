
# from crudop import projectsMenu


def viewProject() :
    con = input("Are you sure want to continue y/n ?")
    if con == "n" :
        # projectsMenu()
                print("back to main menu")
    elif con == "y" :
        try:
            operation = open("projects.text", "r")
        except Exception as err:
            print(err)
        else:
            data = operation.read()
            print(data)
            operation.close()

