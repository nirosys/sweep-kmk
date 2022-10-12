import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.RGB import RGB

# in use: D0, D2, D3, D4, D5, D6, D7, D8, D9, D10
#       : A0, A1, A2, A3
#       : MOSI, MISO, SCK
_KEY_CFG = [
        # q = D7
        # w = A0
        # e = A1
        # r = A2
        # t = A3

        # g = D0
        # f = D10
        # d = MOSI
        # s = MISO
        # a = SCK

        # / = D2
        # z = D3
        # x = D4
        # c = D5
        # v = D6

        # BACKSPACE = D8
        # FN = D9
    board.D7, board.A0, board.A1, board.A2, board.A3,

    board.SCK, board.MISO, board.MOSI, board.D10, board.D0,

    board.D2, board.D3, board.D4, board.D5, board.D6,

    board.D8, board.D9

]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        self.matrix = KeysScanner(
            pins=_KEY_CFG,
        )
        self.pixels = RGB(pixel_pin=board.NEOPIXEL, num_pixels=1)
        self.coord_mapping = [
             0,  1,  2,  3,  4,
             5,  6,  7,  8,  9,
            10, 11, 12, 13, 14,
                        15, 16,

            21, 20, 19, 18, 17,
            26, 25, 24, 23, 22,
            31, 30, 29, 28, 27,
                        33, 32,
        ]
        self.data_pin = board.D1
