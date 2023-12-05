## We use bind() to attach a callback with a non-standard name.
## We also use bind() to attach a parent's method as a callback.
## NOTE: If bind() were to be used to associate Button.on_release()
## as a callback, it would be bind()ed twice and the callback would
## fire twice.
## This double-trigger will also go off if we were to associate the
## on_release() callback in the MyButton definition in the .kv file. And
## that will happen even without calling button.bind() if the callback
## is named on_release().
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

Builder.load_file("ev05_double_bind.kv")

class MyBoxLayout(BoxLayout):
	pass
	
class MyButton(Button):
	label_to_change = ObjectProperty()
	
	def switch_label(self, *args):
		print("... and this happens later.")

		if self.label_to_change.text == "Here's a label":
			self.label_to_change.text = "Another Label"
		else:
			self.label_to_change.text = "Here's a label"


class MyLabel(Label):
	pass

class MyApp(App):
	def on_release(self, obj):
		print("This happens first...")

	def build(self):
		label = MyLabel()
		button = MyButton()
		button.label_to_change = label
		button.bind(on_release = button.switch_label)
		button.bind(on_release = self.on_release)
		
		layout = MyBoxLayout()
		layout.add_widget(label)
		layout.add_widget(button)
		
		Window.add_widget(layout)

if __name__ == "__main__":
	MyApp().run()
