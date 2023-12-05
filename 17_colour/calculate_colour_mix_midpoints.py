## Calculate colour mix midpoints
## NOTE: substring slices need a start and end point, NOT a start and number of characters.

hex1 = "6c2f8e"
hex2 = "00c0cb"

red1 = int(hex1[0:2], 16)
green1 = int(hex1[2:3], 16)
blue1 = int(hex1[4:5], 16)
print(hex1, " RGB: ", red1, green1, blue1, "\n")

red2 = int(hex2[0:2], 16)
green2 = int(hex2[2:3], 16)
blue2 = int(hex2[4:5], 16)
print(hex2, " RGB: ", red2, green2, blue2, "\n")

mix_red = int((red1 + red2) / 2)
mix_green = int((green1 + green2) / 2)
mix_blue = int((blue1 + blue2) / 2)
int_red = "{:03d}".format(mix_red)
int_green = "{:03d}".format(mix_green)
int_blue = "{:03d}".format(mix_blue)

mix_hex_red = hex(mix_red)[2:]
mix_hex_green = hex(mix_green)[2:]
mix_hex_blue = hex(mix_blue)[2:]
mix_hex = format(mix_red, "02x") + format(mix_green, "02x") + format(mix_blue, "02x")



print("midpoint: (" + int_red, ", ", int_green, ", ", int_blue + ")")
print("midpoint hex: " + mix_hex)

print("IN Kivy format:")
print("Colour 1: ", "{:.3f}".format(red1 / 255), "{:.3f}".format(green1 / 255), "{:.3f}".format(blue1 / 255))
print("Colour 2: ", "{:.3f}".format(red2 / 255), "{:.3f}".format(green2 / 255), "{:.3f}".format(blue2 / 255))
print("midpoint colour: ", "{:.3f}".format(mix_red / 255), "{:.3f}".format(mix_green / 255), "{:.3f}".format(mix_blue / 255))