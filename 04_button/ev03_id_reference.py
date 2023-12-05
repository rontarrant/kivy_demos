## We use a root rule here so we can access the ids array
## to find the label. Note how the layout is simply tossed into
## the App's build() method.
## This won't work if we hand assemble the app from a collection
## of class rules using the Window class-object.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

kv = Builder.load_file("ev03_id_reference.kv")

class MyBoxLayout(BoxLayout):
	pass
	
class MyButton(Button):
	pass

class MyLabel(Label):
	pass

class MyApp(App):
	def set_text(self):
		label_to_change = self.root.ids.my_label
		
		if label_to_change.text == "Here's a label":
			label_to_change.text = "Another Label"
		else:
			label_to_change.text = "Here's a label"
		
		
	def build(self):
		return kv
		
if __name__ == "__main__":
	MyApp().run()
