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
import backend.auth as auth
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
            "btn_tooltip" : "Home",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_profile.svg",
            "btn_id" : "btn_profile",
            "btn_text" : "Profile",
            "btn_tooltip" : "Profile",
            "show_top" : True,
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
            elif self.pref["usertype"] == "Student":
                MainFunctions.set_page(self, self.ui.load_pages.st_home_page)
            
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
                self.pref["name"] = self.s_name_line_edit.text()
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
        #name
        self.l_name_line_edit = QLineEdit()
        self.l_name_line_edit.setMinimumHeight(50)
        self.l_name_line_edit.setStyleSheet("border-radius: 12px; font-size: 35px; color:black;")
        self.ui.load_pages.l_name_layout.addWidget(self.l_name_line_edit)
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
                if self.pref["usertype"] == "Teacher":
                    MainFunctions.set_page(self, self.ui.load_pages.tc_home_page)
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
        
        
        # 3) Teacher Home Page
        #Next button
        def next_student():
            pass
        self.next_st_btn = PyPushButton(
            text="Next",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=35
            )
        self.next_st_btn.setMinimumHeight(50)
        self.next_st_btn.clicked.connect(next_student)
        self.ui.load_pages.next_st_layout.addWidget(self.next_st_btn)
        
        #End Class button
        def end_class():
            self.ui.load_pages.st_name_label.setText("[Start a class first]")
            pass
        self.end_cl_btn = PyPushButton(
            text="End Class",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["red"],
            bg_color_pressed=self.themes["app_color"]["red"],
            font_size=35
            )
        self.end_cl_btn.setMinimumHeight(50)
        self.end_cl_btn.clicked.connect(end_class)
        self.ui.load_pages.end_cl_layout.addWidget(self.end_cl_btn)
        
        #Start Class button
        def start_class():
            
            
            pass
        self.start_cl_btn = PyPushButton(
            text="Start Class",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["green"],
            bg_color_pressed=self.themes["app_color"]["green"],
            font_size=35
            )
        self.start_cl_btn.setMinimumHeight(50)
        self.start_cl_btn.clicked.connect(start_class)
        self.ui.load_pages.start_cl_layout.addWidget(self.start_cl_btn)
        
        
        # 4) Teacher profile page
        # Classes Table
        self.tc_table = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.tc_table.setColumnCount(3)
        self.tc_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tc_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tc_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Columns / Header
        self.tc_column_1 = QTableWidgetItem()
        self.tc_column_1.setTextAlignment(Qt.AlignCenter)
        self.tc_column_1.setText("Your Classes")
        self.tc_column_2 = QTableWidgetItem()
        self.tc_column_2.setTextAlignment(Qt.AlignCenter)
        self.tc_column_2.setText("Class Code")
        self.tc_column_3 = QTableWidgetItem()
        self.tc_column_3.setTextAlignment(Qt.AlignCenter)
        self.tc_column_3.setText("Class Strength")
        # Set column
        self.tc_table.setHorizontalHeaderItem(0, self.tc_column_1)
        self.tc_table.setHorizontalHeaderItem(1, self.tc_column_2)
        self.tc_table.setHorizontalHeaderItem(2, self.tc_column_3)
        # Populating table
        for x in range(5):
            row_number = self.tc_table.rowCount()
            self.tc_table.insertRow(row_number)
            self.class_text = QTableWidgetItem()
            self.class_text.setTextAlignment(Qt.AlignCenter)
            self.class_text.setText("CS")
            self.tc_table.setItem(row_number, 0, self.class_text)
            self.code_text = QTableWidgetItem()
            self.code_text.setTextAlignment(Qt.AlignCenter)
            self.code_text.setText("agbhrf829g")
            self.tc_table.setItem(row_number, 1, self.code_text)
            self.strength_text = QTableWidgetItem()
            self.strength_text.setTextAlignment(Qt.AlignCenter)
            self.strength_text.setText("40")
            self.tc_table.setItem(row_number, 2, self.strength_text)
            
            self.tc_table.setRowHeight(row_number, 40)
        # Add to layout
        self.ui.load_pages.tc_table_layout.addWidget(self.tc_table)
        
        # Class name input
        self.new_class = QLineEdit()
        self.new_class.setPlaceholderText("Enter class name")
        self.new_class.setMinimumHeight(50)
        self.new_class.setStyleSheet("border-radius: 12px; font-size: 25px; color:black;")
        self.ui.load_pages.new_class_layout.addWidget(self.new_class)
        
        # New class btn
        def new_class():
            pass
        self.new_class_btn = PyPushButton(
            text="Create Class",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=35
            )
        self.new_class_btn.setMinimumHeight(50)
        self.new_class_btn.clicked.connect(new_class)
        self.ui.load_pages.new_class_btn_layout.addWidget(self.new_class_btn)
        
        # View scores btn
        def view_scores():
            pass
        self.view_scores_btn = PyPushButton(
            text="View Scores",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=35
            )
        self.view_scores_btn.setMinimumHeight(50)
        self.view_scores_btn.clicked.connect(view_scores)
        self.ui.load_pages.view_scroes_layout.addWidget(self.view_scores_btn)
        
        
        # 5) Student profile page
        # Classes Table
        self.st_table = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.st_table.setColumnCount(3)
        self.st_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.st_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.st_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Columns / Header
        self.st_column_1 = QTableWidgetItem()
        self.st_column_1.setTextAlignment(Qt.AlignCenter)
        self.st_column_1.setText("Your Classes")
        self.st_column_2 = QTableWidgetItem()
        self.st_column_2.setTextAlignment(Qt.AlignCenter)
        self.st_column_2.setText("Teacher")
        self.st_column_3 = QTableWidgetItem()
        self.st_column_3.setTextAlignment(Qt.AlignCenter)
        self.st_column_3.setText("Score")
        # Set column
        self.st_table.setHorizontalHeaderItem(0, self.st_column_1)
        self.st_table.setHorizontalHeaderItem(1, self.st_column_2)
        self.st_table.setHorizontalHeaderItem(2, self.st_column_3)
        # Populating table
        for x in range(5):
            row_number = self.st_table.rowCount()
            self.st_table.insertRow(row_number)
            self.class_text = QTableWidgetItem()
            self.class_text.setTextAlignment(Qt.AlignCenter)
            self.class_text.setText("CS")
            self.st_table.setItem(row_number, 0, self.class_text)
            self.code_text = QTableWidgetItem()
            self.code_text.setTextAlignment(Qt.AlignCenter)
            self.code_text.setText("75")
            self.st_table.setItem(row_number, 1, self.code_text)
            self.strength_text = QTableWidgetItem()
            self.strength_text.setTextAlignment(Qt.AlignCenter)
            self.strength_text.setText("7")
            self.st_table.setItem(row_number, 2, self.strength_text)
            
            self.st_table.setRowHeight(row_number, 40)
        # Add to layout
        self.ui.load_pages.st_table_layout.addWidget(self.st_table)
        
        # Class code input
        self.class_code = QLineEdit()
        self.class_code.setPlaceholderText("Enter class code")
        self.class_code.setMinimumHeight(50)
        self.class_code.setStyleSheet("border-radius: 12px; font-size: 25px; color:black;")
        self.ui.load_pages.class_code_layout.addWidget(self.class_code)
        
        # Join class btn
        def join_class():
            pass
        self.join_class_btn = PyPushButton(
            text="Join Class",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=35
            )
        self.join_class_btn.setMinimumHeight(50)
        self.join_class_btn.clicked.connect(join_class)
        self.ui.load_pages.join_class_layout.addWidget(self.join_class_btn)
        
        
        # 6) Student home page
        # Choose reward combo box
        def get_rewards():
            return ["R1", "R2", "R3"]
        rews = get_rewards()
        for rew in rews:
            self.ui.load_pages.pick_reward.addItem(rew)

        # Redeem reward btn
        def redeem():
            rew = self.ui.load_pages.pick_reward.itemText()
            pass
        self.redeem_btn = PyPushButton(
            text="Redeem",
            radius=12,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["context_hover"],
            bg_color_pressed=self.themes["app_color"]["context_hover"],
            font_size=35
            )
        self.redeem_btn.setMinimumHeight(50)
        self.redeem_btn.clicked.connect(redeem)
        self.ui.load_pages.redeem_layout.addWidget(self.redeem_btn)
        
        
    def resize_grips(self): # Handle window resize
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)