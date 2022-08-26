import time
import threading
from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import KeyCode, Listener
from pynput import mouse


delay = 0.14
button = Button.left
start_stop_key = KeyCode(char='1')
stop_key = KeyCode(char='2')
button_names = ["Awesome"]


class click(threading.Thread):

    def __init__(self, delay, button):
        super(click, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.mouse_position = []
        self.button_names = button_names
        self.postions = []

    def setup(self):
        for b in self.button_names:
            print(f"Click the '{b}' button...")

            def on_click(x, y, button, pressed):
                if pressed:
                    self.mouse_position = [x, y]

            listener = mouse.Listener(on_click=on_click)
            listener.start()

            while self.mouse_position == []:
                time.sleep(1)

            self.positions.append(self.mouse_position)
            print(f"\tPosition: {self.mouse_position}")

            self.mouse_position = []
            listener.stop()
    
    def start_clicking(self):
        self.running = True
    
    def stop_clicking(self):
        self.running = False
    
    def exit(self):
        self.stop_clicking()
        self.program_running = False
    
    def run(self):
        self.setup()
        print("Auto-clicker has started --- Press 1 to toggle ON/OFF / Press 2 to exit")
        while self.program_running:
            while self.running:
                for p in self.positions:
                    mouse_controller.position = p
                    mouse_controller.click(self.button)
                    time.sleep(self.delay)
            time.sleep(0.1)

mouse_controller = Controller()
click_thread = click(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()


    elif key == stop_key:
        click_thread.exit()
        listener.stop()
  
  
with Listener(on_press=on_press) as listener:
    listener.join()