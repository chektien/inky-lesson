from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# set font and text
font = ImageFont.truetype(FredokaOne, 20)
msg = "from Ean, can you \ncome to my house \ntomorrow, to Finn"

# initialize display
ink_disp = InkyPHAT('red')
ink_disp.set_border(ink_disp.WHITE)

# create a single channel image that is pure white as the inverted bg
# background = Image.open('black.png')
background = Image.new("1", (ink_disp.width, ink_disp.height), 255)

# draw on the background image
draw = ImageDraw.Draw(background)
draw.text(
    xy=(0,0),
    text=msg,
    fill=ink_disp.WHITE,
    font=font)

# set image onto display
ink_disp.set_image(background.rotate(180))

ink_disp.show()
