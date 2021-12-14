import unittest
import _tkinter
from tkinter import Tk

class TestTkinter(unittest.TestCase):
    def setUp(self):
        self.window = Tk()
        self.pump_events()

    def pump_events(self):
        while self.window.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass

    def tearDown(self):
        if self.window:
            self.window.destroy()
            self.pump_events()
