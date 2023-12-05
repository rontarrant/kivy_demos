## A simple button with a callback

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button

class MyButton(Button):
	color =(1, 0, .65, 1)
	background_normal = './images/ButtonOKnormal.png'
	background_down = './images/ButtonOKpressed.png'
	size_hint = (None, None)
	size = (186, 104)
	pos_hint = {"x":0.35, "y":0.3}

	
	def on_release(self):
		print("Button pressed")


class MyApp(App):
	def build(self):
		button = MyButton()
		Window.add_widget(button)

if __name__ == "__main__":
	MyApp().run()
