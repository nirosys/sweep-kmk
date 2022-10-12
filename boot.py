import storage
import supervisor

# Rename mount point..
storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "SWEEP-R"
storage.remount("/", readonly=True)
storage.enable_usb_drive()

supervisor.set_next_stack_limit(4096 + 4096)

