def on_button_pressed_b():
    basic.clear_screen()
    music.play_melody("C5 C5 C5 C5 C5 A G E ", 120)
    basic.show_leds("""
        # # . . .
                . # . . #
                . # . . .
                . # # # #
                . # . # .
    """)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        # # . . .
                . # . . .
                . # . . .
                . # # # #
                . # . # .
    """)
    basic.show_icon(IconNames.YES)
    basic.show_icon(IconNames.NO)
    basic.show_icon(IconNames.GIRAFFE)
input.on_button_pressed(Button.B, on_button_pressed_b)
