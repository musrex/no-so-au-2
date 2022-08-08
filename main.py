from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class Popup(Widget):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    


class magicwordApp(App):
    def build(self):
        self = GridLayout(rows=6, cols=1)
        self.size_hint = (0.8, 0.8)
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}

        #add widgets to window

        # image widget
        self.add_widget(Image(source="logo.png"))

        btn1 = Button(text ="Select File",
                    background_color =(2,2,2,2))
        btn1.bind(on_release=Popup)
        btn2 = Button(text ="Encrypt",
                    background_color =(2,2,2,2))
        btn3 = Button(text ="Decrypt",
                    background_color =(2,2,2,2))
        btn4 = Button(text ="Settings",
                    background_color =(2,2,2,2))

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)


        return self

if __name__ == "__main__":
    magicwordApp().run()