from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import os

#mainkvFile = Builder.load_file("mobilebertapp.kv")
class WindowManager(ScreenManager):
    pass

class Root(Screen):
    user_input = ObjectProperty(None)
    model_results= ObjectProperty(None)

    def btnTest(self):
        print("User typed: ", self.user_input.text)

    def trainModel(self):
        print('training')

class Train(Screen):
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        PATH = "."
        if platform == "android":
          from android.permissions import request_permissions, Permission
          request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
          app_folder = os.path.dirname(os.path.abspath(__file__))
          PATH = "/storage/emulated/0" #app_folder
        content.ids.filechooser.path = PATH

        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

  
    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def trainModel(self):
        print('training') 

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)   

class MobileBertTest(App):
    def build(self):
        return super().build()

    def close(self):
        App.get_running_app.stop
        window.close()



if __name__ == '__main__':
    MobileBertTest().run()