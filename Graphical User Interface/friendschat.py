#created 20/10/2019 - 14:04
#Mitchell Hardie
from kivy.app import  App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button

#Constants
LARGE_FONT = ("roboto", 16)
COUNTDOWN_FONT = ("roboto", 32)

class FriendFrame(GridLayout):
    def __init__(self, **kwargs):
        super(FriendFrame, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        float_colour1 = 84/255.0
        float_colour2 = 84/255.0
        float_colour3 = 84/255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1,float_colour2,float_colour3,float_colour4)
            Rectangle(size=(720, 100), pos=(0,875))

        #Current and chat history
        self.add_widget(ChatHistory)
        #Your current message or typed message
        self.add_widget(CurrentMsg)

class ChatHistory(GridLayout):
    def __init__(self, **kwargs):
        super(ChatHistory, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 1
        float_colour1 = 84/255.0
        float_colour2 = 84/255.0
        float_colour3 = 84/255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1,float_colour2,float_colour3,float_colour4)
            Rectangle(size=(720, 100), pos=(0,875))

        self.add_widget()

class CurrentMsg(GridLayout):
    def __init__(self, **kwargs):
        super(CurrentMsg, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 1
        float_colour1 = 84/255.0
        float_colour2 = 84/255.0
        float_colour3 = 84/255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1,float_colour2,float_colour3,float_colour4)
            Rectangle(size=(720, 100), pos=(0,875))

        self.add_widget(MsgBox)
        self.add_widget(SendButton)

class MsgBox():
    pass

class SendButton(Button):
    def __init__(self, **kwargs):
        super(SendButton, self).__init__(**kwargs)
        self.text = "<<"
        self.font_size = 34
        self.size_hint_y = None
        self.height = 150
        self.background_normal = ''
        self.background_color = [84/255.0,84/255.0,84/255.0,1]