def on_button_pressed_a():
    music.stop_all_sounds()
    pixel_array.range(0, 2).show_color(neopixel.colors(NeoPixelColors.BLUE))
    pixel_array.range(3, 2).show_color(neopixel.colors(NeoPixelColors.BLUE))
    pins.servo_write_pin(AnalogPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 180)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    pixel_array.range(0, 2).show_color(neopixel.colors(NeoPixelColors.RED))
    pixel_array.range(3, 2).show_color(neopixel.colors(NeoPixelColors.RED))
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.ring_tone(262)
    pixel_array.range(0, 2).show_color(neopixel.colors(NeoPixelColors.WHITE))
    pixel_array.range(3, 2).show_color(neopixel.colors(NeoPixelColors.WHITE))
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def move(list2: List[any], sprite: game.LedSprite):
    pass
pixel_array: neopixel.Strip = None
pixel_array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
basic.show_icon(IconNames.TARGET)