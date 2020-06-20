import ctypes
import cv2
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
global num


class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = "MP4"


class MyFloatLayout(Screen):
    password = 12345678
    num = 3
    attempts = ObjectProperty(None)
    inp = ObjectProperty(None)
    text1 = "Youhave  "
    text2 = " attempts to enter a password.\nEach wrong attempt takes " \
            "you 5 minutes.\nyou can enter only numbers."
    btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MyFloatLayout, self).__init__(**kwargs)
        self.update_attempts()

    def onsendbtn(self):

        self.num -= 1
        inp = 6
        if self.num == 0:
            try:
                inp = int(self.inp.text)
            except:
                self.parent.current = "err"
                self.num = 3
                self.inp.text = ""
                self.update_attempts()
            if inp == self.password:
                self.update_attempts()
                print("well done!!!")
                self.btn.disabled = True
                self.parent.current = "success"
            else:
                self.parent.current = "err"
                self.num = 3
                self.update_attempts()
                self.inp.text = ""
        else:
            try:
                inp = int(self.inp.text)
            except:
                self.parent.current = "error"
                self.inp.text = ""
            if inp == self.password:
                self.update_attempts()
                print("well done!!!")
                self.btn.disabled = True
            else:
                self.update_attempts()

            # self.root.onsendbtn()
            self.parent.current = "error" if self.inp.text != "12345678" else "success"
            # self.parent.manager.transition.direction = "left"

    def update_attempts(self):
        try:
            self.attempts.text = self.text1 + str(self.num) + self.text2
        except:
            pass


class ErrorWindow(Screen):
    pass


class Error(Screen):

    tec = ObjectProperty(None)

    def btn(self):
        if self.tec.text == "8888":
            self.parent.current = "main"
            self.tec.text = ""
        else:
            self.tec.text = ""
            self.parent.current = "err2"


class Error2(Screen):
    pass


class success(Screen):

    def hintpop(self):
        movie = Movie_MP4(r"C:\Users\User\Dropbox\all_my_en_and_dris\programer\Prog\pycharm projects\SchoolProject\ddd.mp4")
        movie.play()
        # popup()




class WindowManager(ScreenManager):
    pass


class P(FloatLayout):
    pass


def popup():
    show = P()
    pop = Popup(title="the hint!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", content=show, size_hint=(None, None), size=(500, 500))
    pop.open()


class Main_kivyApp(App):
    def build(self):
        return kv


kv = Builder.load_file("Main_kivy.kv")

if __name__ == "__main__":
    Main_kivyApp().run()
