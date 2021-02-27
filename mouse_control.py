from talon import Module, actions
from talon_plugins import eye_zoom_mouse
from talon_plugins.eye_mouse import config, toggle_control

import threading
from functools import wraps


mouse_control_active = False
put_eye_tracker_to_sleep_timer = None
eye_tracker_sleep_timer_delay = 60 * 15 # 15 mins


mod = Module()

@mod.action_class
class Actions:
    def start_mouse_control():
        """Starts mouse control"""
        global mouse_control_active
        global eye_tracker_sleep_timer_delay

        schedule_putting_eye_tracker_to_sleep(eye_tracker_sleep_timer_delay)

        eye_zoom_mouse.toggle_zoom_mouse(True)
        if (not mouse_control_active):
            toggle_control(not config.control_mouse)
            mouse_control_active = True
        
    def stop_mouse_control():
        """Stops mouse control"""
        global mouse_control_active
        global eye_tracker_sleep_timer_delay

        schedule_putting_eye_tracker_to_sleep(eye_tracker_sleep_timer_delay)

        if (mouse_control_active):
            toggle_control(False)
            mouse_control_active = False

    def move_mouse_to_current_gaze_position():
        """Moves the mouse to where you are currently looking at"""
        global eye_tracker_sleep_timer_delay

        schedule_putting_eye_tracker_to_sleep(eye_tracker_sleep_timer_delay)

        toggle_control(True)
        actions.sleep("100ms")
        toggle_control(False)

    def put_eye_tracker_to_sleep():
        """Puts eye tracker to sleep"""
        schedule_putting_eye_tracker_to_sleep()
 

def schedule_putting_eye_tracker_to_sleep(seconds=0.):
    global put_eye_tracker_to_sleep_timer

    if (put_eye_tracker_to_sleep_timer):
        put_eye_tracker_to_sleep_timer.clearTimeout()
        put_eye_tracker_to_sleep_timer = None

    def doIt():
        global mouse_control_active
        global put_eye_tracker_to_sleep_timer

        mouse_control_active = False
        eye_zoom_mouse.toggle_zoom_mouse(False)
        toggle_control(False)
        if (put_eye_tracker_to_sleep_timer):
            put_eye_tracker_to_sleep_timer.clearTimeout()
            put_eye_tracker_to_sleep_timer = None

    
    put_eye_tracker_to_sleep_timer = Timer()
    put_eye_tracker_to_sleep_timer.setTimeout(doIt, seconds)
 

def delay(delay=0.):
    """
    Decorator delaying the execution of a function for a while.
    """
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args=args, kwargs=kwargs)
            timer.start()
        return delayed
    return wrap


class Timer():
    toClearTimer = False
    def setTimeout(self, fn, time):
        isInvokationCancelled = False

        @delay(time)
        def some_fn():
            if (self.toClearTimer is False):
                fn()

        some_fn()
        return isInvokationCancelled
    def clearTimeout(self):
        self.toClearTimer = True
