from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Contador(BoxLayout):
    pass

class Test(App):         #criar test.kv
    def build(self):
         return Contador()

Test().run()
