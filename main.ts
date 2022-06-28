input.onButtonPressed(Button.A, function () {
    cars += 1
})
input.onButtonPressed(Button.B, function () {
    cars += -1
})
let cars = 0
if (cars > 15) {
    basic.showString("Car Park has less than 15 people")
} else {
    basic.showString("Car Park is full")
}
