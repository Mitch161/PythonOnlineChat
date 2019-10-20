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
from friendschat import FriendFrame

#Constants
LARGE_FONT = ("roboto", 16)
COUNTDOWN_FONT = ("roboto", 32)

class HomeFrame(App):
    def __init__(self,**kwargs):
        super(HomeFrame, self).__init__(**kwargs)
        self.display = HomeGrid

    def build(self):
        Config.set('graphics', 'width', '720')
        Config.set('graphics', 'height', '1480')
        return self.display

class HomeGrid(GridLayout):
    def __init__(self, **kwargs):
        super(HomeGrid, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 1
        float_colour1 = 255/255.0
        float_colour2 = 255/255.0
        float_colour3 = 255/255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1,float_colour2,float_colour3,float_colour4)
            Rectangle(size=(720, 1480), pos=(0,0))

        #row1
        self.add_widget(WestFrame)
        self.add_widget(EastFrame)

class WestFrame(GridLayout):
    def __init__(self, **kwargs):
        super(WestFrame, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 4
        float_colour1 = 84/255.0
        float_colour2 = 84/255.0
        float_colour3 = 84/255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1,float_colour2,float_colour3,float_colour4)
            Rectangle(size=(720, 100), pos=(0,875))

        self.add_widget(FriendsButton)
        self.add_widget(ProfileButton)
        self.add_widget(SettingsButton)
        self.add_widget(QuitButton)

class EastFrame(GridLayout):
    def __init__(self, **kwargs):
        super(EastFrame, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 1
        float_colour1 = 84/255.0
        float_colour2 = 84/255.0
        float_colour3 = 84/255.0
        float_colour4 = 1
        with self.canvas:
            Color(float_colour1,float_colour2,float_colour3,float_colour4)
            Rectangle(size=(720, 100), pos=(0,875))

        self.add_widget(FriendFrame)

class FriendsButton(Button):
    def __init__(self, **kwargs):
        super(FriendsButton, self).__init__(**kwargs)
        self.text = "Friends"
        self.font_size = 34
        self.size_hint_y = None
        self.height = 150
        self.background_normal = ''
        self.background_color = [84/255.0,84/255.0,84/255.0,1]
class ProfileButton(Button):
    def __init__(self, **kwargs):
        super(ProfileButton, self).__init__(**kwargs)
        self.text = "Profile"
        self.font_size = 34
        self.size_hint_y = None
        self.height = 150
        self.background_normal = ''
        self.background_color = [84/255.0,84/255.0,84/255.0,1]
class SettingsButton(Button):
    def __init__(self, **kwargs):
        super(SettingsButton, self).__init__(**kwargs)
        self.text = "Settings"
        self.font_size = 34
        self.size_hint_y = None
        self.height = 150
        self.background_normal = ''
        self.background_color = [84/255.0,84/255.0,84/255.0,1]
class QuitButton(Button):
    def __init__(self, **kwargs):
        super(QuitButton, self).__init__(**kwargs)
        self.text = "Quit"
        self.font_size = 34
        self.size_hint_y = None
        self.height = 150
        self.background_normal = ''
        self.background_color = [84/255.0,84/255.0,84/255.0,1]