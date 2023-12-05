## ti03_textinput_colors.py

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_file('ti03_textinput_colors.kv')

class TestApp(App):
	def build(self):
		return TextInput()

if __name__ == "__main__":
	TestApp().run()
