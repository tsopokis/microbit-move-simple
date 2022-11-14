input.onButtonPressed(Button.A, function () {
    move(0, 180, neopixel.colors(NeoPixelColors.Blue))
    basic.showArrow(ArrowNames.North)
})
input.onButtonPressed(Button.AB, function () {
    move(90, 90, neopixel.colors(NeoPixelColors.Red))
    basic.showIcon(IconNames.SmallSquare)
})
input.onButtonPressed(Button.B, function () {
    move(180, 0, neopixel.colors(NeoPixelColors.White))
    basic.showArrow(ArrowNames.South)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    for (let index = 0; index < 5; index++) {
        basic.showIcon(IconNames.SmallHeart)
        basic.pause(100)
        basic.showIcon(IconNames.Heart)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})
function move (servo1: number, servo2: number, color: number) {
    pixel_array.range(0, 2).showColor(color)
    pixel_array.range(3, 2).showColor(color)
    pins.servoWritePin(AnalogPin.P1, servo1)
    pins.servoWritePin(AnalogPin.P2, servo2)
}
let pixel_array: neopixel.Strip = null
pixel_array = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
basic.showIcon(IconNames.Target)
