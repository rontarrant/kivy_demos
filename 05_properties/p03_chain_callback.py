# a Kivy custom property

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder


Builder.load_file("p03_chain_callback.kv")

class MyLabel(Label):

	def get_count(self):
		print("count is now: ", self.count)
		
	def on_count(self, instance, value):
		self._get_count()

	# This isn't called on start-up.
	def chain_on_text(self):
		print("Text passed into chain_on_text(): ", self.text)
		self.count += 1
		print("Label text: ", self.text, "\n")

	# This IS called on start-up.
	def on_text(self, instance, text):
		print("Text passed into on_text(): ", self.text)
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
