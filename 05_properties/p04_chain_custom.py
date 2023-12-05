# A Kivy custom property declared in the .kv file
# with chained callbacks.

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder


Builder.load_file("p04_chain_custom.kv")

class MyLabel(Label):

	def get_count(self):
		print("count is now: ", self.count, "\n")
		
	def on_count(self):
		print("on_count called...")
		self.get_count()

	def _on_chain_count(self):
		print("on_chain_count called")
		self.get_count()
		
	# This IS called on start-up.
	def on_text(self, instance, text):
		self.count += 1


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
