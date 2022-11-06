import time
start_time = time.monotonic()
print("Starting..")

import board
from kb import KMKKeyboard

from kmk.keys import KC, make_key
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.combos import Combos, Chord
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB

# split = Split(split_side=SplitSide.LEFT)
split = Split(split_type=SplitType.UART, use_pio=True)
combos = Combos()

keyboard = KMKKeyboard()
keyboard.modules = [Layers(), split, combos]
keyboard.extensions.append(MediaKeys())
# keyboard.extensions.append(RGB(pixel_pin=board.NEOPIXEL, num_pixels=1))
# keyboard.debug_enabled = True

L_EXT = KC.MO(1)
L_SYM = KC.MO(2)
L_NUM = KC.MO(3)

combos.combos = [
    Chord((KC.W, KC.E),          KC.ESC),
    Chord((KC.X, KC.C),          KC.TAB),
    Chord((KC.K, KC.L),          KC.ENT),
    Chord((KC.I, KC.O),          KC.BSPACE),
    Chord((KC.SPACE, KC.LSHIFT), KC.LCTRL),
]

____ = KC.TRNS

keyboard.keymap = [
    # DEFAULT
    [
        # LEFT
        KC.Q,              KC.W,              KC.E,                  KC.R,            KC.T,        
        KC.A,              KC.S,              KC.D,                  KC.F,            KC.G,        
        KC.Z,              KC.X,              KC.C,                  KC.V,            KC.B, 
                                                                     L_EXT,           KC.LSHIFT,      

        # RIGHT
        KC.Y,               KC.U,              KC.I,                 KC.O,            KC.P,
        KC.H,               KC.J,              KC.K,                 KC.L,            KC.QUOTE,
        KC.N,               KC.M,              KC.COMMA,             KC.DOT,          KC.SLASH,
        KC.SPACE,           L_SYM,
    ],
    [ # EXT LAYER
        # LEFT
        ____,               ____,              KC.AUDIO_VOL_DOWN,    KC.AUDIO_VOL_UP, ____,
        KC.LCTL,            KC.LALT,           KC.LCMD,              KC.LSHIFT,       ____,        
        ____,               ____,              ____,                 KC.TAB,          KC.V,    
                                                                     KC.NO,           KC.TRNS,

        # RIGHT
        KC.HOME,            KC.PGDN,           KC.PGUP,              KC.END,          ____,
        KC.LEFT,            KC.DOWN,           KC.UP,                KC.RIGHT,        KC.BACKSPACE,
        ____,               KC.ENT,            ____,                 ____,            KC.DEL,
        KC.ENT,             L_NUM,
    ],
    [ # SYM LAYER
        # LEFT
        KC.LSFT(KC.N1),     KC.LSFT(KC.N2),    KC.LSFT(KC.N3),       KC.LSFT(KC.N4),  KC.LSFT(KC.N5),        
        KC.GRAVE,           KC.LSFT(KC.GRAVE), KC.LSFT(KC.LBRACKET), KC.LSFT(KC.N9),  KC.LBRACKET,
        KC.LSFT(KC.COMMA),  KC.LSFT(KC.DOT),   KC.LSFT(KC.RBRACKET), KC.LSFT(KC.N0),  KC.RBRACKET,
                                                                     L_NUM,           ____,

        # RIGHT
        KC.LSFT(KC.N6),     KC.LSFT(KC.N7),    KC.LSFT(KC.N8),       KC.LSFT(KC.MINS), KC.SCOLON,
        KC.LSFT(KC.SCOLON), KC.LSHIFT,         KC.LCMD,              KC.LALT,          KC.LCTRL,
        KC.LSFT(KC.BSLASH), KC.MINS,           KC.EQL,               KC.LSFT(KC.EQL),  KC.BSLASH,
        ____,              ____,
    ],
    [ # NUM LAYER
        # LEFT
        ____,               ____,              ____,                 ____,             ____,
        KC.LCTRL,           KC.LALT,           KC.LCMD,              KC.LSHIFT,        ____,
        ____,               ____,              ____,                 ____,             ____,
                                                                     ____,             ____,

        # RIGHT
        ____,               KC.N7,             KC.N8,                KC.N9,            ____,
        KC.LCTRL,           KC.N4,             KC.N5,                KC.N6,            ____,
        KC.N0,              KC.N1,             KC.N2,                KC.N3,            ____,
        ____,               ____,
    ],
]

keyboard.pixels.set_rgb((32, 0, 32), 0)
elapsed = time.monotonic() - start_time
print("Startup complete in %f seconds." % elapsed)

#if __name__ == '__main__':
keyboard.go()
