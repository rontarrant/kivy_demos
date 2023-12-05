## A simple button with a callback

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button

class MyButton(Button):
	text = "Push"
	
	def on_release(self):
		print("Button pressed")


class MyApp(App):
	def build(self):
		button = MyButton()
		Window.add_widget(button)

if __name__ == "__main__":
	MyApp().run()

