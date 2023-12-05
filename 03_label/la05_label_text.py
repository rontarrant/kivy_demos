# Add a Label to a window using KV
# and association by name.

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyLabel(Label):
	pass

class la05_Label_TextApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)


if __name__ == "__main__":
	la05_Label_TextApp().run()
