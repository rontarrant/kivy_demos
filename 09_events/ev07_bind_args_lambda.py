## We use bind() to attach a callback with a non-standard name.
## We also use bind() to attach a parent's method as a callback.
## NOTE: If bind() were to be used to associate Button.on_release()
## as a callback, it would be bind()ed twice and the callback would
## fire twice.

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

Builder.load_file("ev07_bind_args_lambda.kv")

class MyBoxLayout(BoxLayout):
	pass
	
class MyButton(Button):
	def switch_label(self, *args):
		print("... and this happens later.")
		label_to_change = args[1]

		if label_to_change.text == "Here's a label " + str(label_to_change.count - 1):
			label_to_change.text = "Another Label " + str(label_to_change.count)
		else:
			label_to_change.text = "Here's a label " + str(label_to_change.count)


class MyLabel(Label):
	def on_text(self, instance, text):
		self.count += 1
		print("count: ", self.count)
		

class MyApp(App):
	def on_release(self, obj):
		print("This happens first...")

	def build(self):
		label = MyLabel()
		button = MyButton()
		button.bind(on_release = lambda instance: button.switch_label(instance, label))
		layout = MyBoxLayout()
		layout.add_widget(label)
		layout.add_widget(button)
		
		Window.add_widget(layout)

if __name__ == "__main__":
	MyApp().run()
