# Add a Label to a window using KV

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyLabel(Label):
	
	def set_text(self, new_text):
		self.text = new_text
		self.color = (0.6, 0.8, 0.7, 1)

class LabelApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)
		label.set_text("Label 04 Example")


if __name__ == "__main__":
	LabelApp().run()
