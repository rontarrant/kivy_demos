## Allow only uppercase letters to be entered
## into a Kivy TextInput.

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class UppercaseInput(TextInput):
	def insert_text(self, substring, from_undo=False):
		s = substring.upper()
		
		return super().insert_text(s, from_undo=from_undo)

class TestApp(App):
	def build(self):
		uppercase_input = UppercaseInput()
		Window.add_widget(uppercase_input)

if __name__ == "__main__":
	TestApp().run()
