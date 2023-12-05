## ti02_textinput_multiline.py

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_file('ti02_textinput_multiline.kv')

class TestApp(App):
	def build(self):
		return TextInput()

if __name__ == "__main__":
	TestApp().run()
