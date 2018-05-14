import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/results?search_query=bouncing+seals","https://www.youtube.com/watch?v=EZ87cx0BzSc"]

music = ["https://www.youtube.com/watch?v=JGwWNGJdvx8"]

answer = pg.prompt (
"""
What would you like to do?
a) Watch videos
b) Listen to music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer == "b":
    for i in music:
        webbrowser.open(i)
