for index in range(4):
    basic.show_leds("""
        # # # # #
                # . . . #
                # . . . #
                . . . . .
                . . . . .
    """)
    basic.show_icon(IconNames.TSHIRT)
    basic.show_leds("""
        # # # # #
                # # . # #
                # # . # #
                # # . # #
                # # . # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # # . # #
                # # . # #
    """)