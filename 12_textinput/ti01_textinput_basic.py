## ti01_textinput_basic.py

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_file('ti01_textinput_basic.kv')

class TestApp(App):
	def build(self):
		return TextInput()

if __name__ == "__main__":
	TestApp().run()
