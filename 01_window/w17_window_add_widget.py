# Add a Label to a Window.

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyLabel(Label):
	pass

class WindowApp(App):
	def build(self):
		label = MyLabel(text = "My Test Label")
		Window.add_widget(label)
		

if __name__ == "__main__":
	WindowApp().run()
