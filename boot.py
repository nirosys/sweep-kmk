import storage
import board
import supervisor
import digitalio
import usb_cdc
import usb_hid

# Rename our CircuitPython drive so that we can use EE Hands.
# This allows us to plug either side of the keyboard in via USB, and KMK will
# use the drive name to figure out which side is which.
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "SWEEP-L"
storage.remount("/", readonly=True)

# If during startup we see the left layer key pressed, then we'll enable the USB
# drive and serial logging. Otherwise we should keep it quiet.
debug = digitalio.DigitalInOut(board.D9)
debug.pull = digitalio.Pull.UP
if debug.value:
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)

debug.deinit()
