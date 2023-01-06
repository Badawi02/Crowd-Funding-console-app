

def displayAllprojects():
    try:
        fileobj = open("projects.text","r")
    except Exception as e:
        print(e)
    else:
        projects = fileobj.readlines()
        print("Title:Details:Target:startData:endData")
        for project in projects:
            print(project.strip("\n"))
        return projects


def deleteProject ():
    allproject = displayAllprojects()
    projectdelete = input("please enter the Title of the project you want to delete : ")
    print(projectdelete)

    for l in allproject:
        pro_info= l.strip("\n")
        pro_info = pro_info.split(":")
        if pro_info[0] == projectdelete:
            allproject.remove(l)
            print("project found and remove it")
            break
    else:
        return deleteProject()


    w = open("projects.text", "w")
    w.writelines(allproject)
    w.close()
