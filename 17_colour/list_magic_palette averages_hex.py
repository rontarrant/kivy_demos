from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

## local
from colour_look_up import ColourLookUp as clu

colours = iter(clu.items())
colour_number = 0
count = 1
key, value = next(colours)

class LLBoxLayout(BoxLayout):
	def set_colours(self):
		global count, colour_number, key, value
		print("Hello")

		## print(self.ids.base_colour.background_color)
		## Write code to replace all colours in widgets
		## with ids: base_colour, mix_two, mix_one, average, and mix_colour.
		## Also, replace colour names in base_colour and mix_colour.
		## NOTE: The order of the colours in the display has been corrected.
		if count == 14:
			key, value = next(colours)
			count = 1
			colour_number += 1
			print("count: ", count, ", colour_number: ", colour_number)
			print("count: ", count)
			print("colour name: ", key)
			print("colour hex: ", value[0])
			print("mix colour: ", value[count][4])
			self.ids.base_colour.text = key
			self.ids.base_colour.background_color = value[0]
			self.ids.mix_one.background_color = value[count][0]
			self.ids.average.background_color = value[count][1]
			self.ids.mix_two.background_color = value[count][2]
			self.ids.mix_colour.text = value[count][4]
			self.ids.mix_colour.text = value[count][4]
			self.ids.mix_colour.background_color = value[count][3]
			self.parent.set_title(key + " - " + value[count][4])

			count += 1
		else:
			self.ids.base_colour.background_color = value[0]
			self.ids.mix_one.background_color = value[count][0]
			self.ids.average.background_color = value[count][1]
			self.ids.mix_two.background_color = value[count][2]
			self.ids.mix_colour.text = value[count][4]
			self.ids.mix_colour.text = value[count][4]
			self.ids.mix_colour.background_color = value[count][3]
			print("count: ", count)
			print("colour name: ", key)
			print("colour hex: ", value[0])
			print("mix colour: ", value[count][4])
			print("mix_colour hex: ", value[count][3])
			print("mix 1: ", value[count][0])
			print("average: ", value[count][1])
			print("mix 2: ", value[count][2])
			self.parent.set_title(key + " - " + value[count][4])
			count += 1


kv = Builder.load_file("test_magic_palette_averages_hex.kv")

class MyApp(App):
	def build(self):
		Window.size = (1000, 400)
		return LLBoxLayout()
		
if __name__ == "__main__":
	MyApp().run()
