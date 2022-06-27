from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Test(App):
    def build(self):
        box1 = BoxLayout()
        box2 = BoxLayout(orientation="vertical")
        button1 = Button(text="+", font_size=30, on_release=self.incrementar)
        button2 = Button(text="-", font_size=30, on_release=self.decrementar)
        self.label = Label(text="0", font_size=30)
        box1.add_widget(button1)
        box1.add_widget(button2)
        box2.add_widget(box1)
        box2.add_widget(self.label)

        return box2

    def incrementar(self, button1):
        self.label.text = str(int(self.label.text) + 1)

    def decrementar(self, button2):
        self.label.text = str(int(self.label.text) - 1)


Test().run()
