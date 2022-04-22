input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    music.playMelody("C5 C5 C5 C5 C5 A G E ", 120)
    basic.showLeds(`
        # # . . .
        . # . . #
        . # . . .
        . # # # #
        . # . # .
        `)
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.showLeds(`
        # # . . .
        . # . . .
        . # . . .
        . # # # #
        . # . # .
        `)
    basic.showIcon(IconNames.Yes)
    basic.showIcon(IconNames.No)
    basic.showIcon(IconNames.Giraffe)
})
