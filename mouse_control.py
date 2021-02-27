from talon import Module, actions
from talon_plugins import eye_zoom_mouse
from talon_plugins.eye_mouse import config, toggle_control

mouse_control_active = False

mod = Module()

@mod.action_class
class Actions:
    def start_mouse_control():
        """Starts mouse control"""
        global mouse_control_active
        eye_zoom_mouse.toggle_zoom_mouse(True)
        if (not mouse_control_active):
            toggle_control(not config.control_mouse)
            mouse_control_active = True
        
    def stop_mouse_control():
        """Stops mouse control"""
        global mouse_control_active
        if (mouse_control_active):
            toggle_control(False)
            mouse_control_active = False

    def mouse_move_current_gaze_position():
        """Moves the mouse to where you are currently looking at"""
        toggle_control(True)
        actions.sleep("100ms")
        toggle_control(False)

    def put_eye_tracker_to_sleep():
        """Puts eye tracker to sleep"""
        global mouse_control_active
        mouse_control_active = False
        eye_zoom_mouse.toggle_zoom_mouse(False)
        toggle_control(False)
 
        
 