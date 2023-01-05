from register import register
from login import login
from createproject import createProject
from viewProject import viewProject
from deleteProject import deleteProject
#from editProject import editproject


def projectsMenu():
    print("================================================================")
    choice = input("please enter your choice\nc) Create you project\nv) view all project \ne) edit in your project  \nx) delete in your project \ns) search for projects \nq) Return to main menu ")
    if choice == "c":
        createProject()
    elif choice == "v":
        viewProject()
    elif choice == "x":
        deleteProject()
#    elif choice == "e":
#        editproject()
#    elif choice == "s":
#        print("this option will be available Soon :)")
    elif choice == "q":
        mainMenu()
    else:
        print("plz enter vaild choise")
        projectsMenu()


def mainMenu():
    choice = input("Please enter l for login , r for register ")
    if choice == "r":
        register()
    elif choice == "l":
        m = login()
        if m :
            projectsMenu()


mainMenu()


