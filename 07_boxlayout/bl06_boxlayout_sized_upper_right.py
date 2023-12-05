from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class URBoxLayout(BoxLayout):
	def release(self):
		label = self.ids.my_label
		button = self.ids.my_button
		
		if label.text == "Here's a label":
			label.text = "Another Label"
		else:
			label.text = "Here's a label"


kv = Builder.load_file("bl06_boxlayout_sized_upper_right.kv")

class MyApp(App):

	def build(self):
		return URBoxLayout()

if __name__ == "__main__":
	MyApp().run()
