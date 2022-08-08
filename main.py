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

class magicwordApp(App):
    def build(self):
        self = GridLayout()
        self.rows = 6
        

        #add widgets to window

        # image widget
        self.add_widget(Image(source="logo.png",
                                    pos_hint=(2,1)))


        btn1 = Button(text ="Select File",
                    background_color =(2,2,2,2),
                    size_hint=(.6,.6),
                    pos_hint={'x':.4, 'y':.2})
        


        btn2 = Button(text ="Encrypt",
                    background_color =(2,2,2,2),
                    size_hint=(.6,.6),
                    pos_hint={'x':.4, 'y':.4})
        btn3 = Button(text ="Decrypt",
                    background_color =(2,2,2,2),
                    size_hint=(.6,.6),
                    pos_hint={'x':.2, 'y':.2})
        btn4 = Button(text ="Settings",
                    background_color =(2,2,2,2),
                    size_hint=(.6,.6),
                    pos_hint={'x':.2, 'y':.2})

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)


        return self

if __name__ == "__main__":
    magicwordApp().run()