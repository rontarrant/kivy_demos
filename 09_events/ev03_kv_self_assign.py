from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class MyBoxLayout(BoxLayout):
	pass
	
class MyButton(Button):
	label = ObjectProperty()
	
	def release(self):	
		if self.label.text == "Here's a label":
			self.label.text = "Another Label"
		else:
			self.label.text = "Here's a label"


kv = Builder.load_file("ev03_kv_self_assign.kv")

class MyApp(App):

	def build(self):
		return MyBoxLayout()

if __name__ == "__main__":
	MyApp().run()
