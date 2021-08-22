# IMPORTS
import sys
import os
import webbrowser
import json
from gui.uis.windows.main_window.functions_main_window import * # Import main window functions
from qt_core import * # Import qt core
from gui.core.json_settings import Settings # Import settings
from gui.uis.windows.main_window import * # Import main window
from gui.widgets import * # Import widgets
# ====================================================================================================


# SETUP
os.environ["QT_FONT_DPI"] = "96" # Adjust font DPI
# ====================================================================================================


# CLASSES
class MainWindow(QMainWindow): # Main window
    def __init__(self):
        super().__init__()
        
        self.ui = UI_MainWindow() # Initialize main window
        self.ui.setup_ui(self) # Load widgets from "gui\uis\main_window\ui_main.py"

        settings = Settings()
        self.settings = settings.items # Load settings
        
        self.pref = json.load(open(r'UserPref/preferences.json'))

        
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self) # Setup main window

        self.show() # Show main window

    # Handling left menu button clicks
    '''
    Run function when button is clicked
    Check funtion by object name (btn_id)
    '''
    def btn_clicked(self):
        '''Gets name of the clicked button'''
        btn = SetupMainWindow.setup_btns(self)
        
        # Logout button
        if btn.objectName() == "logout":
            print("Loging out")
        
        # Open home page
        if btn.objectName() == "btn_home":
            # Activate menu button
            self.ui.left_menu.select_only_one(btn.objectName())
            
            # Load page
            if self.pref["localId"] == None:
                MainFunctions.set_page(self, self.ui.load_pages.login_page)
            else:
                if self.pref["usertype"] == "Teacher":
                    MainFunctions.set_page(self, self.ui.load_pages.tc_home_page)
                elif self.pref["usertype"] == "Student":
                    MainFunctions.set_page(self, self.ui.load_pages.st_home_page)
        
        # Open profile page
        if btn.objectName() == "btn_profile":
            # Activate menu button
            self.ui.left_menu.select_only_one(btn.objectName())
            
            # Load page
            if self.pref["localId"] == None:
                MainFunctions.set_page(self, self.ui.load_pages.login_page)
            else:
                if self.pref["usertype"] == "Teacher":
                    MainFunctions.set_page(self, self.ui.load_pages.tc_profile_page)
                elif self.pref["usertype"] == "Student":
                    MainFunctions.set_page(self, self.ui.load_pages.st_profile_page)
        
        # Open about page
        if btn.objectName() == "btn_info":
            webbrowser.open(r"https://github.com/HarishChandran3304/foo")
        
        # Open profile page
        if btn.objectName() == "btn_profile":
            # Activate menu button
            self.ui.left_menu.select_only_one(btn.objectName())
            
            # Load page
            if self.pref["localId"] == None:
                MainFunctions.set_page(self, self.ui.load_pages.login_page)
            else:
                if self.pref["usertype"] == "Teacher":
                    MainFunctions.set_page(self, self.ui.load_pages.tc_profile_page)
                elif self.pref["usertype"] == "Student":
                    MainFunctions.set_page(self, self.ui.load_pages.st_profile_page)
        
        # Handling settings menu
        if btn.objectName() == "btn_top_settings":
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True) # Activate button
                MainFunctions.toggle_right_column(self) # Toggle right column
            else:
                btn.set_active(False) # Dectivate button
                MainFunctions.toggle_right_column(self) # Toggle right column

        print(f"Button {btn.objectName()}, clicked!") # [For debugging]

    # Handling left menu button releases
    def btn_released(self):
        btn = SetupMainWindow.setup_btns(self) # Get name of released button
        print(f"Button {btn.objectName()}, released!") # [For debugging]

    # Handling window resize
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # Handling mouse drag
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos() # Mouse drag position
# ====================================================================================================


# MAIN CALL
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
# ====================================================================================================