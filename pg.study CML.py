# This Helps With Studying
import pyautogui as pg
import webbrowser
import time

study = pg.prompt(
"""
What class do you need to study for?

a) Math
b) Spanish
c) English

""")

if study == "a":
    answer = pg.prompt(
        """
What chapter do you need to study for?

a) Chapter 1-3
b) Chapter 4
c) Chapter 5
d) Chapter 6
""")
    pg.alert("Ready to study?","Time to study", "Let's Go")
    if answer == "a":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1v0Ikj_rIQQ_P82SJnG0G205-_BczsmdvPmkuUF_no8g/edit#gid=0")
                        
    if answer == "b":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1v0Ikj_rIQQ_P82SJnG0G205-_BczsmdvPmkuUF_no8g/edit#gid=1063804061")
        
    if answer == "c":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1v0Ikj_rIQQ_P82SJnG0G205-_BczsmdvPmkuUF_no8g/edit#gid=1120119981")
    if answer == "d":
        webbrowser.open("https://docs.google.com/spreadsheets/d/1v0Ikj_rIQQ_P82SJnG0G205-_BczsmdvPmkuUF_no8g/edit#gid=134525343")
if study == "b":
    answer = pg.prompt(
        """
What words do you need  to study?

a) Breakfast
b) Lunch
c) Clothing
d) Everything
""")
    pg.alert("Ready to study?","Time to study", "Let's Go")
    if answer == "a":
        webbrowser.open("https://quizlet.com/274281891/el-desayuno-flash-cards/")

    if answer == "b":
        webbrowser.open("https://quizlet.com/277888196/el-almuerzo-flash-cards/")

    if answer == "c":
        webbrowser.open("https://quizlet.com/258598883/la-ropa-flash-cards/")

    if answer == "d":
        webbrowser.open("https://quizlet.com/MsJanelleCharles")
if study == "c":
    answer = pg.prompt(
        """
Which vocabulary do you need to study?

a)Macbeth
b)Of Mice & Men
c)How to kill a MockingBird
""")
    pg.alert("Ready to study?","Time to study", "Let's Go")
    if answer == "a":
        webbrowser.open("https://quizlet.com/244733341/macbeth-vocab-flash-cards/")

    if answer == "b":
        webbrowser.open("https://quizlet.com/267355163/of-mice-and-men-vocab-flash-cards/")

    if answer == "c":
        webbrowser.open("https://quizlet.com/284774579/to-kill-a-mockingbird-vocab-flash-cards/")
