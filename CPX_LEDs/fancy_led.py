from adafruit_circuitplayground.express import cpx
import adafruit_fancyled.adafruit_fancyled as fancy
import time

cpx.pixels.auto_write = False  # Update only when we say
# make less blinding

palette = [fancy.CRGB(255, 255, 255),  # White
           fancy.CRGB(255, 255, 0),  # Yellow
           fancy.CRGB(255, 85, 0), ]  # Orange

# offset = 0  # Position offset into palette to make it "spin"
# levels = (0.25, 0.3, 0.15)
brighten = 0.001
inc = 1
while True:
    for i in range(10):
        color = fancy.palette_lookup(palette, i / inc)
        cpx.pixels.brightness = 0.002 + brighten
        # color = fancy.gamma_adjust(color, brightness=levels)
        cpx.pixels[i] = color.pack()
        # time.sleep(10)
        brighten += 0.0001
        inc += 1
        if brighten <= 1
            brighten

    cpx.pixels.show()