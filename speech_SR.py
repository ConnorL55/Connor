import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Who is your favorite Youtuber")

answer = pg.prompt("Enter your favorite Youtuber below.")

if answer == "EnderSlicer":
    speak.Speak("Wow, my favorite is EnderSlicer too. Have you liked and subbed already")
if answer == "Jake Paul":
    speak.Speak("I'm a Jake Pauler!!! LIKE AND SUBSCRIBE!!!! MERCH LINK IN BIO")
else:
    speak.Speak("Get out of my Minecraft server!!!")

speak.Speak("What's your favorite Youtube video")

video = pg.prompt("Enter your favorite Youtube video")

speak.Speak("Alright Connor, let's searching for " + video)

wb.open("https://www.youtube.com/results?search_query=" + video)
