from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from crypt import *

import os

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class LoadDialog(Widget):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()


class magicwordApp(App):
    def build(self):
        self = GridLayout(rows=6, cols=1)
        self.size_hint = (0.6, 0.8)
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}
        self.spacing = 25

        #add widgets to window

        # image widget
        self.add_widget(Image(source="logo.png"))

        btn1 = Button(text ="Select File",
                    background_color =(1,0,0,1))
        btn1.bind(on_release=Popup)
        btn2 = Button(text ="Encrypt",
                    background_color =(1,0,0,1))
        btn2.bind(on_release=encryptFile)
        btn3 = Button(text ="Decrypt",
                    background_color =(1,0,0,1))
        btn3.bind(on_release=decryptFile)
        btn4 = Button(text ="Settings",
                    background_color =(1,0,0,1))
        

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)


        return self

if __name__ == "__main__":
    magicwordApp().run()