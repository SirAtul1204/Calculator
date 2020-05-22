from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
import math
class HomeScreen(Screen):
    s = ""
    total = ""
    h = ""
    b = ""
    numbers = ['0','1','2','3','4','5','6','7','8','9', '.', '(', ')']
    def numberbtn(self, button_name):
        try:
            output = self.ids['output']
            self.s = output.text
            if button_name in self.numbers:
                output.text = output.text + button_name
            else:
                output.text = output.text
            self.s = output.text
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def opertationbtn(self, operator):
        try:
            output = self.ids['output']
            if (output.text == self.b):
                output.text = ""
            history = self.ids['history']
            self.numberbtn(operator)
            self.total = self.s + " " + operator
            history.text = history.text + self.total
            output.text = ""
            self.h = history.text
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def delbtn(self):
        try:
            output = self.ids['output']
            output.text = output.text[:-1]
            self.s = output.text
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def clearall(self):
        try:
            output = self.ids['output']
            history = self.ids['history']
            output.text = ""
            history.text = ""
            self.h = history.text
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def equalbtn(self):
        try:
            output = self.ids['output']
            self.h = self.h + output.text
            history = self.ids['history']
            history.text = self.h
            a = eval(self.h)
            output.text = str(a)
            self.b = str(a)
            history.text = str(a)
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def squarebtn(self):
        try:
            output = self.ids['output']
            output.text = output.text + '**2'
            squarestring = (eval(output.text))
            output.text = str(squarestring)
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def squarerootbtn(self):
        try:
            output = self.ids['output']
            output.text = output.text + '**0.5'
            squarestring = (eval(output.text))
            output.text = str(squarestring)
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

        


class OtherScreen(Screen):
    s = ""
    total = ""
    h = ""
    b = ""
    numbers = ['0','1','2','3','4','5','6','7','8','9', '.', '(', ')']
    def numberbtn(self, button_name):
        try:
            output = self.ids['output']
            self.s = output.text
            if button_name in self.numbers:
                output.text = output.text + button_name
            else:
                output.text = output.text
            self.s = output.text
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def opertationbtn(self, operator):
        try:
            output = self.ids['output']
            if (output.text == self.b):
                output.text = ""
            history = self.ids['history']
            self.numberbtn(operator)
            self.total = self.s + " " + operator
            history.text = history.text + self.total
            output.text = ""
            self.h = history.text
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def delbtn(self):
        try:
            output = self.ids['output']
            output.text = output.text[:-1]
            self.s = output.text
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def clearall(self):
        try:
            output = self.ids['output']
            history = self.ids['history']
            output.text = ""
            history.text = ""
            self.h = history.text
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def equalbtn(self):
        try:
            output = self.ids['output']
            self.h = self.h + output.text
            history = self.ids['history']
            history.text = self.h
            a = eval(self.h)
            output.text = str(a)
            self.b = str(a)
            history.text = str(a)
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def factbtn(self):
        try:
            output = self.ids['output']
            s = output.text
            b = math.factorial(int(s))
            output.text = str(b)
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

    def logbtn(self, base):
        try:
            output = self.ids['output']
            s = output.text
            b = math.log(float(s), float(base))
            output.text = str(b)
        except:
            history = self.ids['history']
            output = self.ids['output']
            history.text = ""
            output.text = "Error"

GUI = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return GUI
    
    def changescreen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name

MainApp().run()