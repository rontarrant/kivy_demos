# a Kivy custom property

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder


Builder.load_file("p02_kv_property.kv")

class MyLabel(Label):
	def get_count(self):
		print("count is now: ", self.count)
	
	# Properties added in the .kv file automatically
	# emit signals. This is how we harness them.
	def on_count(self, instance, value):
		self.get_count()

	# This overrides the inherited method.
	def on_text(self, instance, text):
		print("Text passed into _on_text(): ", self.text)
		self.count += 1
		print("Label text: ", self.text, "\n")


class PropApp(App):
	def build(self):
		label = MyLabel()
		Window.add_widget(label)
		
		# change the label text
		label.text = "New Text"
		
		# change the label text again
		label.text = "More New Text"
		
		# and one more time
		label.text = "Hello, Kivy World, Again!"
		
if __name__ == "__main__":
	PropApp().run()
