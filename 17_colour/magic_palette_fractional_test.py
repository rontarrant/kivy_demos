## test_magic_palette_fractional.py
## To mimic how the Zorn app works, this test platform uses
## colour name strings to look up first the base colour,
## then the mix colour. See the print() statements for
## how the fractional colour triplets are accessed.
from magic_palette_fractional import ColourLookUp as clu

## These two take the place of setting colour names from
## the Spinners used in the Zorn App.
key_colour_text = "Cadmium Red Light"
mix_colour_text = "Cadmium Yellow Medium"

## get the base colour and its data from the dictionary
base_colour_chip_set = clu[key_colour_text]

## Find the mix colour string within the base colour's data
## which makes working_chip the tuple we're working with.
for chip in base_colour_chip_set:
	if chip[2] == mix_colour_text:
		working_chip = chip

## the RGB value of the base colour
key_colour_rgb = base_colour_chip_set[0]

## We look up the name of the mix colour by name as well
## and it'll be at:
mix_colour_name = working_chip[2]

## and the mix colour RGB values are found at:
mix_colour_rgb = working_chip[1]

## Finally, the midpoint colour is found here:
midpoint_colour = working_chip[0]
## Now we've got a pairing of base colour and mix colour.
## Print the results.
print("Base: \t\t", key_colour_text, "\t", key_colour_rgb)
print("Mix Colour: \t", mix_colour_name, "\t", mix_colour_rgb)
print("Mid colour: \t\t\t\t", midpoint_colour)
