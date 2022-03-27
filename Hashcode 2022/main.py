from Extractor import extract
from Write import write
from Contributer import Contributer
from Project import Project
from Role import Role
from Skills import Skill

from tkinter import *

def partA():
    tkinter()

    global i
    i = 0

    input = extract("b_better_start_small.in.txt")

    nb_contributers = int(input[0][0])
    nb_projects = int(input[0][1])
    i+=1

    print(nb_contributers, nb_projects)

    contributers = createContributers(input, nb_contributers)
    projects = createProjects(input, nb_projects)

    write(input)


def createContributers(input, nb_contributers):
    global i
    back = []
    count = 0

    while count != nb_contributers:
        name = input[i][0]
        nb_skills = int(input[i][1])
        skills = []
        count_b = 0
        while count_b != nb_skills:
            i+=1
            skill = Skill(input[i][0], int(input[i][1]))
            skills.append(skill)
            count_b+=1
        contributer = Contributer(name, skills)
        back.append(contributer)
        i+=1
        count+=1

    return back


def createProjects(input, nb_projects):
    global i
    back = []
    count = 0

    while count != nb_projects:
        name = input[i][0]
        duration = int(input[i][1])
        score = int(input[i][2])
        best_before = int(input[i][3])
        nb_roles = int(input[i][4])
        roles = []
        count_b = 0
        while count_b != nb_roles:
            i+=1
            role = Role(input[i][0], int(input[i][1]))
            roles.append(role)
            count_b+=1
        project = Project(name, duration, score, best_before, roles)
        back.append(project)
        i+=1
        count+=1

    return back


def tkinter():
    fen = Tk()
    fen.title = "La Vie bogoss"
    fen.size = 1920*1080


partA()