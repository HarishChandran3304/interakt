# IMPORTS
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os
from qt_core import *
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import *
from . ui_main import *
from . functions_main_window import *
import auth
import json


# CLASSES
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow() # Setup main window and load widgets
        self.ui.setup_ui(self)

    # ADD LEFT MENU BUTTONS
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_file.svg",
            "btn_id" : "btn_page_2",
            "btn_text" : "Page 2",
            "btn_tooltip" : "Open Page 2",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_save.svg",
            "btn_id" : "btn_page_3",
            "btn_text" : "Page 3",
            "btn_tooltip" : "Open Page 3",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_profile.svg",
            "btn_id" : "btn_profile",
            "btn_text" : "Profile",
            "btn_tooltip" : "Profile",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "About",
            "btn_tooltip" : "About",
            "show_top" : False,
            "is_active" : False
        }
    ]

     # ADD TITLE BAR BUTTONS
    add_title_bar_menus = [
        # {
        #     "btn_icon" : "icon_search.svg",
        #     "btn_id" : "btn_search",
        #     "btn_tooltip" : "Search",
        #     "is_active" : False
        # },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Settings",
            "is_active" : False
        }
    ]

    def setup_btns(self): # Setup buttons
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    def setup_gui(self): # Setup main window with custom title bar and menus
        self.setWindowTitle(self.settings["app_name"])
        
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)


        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus) # Add left menu buttons
        self.ui.left_menu.clicked.connect(self.btn_clicked) # Connect left menu button clicks
        self.ui.left_menu.released.connect(self.btn_released) # Connect left menu button releases

        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus) # Add title bar buttons
        self.ui.title_bar.clicked.connect(self.btn_clicked) # Connect title bar button clicks
        self.ui.title_bar.released.connect(self.btn_released) # Connect title bar button releases

        # Set title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to Interakt")

        self.ui.left_column.clicked.connect(self.btn_clicked) # Connect left column button clicks
        self.ui.left_column.released.connect(self.btn_released) # Connect left column button releases

        # Setup initial page
        self.pref = json.load(open(r'UserPref/preferences.json'))
        if self.pref["localId"] == None:
            MainFunctions.set_page(self, self.ui.load_pages.login_page)
        else:
            if self.pref["usertype"] == "Teacher":
                MainFunctions.set_page(self, self.ui.load_pages.tc_home_page)
            
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # Load settings
        settings = Settings()
        self.settings = settings.items

        # Load theme
        themes = Themes()
        self.themes = themes.items
        
        # ADDING WIDGETS TO PAGES
        # 1) Signup Page
        #email
        self.s_email_line_edit = QLineEdit()
        self.s_email_line_edit.setMinimumHeight(50)
        self.s_email_line_edit.setStyleSheet("border-radius: 12px; font-size: 35px; color:black;")
        self.ui.load_pages.s_email_layout.addWidget(self.s_email_line_edit)
        #pwd
        self.s_pwd_line_edit = QLineEdit()
        self.s_pwd_line_edit.setEchoMode(QLineEdit.Password)
        self.s_pwd_line_edit.setMinimumHeight(50)
        self.s_pwd_line_edit.setStyleSheet("border-radius: 12px; font-size: 35px; color:black;")
        self.ui.load_pages.s_pwd_layout.addWidget(self.s_pwd_line_edit)
        #submit
        def signup():
            creds = auth.sign_up(self.s_email_line_edit.text(), self.s_pwd_line_edit.text())
            if creds:
                self.pref["localId"] = creds["localId"]
                self.pref["usertype"] = self.ui.load_pages.s_user_type.currentText()
                p = json.dumps(self.pref)
                with open(r'UserPref/preferences.json', 'w') as f:
                    f.write(p)
                MainFunctions.set_page(self, self.ui.load_pages.home_page)
        self.s_submit_btn = PyPushButton(
            text="Submit",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=35
            )
        self.s_submit_btn.setMinimumHeight(50)
        self.s_submit_btn.clicked.connect(signup)
        self.ui.load_pages.s_submit_layout.addWidget(self.s_submit_btn)
        #redirect to login
        def redirect_to_login_page():
            print("Redirecting to login")
            MainFunctions.set_page(self, self.ui.load_pages.login_page)
            print("Done")
        self.already_have_btn = PyPushButton(
            text="Already have an account?\nLogin here",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=15
            )
        self.already_have_btn.setMinimumHeight(35)
        self.already_have_btn.clicked.connect(redirect_to_login_page)
        self.ui.load_pages.already_have_layout.addWidget(self.already_have_btn)
        
        
        # 2) Login Page
        #email
        self.l_email_line_edit = QLineEdit()
        self.l_email_line_edit.setMinimumHeight(50)
        self.l_email_line_edit.setStyleSheet("border-radius: 12px; font-size: 35px; color:black;")
        self.ui.load_pages.l_email_layout.addWidget(self.l_email_line_edit)
        #pwd
        self.l_pwd_line_edit = QLineEdit()
        self.l_pwd_line_edit.setEchoMode(QLineEdit.Password)
        self.l_pwd_line_edit.setMinimumHeight(50)
        self.l_pwd_line_edit.setStyleSheet("border-radius: 12px; font-size: 35px; color:black;")
        self.ui.load_pages.l_pwd_layout.addWidget(self.l_pwd_line_edit)
        #submit
        def login():
            creds = auth.log_in(self.l_email_line_edit.text(), self.l_pwd_line_edit.text())
            if creds:
                self.pref["localId"] = creds["localId"]
                self.pref["usertype"] = self.ui.load_pages.s_user_type.currentText()
                p = json.dumps(self.pref)
                with open(r'UserPref/preferences.json', 'w') as f:
                    f.write(p)
                MainFunctions.set_page(self, self.ui.load_pages.home_page)
        self.l_submit_btn = PyPushButton(
            text="Submit",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=35
            )
        self.l_submit_btn.setMinimumHeight(50)
        self.l_submit_btn.clicked.connect(login)
        self.ui.load_pages.l_submit_layout.addWidget(self.l_submit_btn)
        #redirect to signup
        def redirect_to_signup_page():
            print("Redirecting to signup")
            MainFunctions.set_page(self, self.ui.load_pages.signup_page)
            print("Done")
        self.dont_have_btn = PyPushButton(
            text="Don't have an account?\nSignup here",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=15
            )
        self.dont_have_btn.setMinimumHeight(35)
        self.dont_have_btn.clicked.connect(redirect_to_signup_page)
        self.ui.load_pages.dont_have_layout.addWidget(self.dont_have_btn)
        
        
        
        
    def resize_grips(self): # Handle window resize
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)