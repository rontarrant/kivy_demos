from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class LMBoxLayout(BoxLayout):
	def release(self):
		label = self.ids.my_label
		button = self.ids.my_button
		
		if label.text == "Here's a label":
			label.text = "Another Label"
		else:
			label.text = "Here's a label"


kv = Builder.load_file("bl09_boxlayout_sized_lower_middle.kv")

class MyApp(App):

	def build(self):
		return LMBoxLayout()

if __name__ == "__main__":
	MyApp().run()
