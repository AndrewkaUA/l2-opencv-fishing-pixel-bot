import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
import threading
import pydirectinput
import queue

os.chdir(os.path.dirname(os.path.abspath(__file__)))
wincap = WindowCapture('Asterios Pride') # game window name

def all_the_same(elements):
    return len(np.unique(elements)) <= 1

class DerivThread(threading.Thread):
    def __init__(self, q: queue.Queue):
        super().__init__()
        self.q = q
        self.stop_event = threading.Event()
        
    def run(self):
        while not self.stop_event.is_set():
            button = self.q.get()
            try:
                if (button == 'f1'):    
                    pydirectinput.press(button)
                    pydirectinput.press('f5')
                    pydirectinput.press('f6')
                    pydirectinput.press('f7')
                    time.sleep(0.1)
                if (button == 'f2' and (abs(delta_progress_bar) < 0.05) and abs(delta_progress_bar) > 0.0):
                    print('Нажал F2', 'delta = ', abs(delta_progress_bar))    
                    pydirectinput.press(button)
                    pydirectinput.press('f5')
                    pydirectinput.press('f6')
                    pydirectinput.press('f7')
                    time.sleep(0.1)
                if (bot_process_fishing == 0):
                    pydirectinput.press(button)
                    time.sleep(1)
            except queue.Empty:
                time.sleep(0.01)

# HSV values
lower_white = np.array([78,0,109])
upper_white = np.array([255,147,235])
lower_blue = np.array([62,0,124])
upper_blue = np.array([179,255,255])

# % value progress_bar
prev_progress_value = 0.0
current_progress_value = 0.0
delta_progress_bar = 0.0

# Array of screenshots for progress bar stop condition
array_screen = []

# Statement bot action
bot_process_fishing = 0
bot_attacking_fish = 0

# Threading
q = queue.Queue(maxsize = 1)
deriv = DerivThread(q)
event = deriv.stop_event
deriv.start()

loop_time = time.time()

while(True):
    screenshot = wincap.get_screenshot()

    window_fishing = screenshot[245:260, 390:435, ...]
    window_fishing = cv.cvtColor(window_fishing, cv.COLOR_BGR2HSV)
    mask_fishing = cv.inRange(window_fishing, lower_white, upper_white)
    window_fishing_value = mask_fishing.mean() / 255    


    progress_bar = screenshot[486:497, 296:527, ...]
    progress_bar = cv.cvtColor(progress_bar, cv.COLOR_BGR2HSV)
    mask_progress_bar = cv.inRange(progress_bar, lower_blue, upper_blue)

    prev_progress_value = current_progress_value
    current_progress_value = mask_progress_bar.mean() / 255

    delta_progress_bar = prev_progress_value - current_progress_value
    
    if (len(array_screen) == 80):
        array_screen.pop(0)
    else:
        array_screen.append(round(current_progress_value, 2))
        
    if (window_fishing_value > 0):
        bot_process_fishing = 1 
    else:
        bot_process_fishing = 0
    
    if (current_progress_value > 0):
        bot_attacking_fish = 1
    else:
        bot_attacking_fish = 0


    try:
        if (bot_attacking_fish == 1 and (current_progress_value > 0.0001 and all_the_same(array_screen) and delta_progress_bar == 0.0)):
            q.put_nowait('f1')
        if (bot_attacking_fish == 1 and ((current_progress_value > prev_progress_value))):
            q.put_nowait('f2')
        if (bot_process_fishing == 0):
            q.put_nowait('f4')
    except queue.Full:
        pass
    
    # print('FPS {}'.format(1 / (time.time() - loop_time)))
    cv.imshow('imshow', mask_fishing)
    loop_time = time.time()

    if cv.waitKey(1) == ord('r'):
        cv.destroyAllWindows()
        break

print('Done.')
