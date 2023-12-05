# build Kivy widgets inside a Python script
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyLabel(Label):
	text = "This is a Label"

class WindowApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)


if __name__ == "__main__":
	WindowApp().run()
