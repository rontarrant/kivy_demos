# The instance variable passed into a callback
# identifies the instance of a Widget with which
# the callback is associated, thus proving that
# each instance of a widget defined in a .kv file
# is, in fact, treated as an individual instance.
# (This is contrary to what is implied in the Kivy docs.)
# NOTE: A Window, on the other hand, is treated like a
# singleton. It's automatically instantiated behind the
# scenes at the same time as App.

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty

Builder.load_file("p07_instance_arg.kv")

class MyLabel(Label):
	count = NumericProperty(0)

class PropApp(App):
	def build(self):
		layout = BoxLayout()
		Window.add_widget(layout)
		
		label_01 = MyLabel()
		label_02 = MyLabel()
		layout.add_widget(label_01)
		layout.add_widget(label_02)

		print("label_01: ", label_01, "\n")
		print("label_02: ", label_02, "\n")

if __name__ == "__main__":
	PropApp().run()
