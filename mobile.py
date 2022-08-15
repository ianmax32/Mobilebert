import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import FileSelect
from FileSelect import Editor

class FileChoose(App):
    def build(self):
        return FileChooser()

class View(GridLayout):
    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Finetuning mobile bert'))
        self.add_widget(Label(text='Please select the txt file to train'))
        self.btnLoadFile = Button(text="Upload")
        self.btnLoadFile.bind(on_press=self.loadPressed)
        self.add_widget(self.btnLoadFile)
        self.btnTrain = Button(text="Train")
        self.btnTrain.bind(on_press=self.trainPressed)
        self.add_widget(self.btnTrain)

    def loadPressed(self, instance):
        print("load selected")
        Editor(App)

    def trainPressed(self, instance):
        return FileChoose()

class mobile(App):
    def build(self):
        return View()


if __name__ == "__main__":
    mobile().run()