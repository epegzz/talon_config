# My Talon config

This is my own custom Talon config. Currently only used to support eye tracking 
mouse control via keyboard shortcuts.

## Current features:

- Function to enable mouse control via eye tracker (continuously move mouse to where you look at on the screen):

  `user.start_mouse_control`
  

- Function to enable mouse control via eye tracker (stop updating mouse position):

  `user.stop_mouse_control`

- Function to put the mouse to the position on the screen that you are looking at once:

  `user.move_mouse_to_current_gaze_position`

- Function to put eye tracker to sleep:

  `user.put_eye_tracker_to_sleep`

- Puts eye tracker to sleep automatically after 15 minutes

## Linux & Mac setup

Clone repo into `~/.talon/user`

```insert code:
cd ~/.talon/user
git clone git@github.com:epegzz/talon_config.git epegzz_talon
```
   

# Talon documentation
For up-to-date documentation on Talon's API and features, please visit https://talon.wiki/. 

https://talon.wiki/unofficial_talon_docs/ is a great place to learn about Talon files, actions, and voice command definitions.
