# Put mouse to gaze position
# Triggered via Karabiner Elements via: `Tab + Left Command`
# ---------------------------------------------------------------------
key(cmd-ctrl-j):
    user.move_mouse_to_current_gaze_position()


# Enable mouse control
# Triggered via Karabiner Elements via: `Tab + Left Command (hold)`
# ---------------------------------------------------------------------
key(f13):
    user.start_mouse_control()
key(cmd-f13):
    user.start_mouse_control()    

# Disable mouse control
# Triggered via Karabiner Elements via: `Tab + Left Command (release)`
# ---------------------------------------------------------------------
key(f14):
    user.stop_mouse_control()    
key(cmd-f14):
    user.stop_mouse_control()    


# Put eye tracker to sleep
# Triggered via Karabiner Elements via: `Tab + Left Command + Backspace`
# ---------------------------------------------------------------------
#key(cmd-ctrl-alt-backspace):
#    user.put_eye_tracker_to_sleep()
