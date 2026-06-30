#!/bin/python3

# importing modules
import tkinter as tk
import tkinter.ttk as ttk

import lib.main_menu as main_menu
import lib.login_system as login_system


class FrameSwitcher(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)

        # 🔹 ADD THESE 2 LINES (FULL DESKTOP SIZE)
        self.state('zoomed')              # Full screen (Windows)
        self.minsize(1200, 700)           # Prevent content cut

        self._frame = None
        # self.switch_frame(main_menu.MainMenuWindow, None)
        self.switch_frame(login_system.LoginWindow, None) 

    def switch_frame(self, frame_class, bg_frame):
        """Destroys current frame and replaces it with a new one."""    
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
            bg_frame.destroy()

            if frame_class == login_system.LoginWindow:
                # Login window should be small
                self.state("normal")
                self.resizable(1,1)
                self.geometry('700x325+333+206')
                self.resizable(0,0)
                
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)  # 🔹 IMPORTANT


if __name__ == "__main__":
    app = FrameSwitcher()
    app.mainloop()