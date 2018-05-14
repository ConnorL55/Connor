import pyautogui as pg
import time

pg.hotkey('ctrl','winleft','d')
pg.hotkey('winleft')
pg.typewrite('chrome\n',0.5)
pg.hotkey('winleft', 'up')
pg.typewrite('Modern Art\n', 0.5)
pg.moveTo(251,198, 5)
pg.click(251,198)
pg.moveTo(833,415, 2)
pg.click(833,415, 2)
pg.moveTo(1356, 206)
pg.click(1356, 206)
time.sleep(5)
pg.dragTo(1358, 273, 5)
