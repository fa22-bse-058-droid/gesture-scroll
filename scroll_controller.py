from pynput.mouse import Controller, Button
import time
from config import SCROLL_SENSITIVITY, SCROLL_COOLDOWN

mouse = Controller()

class ScrollController:
    def __init__(self):
        self.last_scroll_time = 0

    def scroll(self, direction, delta=0.1):
        now = time.time()
        if now - self.last_scroll_time < SCROLL_COOLDOWN:
            return

        amount = SCROLL_SENSITIVITY

        if direction == 'up':
            mouse.scroll(0, amount)      # positive = up
        elif direction == 'down':
            mouse.scroll(0, -amount)     # negative = down

        self.last_scroll_time = now