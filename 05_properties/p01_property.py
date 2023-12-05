# a custom property added in the Python code file.

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import NumericProperty

class MyLabel(Label):
	count = NumericProperty(0)
	
	def get_count(self):
		print("count is now: ", self.count)
	
	# Properties added via the kivy.properties module
	# automatically emit signals. This is how we harness them.
	def on_count(self, instance, value):
		self.get_count()
		
	def on_text(self, instance, text):
		print("Text passed into _on_text(): ", text)
		self.count += 1
		print("Label text: ", self.text, "\n")


class PropApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)
		
		# change the label text
		label.text = "New Text"
		label.color = (0.3, 0.7, 0.5, 1)
		
		# change the label text again
		label.text = "More New Text"
		
		# and one more time
		label.text = "Hello, Kivy World, Again!"

if __name__ == "__main__":
	PropApp().run()
