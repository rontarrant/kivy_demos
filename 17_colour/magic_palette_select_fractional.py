from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

## local
from colour_look_up import ColourLookUp as clu

## new globals
base_key = None
chip_tuple = None

class LLBoxLayout(BoxLayout):
	def set_colours(self, spinner_id):
		print("first spinner set to: ", self.ids.base_spinner.text)
		print("second spinner set to: ", self.ids.mix_spinner.text)
		global base_key, chip_tuple
		working_chip = None
		'''
		if spinner_id == "base_spinner":
			self.ids.base_spinner.text = "Select Base Colour"
		elif spinner_id == "mix_spinner":
			print("second spinner")
			self.ids.mix_spinner.text = "Select Mix Colour"
		'''
		## Find the selected base_colour in colours dictionary.
		if spinner_id == "base_spinner":
			## set the clu dictionary key so we can access the
			## mixed colours associated with it.
			base_key = list(clu.keys()).index(self.ids.base_spinner.text)
			
			## This points to the selected base colour in the dictionary.
			chip_tuple = clu[self.ids.base_spinner.text]
			## print("\n\n", chip_tuple, "\n\n")			

			## Put the colour's hex value on base_colour chip.
			self.ids.base_colour.text = chip_tuple[0]
			
			## And now set the actual colour of the base_colour chip.
			self.ids.base_colour.background_color = chip_tuple[0]
			
			## If a mix_colour is NOT set, abort
			if self.ids.mix_spinner.text == "Select Mix Colour":
				print("A mix colour needs to be set before we can do a mix.")
			## Else if a mix_colour IS set, fill in the chips
			else:
				## Now we have to find which colour chip we're working with
				for chip in chip_tuple:
					if chip[4] == self.ids.mix_spinner.text:
						working_chip = chip
						print("Found the colour: ", working_chip[4])
						self.ids.mix_one.background_color = working_chip[0]
						##self.ids.mix_one.text = "Mix One\n" + self.ids.mix_one.background_color
						self.ids.average.background_color = working_chip[1]
						##self.ids.average.text = "Average\n" + self.ids.average.background_color
						self.ids.mix_two.background_color = working_chip[2]
						##self.ids.mix_two.text = "Mix Two\n" + self.ids.mix_two.background_color
					
				
		elif spinner_id == "mix_spinner":
			if base_key == None:
				print("No base colour set")
				self.ids.mix_spinner.text = "Select Mix Colour"
			else:
				print("Base colour set. Let's go.")
				#self.ids.mix_colour.text = chip_tuple[4]
				for chip in chip_tuple:
					if chip[4] == self.ids.mix_spinner.text:
						working_chip = chip
						print("Found the colour: ", working_chip[4])
						 ## put the hex value on the chip
						self.ids.mix_colour.text = working_chip[3]
						## set the chip colours
						self.ids.mix_colour.background_color = working_chip[3]
						self.ids.mix_one.background_color = working_chip[0]
						self.ids.average.background_color = working_chip[1]
						self.ids.mix_two.background_color = working_chip[2]
						self.ids.mix_1_label.text = working_chip[0]
						self.ids.average_label.text = working_chip[1]
						self.ids.mix_2_label.text = working_chip[2]


		## If no mix_colour selected:
		## 	exit set_colours()
		## Else if a mix_colour is selected:
		##		Find selected mix_colour in colours dictionary.
		## 
		## 
		## NOTE: The order of the colours in the display has been corrected.
		'''
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
			#self.parent.set_title(key + " - " + value[count][4])

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
		'''

kv = Builder.load_file("magic_palette_select_hex.kv")

class MyApp(App):
	def build(self):
		Window.size = (1000, 432)
		self.title = "Magic Palette Selector"
		return LLBoxLayout()
		
if __name__ == "__main__":
	MyApp().run()
