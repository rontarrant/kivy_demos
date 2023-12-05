## This example uses a pointer to the label stored in
## button to access the label's text and make the changes.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

Builder.load_file("ev02_object_reference.kv")

class MyBoxLayout(BoxLayout):
	pass
	
class MyButton(Button):
	label_to_change = ObjectProperty()

	def on_release(self, *args):
		if self.label_to_change.text == "Here's a label":
			self.label_to_change.text = "Another Label"
		else:
			self.label_to_change.text = "Here's a label"


class MyLabel(Label):
	pass

class MyApp(App):

	def build(self):
		label = MyLabel()
		button = MyButton()
		button.label_to_change = label
		
		layout = MyBoxLayout()
		layout.add_widget(label)
		layout.add_widget(button)
		
		Window.add_widget(layout)

if __name__ == "__main__":
	MyApp().run()
