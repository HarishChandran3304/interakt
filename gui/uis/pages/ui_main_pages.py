# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesearqgH.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1195, 627)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"text-align: center;")
        self.tc_home_page = QWidget()
        self.tc_home_page.setObjectName(u"tc_home_page")
        self.tc_home_page.setStyleSheet(u"font-size: 14pt")
        self.tc_home_label = QLabel(self.tc_home_page)
        self.tc_home_label.setObjectName(u"tc_home_label")
        self.tc_home_label.setGeometry(QRect(-4, -1, 1181, 141))
        font = QFont()
        self.tc_home_label.setFont(font)
        self.tc_home_label.setStyleSheet(u"font-size: 100px;")
        self.tc_home_label.setAlignment(Qt.AlignCenter)
        self.st_score = QLabel(self.tc_home_page)
        self.st_score.setObjectName(u"st_score")
        self.st_score.setGeometry(QRect(0, 270, 531, 81))
        self.st_score.setFont(font)
        self.st_score.setStyleSheet(u"font-size: 50px;")
        self.st_score.setAlignment(Qt.AlignCenter)
        self.st_name = QLabel(self.tc_home_page)
        self.st_name.setObjectName(u"st_name")
        self.st_name.setGeometry(QRect(0, 160, 531, 81))
        self.st_name.setFont(font)
        self.st_name.setStyleSheet(u"font-size: 50px;")
        self.st_name.setAlignment(Qt.AlignCenter)
        self.st_name_label = QLabel(self.tc_home_page)
        self.st_name_label.setObjectName(u"st_name_label")
        self.st_name_label.setGeometry(QRect(550, 160, 531, 81))
        self.st_name_label.setFont(font)
        self.st_name_label.setStyleSheet(u"font-size: 50px;")
        self.st_name_label.setAlignment(Qt.AlignCenter)
        self.sc_1 = QRadioButton(self.tc_home_page)
        self.sc_1.setObjectName(u"sc_1")
        self.sc_1.setGeometry(QRect(590, 290, 101, 41))
        self.sc_1.setStyleSheet(u"font-size: 40px;")
        self.sc_1.setIconSize(QSize(30, 30))
        self.sc_2 = QRadioButton(self.tc_home_page)
        self.sc_2.setObjectName(u"sc_2")
        self.sc_2.setGeometry(QRect(690, 290, 101, 41))
        self.sc_2.setStyleSheet(u"font-size: 40px;")
        self.sc_2.setIconSize(QSize(30, 30))
        self.sc_3 = QRadioButton(self.tc_home_page)
        self.sc_3.setObjectName(u"sc_3")
        self.sc_3.setGeometry(QRect(790, 290, 101, 41))
        self.sc_3.setStyleSheet(u"font-size: 40px;")
        self.sc_3.setIconSize(QSize(30, 30))
        self.sc_4 = QRadioButton(self.tc_home_page)
        self.sc_4.setObjectName(u"sc_4")
        self.sc_4.setGeometry(QRect(890, 290, 101, 41))
        self.sc_4.setStyleSheet(u"font-size: 40px;")
        self.sc_4.setIconSize(QSize(30, 30))
        self.sc_5 = QRadioButton(self.tc_home_page)
        self.sc_5.setObjectName(u"sc_5")
        self.sc_5.setGeometry(QRect(990, 290, 101, 41))
        self.sc_5.setStyleSheet(u"font-size: 40px;")
        self.sc_5.setIconSize(QSize(30, 30))
        self.start_class_frame = QFrame(self.tc_home_page)
        self.start_class_frame.setObjectName(u"start_class_frame")
        self.start_class_frame.setGeometry(QRect(880, 500, 280, 80))
        self.start_class_frame.setMinimumSize(QSize(280, 80))
        self.start_class_frame.setMaximumSize(QSize(280, 80))
        self.start_class_frame.setFrameShape(QFrame.NoFrame)
        self.start_class_frame.setFrameShadow(QFrame.Raised)
        self.start_cl_layout = QVBoxLayout(self.start_class_frame)
        self.start_cl_layout.setSpacing(0)
        self.start_cl_layout.setObjectName(u"start_cl_layout")
        self.start_cl_layout.setContentsMargins(0, 0, 0, 0)
        self.tc_select_cl = QComboBox(self.tc_home_page)
        self.tc_select_cl.setObjectName(u"tc_select_cl")
        self.tc_select_cl.setGeometry(QRect(550, 510, 271, 61))
        self.tc_select_cl.setStyleSheet(u"font-size: 35px;\n"
"background-color: rgb(27, 30, 35);\n"
"color: rgb(138, 149, 170);\n"
"text-align: center;")
        self.end_class_frame = QFrame(self.tc_home_page)
        self.end_class_frame.setObjectName(u"end_class_frame")
        self.end_class_frame.setGeometry(QRect(40, 500, 280, 80))
        self.end_class_frame.setMinimumSize(QSize(280, 80))
        self.end_class_frame.setMaximumSize(QSize(280, 80))
        self.end_class_frame.setFrameShape(QFrame.NoFrame)
        self.end_class_frame.setFrameShadow(QFrame.Raised)
        self.end_cl_layout = QVBoxLayout(self.end_class_frame)
        self.end_cl_layout.setSpacing(0)
        self.end_cl_layout.setObjectName(u"end_cl_layout")
        self.end_cl_layout.setContentsMargins(0, 0, 0, 0)
        self.next_st_frame = QFrame(self.tc_home_page)
        self.next_st_frame.setObjectName(u"next_st_frame")
        self.next_st_frame.setGeometry(QRect(680, 360, 280, 80))
        self.next_st_frame.setMinimumSize(QSize(280, 80))
        self.next_st_frame.setMaximumSize(QSize(280, 80))
        self.next_st_frame.setFrameShape(QFrame.NoFrame)
        self.next_st_frame.setFrameShadow(QFrame.Raised)
        self.next_st_layout = QVBoxLayout(self.next_st_frame)
        self.next_st_layout.setSpacing(0)
        self.next_st_layout.setObjectName(u"next_st_layout")
        self.next_st_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.tc_home_page)
        self.tc_profile_page = QWidget()
        self.tc_profile_page.setObjectName(u"tc_profile_page")
        self.tc_class_select = QComboBox(self.tc_profile_page)
        self.tc_class_select.setObjectName(u"tc_class_select")
        self.tc_class_select.setGeometry(QRect(660, 540, 251, 41))
        self.tc_class_select.setStyleSheet(u"font-size: 35px;\n"
"background-color: rgb(27, 30, 35);\n"
"color: rgb(138, 149, 170);\n"
"text-align: center;")
        self.tc_profile_label = QLabel(self.tc_profile_page)
        self.tc_profile_label.setObjectName(u"tc_profile_label")
        self.tc_profile_label.setGeometry(QRect(-4, 0, 1181, 141))
        self.tc_profile_label.setFont(font)
        self.tc_profile_label.setStyleSheet(u"font-size: 100px;")
        self.tc_profile_label.setAlignment(Qt.AlignCenter)
        self.new_class_frame = QFrame(self.tc_profile_page)
        self.new_class_frame.setObjectName(u"new_class_frame")
        self.new_class_frame.setGeometry(QRect(10, 530, 250, 60))
        self.new_class_frame.setMinimumSize(QSize(250, 60))
        self.new_class_frame.setMaximumSize(QSize(250, 60))
        self.new_class_frame.setFrameShape(QFrame.NoFrame)
        self.new_class_frame.setFrameShadow(QFrame.Raised)
        self.new_class_layout = QVBoxLayout(self.new_class_frame)
        self.new_class_layout.setSpacing(0)
        self.new_class_layout.setObjectName(u"new_class_layout")
        self.new_class_layout.setContentsMargins(0, 0, 0, 0)
        self.new_class_btn_frame = QFrame(self.tc_profile_page)
        self.new_class_btn_frame.setObjectName(u"new_class_btn_frame")
        self.new_class_btn_frame.setGeometry(QRect(270, 530, 250, 60))
        self.new_class_btn_frame.setMinimumSize(QSize(250, 60))
        self.new_class_btn_frame.setMaximumSize(QSize(250, 60))
        self.new_class_btn_frame.setFrameShape(QFrame.NoFrame)
        self.new_class_btn_frame.setFrameShadow(QFrame.Raised)
        self.new_class_btn_layout = QVBoxLayout(self.new_class_btn_frame)
        self.new_class_btn_layout.setSpacing(0)
        self.new_class_btn_layout.setObjectName(u"new_class_btn_layout")
        self.new_class_btn_layout.setContentsMargins(0, 0, 0, 0)
        self.view_scores_frame = QFrame(self.tc_profile_page)
        self.view_scores_frame.setObjectName(u"view_scores_frame")
        self.view_scores_frame.setGeometry(QRect(920, 530, 250, 60))
        self.view_scores_frame.setMinimumSize(QSize(250, 60))
        self.view_scores_frame.setMaximumSize(QSize(250, 60))
        self.view_scores_frame.setFrameShape(QFrame.NoFrame)
        self.view_scores_frame.setFrameShadow(QFrame.Raised)
        self.view_scroes_layout = QVBoxLayout(self.view_scores_frame)
        self.view_scroes_layout.setSpacing(0)
        self.view_scroes_layout.setObjectName(u"view_scroes_layout")
        self.view_scroes_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget = QWidget(self.tc_profile_page)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(49, 159, 1071, 331))
        self.tc_table_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.tc_table_layout.setObjectName(u"tc_table_layout")
        self.tc_table_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.tc_profile_page)
        self.st_home_page = QWidget()
        self.st_home_page.setObjectName(u"st_home_page")
        self.tc_home_label_2 = QLabel(self.st_home_page)
        self.tc_home_label_2.setObjectName(u"tc_home_label_2")
        self.tc_home_label_2.setGeometry(QRect(0, 0, 1181, 141))
        self.tc_home_label_2.setFont(font)
        self.tc_home_label_2.setStyleSheet(u"font-size: 100px;")
        self.tc_home_label_2.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_3 = QWidget(self.st_home_page)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(190, 290, 801, 141))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.l_user_type_label_2 = QLabel(self.verticalLayoutWidget_3)
        self.l_user_type_label_2.setObjectName(u"l_user_type_label_2")
        self.l_user_type_label_2.setFont(font)
        self.l_user_type_label_2.setStyleSheet(u"font-size: 50px;")
        self.l_user_type_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.l_user_type_label_2)

        self.pick_reward = QComboBox(self.verticalLayoutWidget_3)
        self.pick_reward.setObjectName(u"pick_reward")
        self.pick_reward.setStyleSheet(u"font-size: 35px;\n"
"background-color: rgb(27, 30, 35);\n"
"color: rgb(138, 149, 170);\n"
"text-align: center;")

        self.verticalLayout_2.addWidget(self.pick_reward)

        self.l_user_type_label_3 = QLabel(self.st_home_page)
        self.l_user_type_label_3.setObjectName(u"l_user_type_label_3")
        self.l_user_type_label_3.setGeometry(QRect(0, 170, 1181, 87))
        self.l_user_type_label_3.setFont(font)
        self.l_user_type_label_3.setStyleSheet(u"font-size: 30px;")
        self.l_user_type_label_3.setAlignment(Qt.AlignCenter)
        self.redeem_frame = QFrame(self.st_home_page)
        self.redeem_frame.setObjectName(u"redeem_frame")
        self.redeem_frame.setGeometry(QRect(450, 490, 280, 80))
        self.redeem_frame.setMinimumSize(QSize(280, 80))
        self.redeem_frame.setMaximumSize(QSize(280, 80))
        self.redeem_frame.setFrameShape(QFrame.StyledPanel)
        self.redeem_frame.setFrameShadow(QFrame.Raised)
        self.redeem_layout = QVBoxLayout(self.redeem_frame)
        self.redeem_layout.setSpacing(0)
        self.redeem_layout.setObjectName(u"redeem_layout")
        self.redeem_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.st_home_page)
        self.st_profile_page = QWidget()
        self.st_profile_page.setObjectName(u"st_profile_page")
        self.st_profile_page.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(self.st_profile_page)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(49, 159, 1071, 331))
        self.st_table_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.st_table_layout.setObjectName(u"st_table_layout")
        self.st_table_layout.setContentsMargins(0, 0, 0, 0)
        self.class_code_frame = QFrame(self.st_profile_page)
        self.class_code_frame.setObjectName(u"class_code_frame")
        self.class_code_frame.setGeometry(QRect(310, 530, 250, 60))
        self.class_code_frame.setMinimumSize(QSize(250, 60))
        self.class_code_frame.setMaximumSize(QSize(250, 60))
        self.class_code_frame.setFrameShape(QFrame.NoFrame)
        self.class_code_frame.setFrameShadow(QFrame.Raised)
        self.class_code_layout = QVBoxLayout(self.class_code_frame)
        self.class_code_layout.setSpacing(0)
        self.class_code_layout.setObjectName(u"class_code_layout")
        self.class_code_layout.setContentsMargins(0, 0, 0, 0)
        self.join_class_frame = QFrame(self.st_profile_page)
        self.join_class_frame.setObjectName(u"join_class_frame")
        self.join_class_frame.setGeometry(QRect(630, 530, 250, 60))
        self.join_class_frame.setMinimumSize(QSize(250, 60))
        self.join_class_frame.setMaximumSize(QSize(250, 60))
        self.join_class_frame.setFrameShape(QFrame.NoFrame)
        self.join_class_frame.setFrameShadow(QFrame.Raised)
        self.join_class_layout = QVBoxLayout(self.join_class_frame)
        self.join_class_layout.setSpacing(0)
        self.join_class_layout.setObjectName(u"join_class_layout")
        self.join_class_layout.setContentsMargins(0, 0, 0, 0)
        self.st_profile_label = QLabel(self.st_profile_page)
        self.st_profile_label.setObjectName(u"st_profile_label")
        self.st_profile_label.setGeometry(QRect(-4, 0, 1181, 141))
        self.st_profile_label.setFont(font)
        self.st_profile_label.setStyleSheet(u"font-size: 100px;")
        self.st_profile_label.setAlignment(Qt.AlignCenter)
        self.pages.addWidget(self.st_profile_page)
        self.signup_page = QWidget()
        self.signup_page.setObjectName(u"signup_page")
        self.s_email_frame = QFrame(self.signup_page)
        self.s_email_frame.setObjectName(u"s_email_frame")
        self.s_email_frame.setGeometry(QRect(640, 270, 450, 80))
        self.s_email_frame.setMinimumSize(QSize(450, 80))
        self.s_email_frame.setMaximumSize(QSize(450, 80))
        self.s_email_frame.setStyleSheet(u"border-radius: 15")
        self.s_email_frame.setFrameShape(QFrame.NoFrame)
        self.s_email_frame.setFrameShadow(QFrame.Raised)
        self.s_email_layout = QVBoxLayout(self.s_email_frame)
        self.s_email_layout.setSpacing(0)
        self.s_email_layout.setObjectName(u"s_email_layout")
        self.s_email_layout.setContentsMargins(0, 0, 0, 0)
        self.s_pwd_frame = QFrame(self.signup_page)
        self.s_pwd_frame.setObjectName(u"s_pwd_frame")
        self.s_pwd_frame.setGeometry(QRect(640, 390, 450, 80))
        self.s_pwd_frame.setMinimumSize(QSize(450, 80))
        self.s_pwd_frame.setMaximumSize(QSize(450, 80))
        self.s_pwd_frame.setFrameShape(QFrame.NoFrame)
        self.s_pwd_frame.setFrameShadow(QFrame.Raised)
        self.s_pwd_layout = QVBoxLayout(self.s_pwd_frame)
        self.s_pwd_layout.setSpacing(0)
        self.s_pwd_layout.setObjectName(u"s_pwd_layout")
        self.s_pwd_layout.setContentsMargins(0, 0, 0, 0)
        self.s_email_label = QLabel(self.signup_page)
        self.s_email_label.setObjectName(u"s_email_label")
        self.s_email_label.setGeometry(QRect(0, 270, 641, 81))
        self.s_email_label.setFont(font)
        self.s_email_label.setStyleSheet(u"font-size: 50px;")
        self.s_email_label.setAlignment(Qt.AlignCenter)
        self.s_pwd_label = QLabel(self.signup_page)
        self.s_pwd_label.setObjectName(u"s_pwd_label")
        self.s_pwd_label.setGeometry(QRect(0, 390, 641, 81))
        self.s_pwd_label.setFont(font)
        self.s_pwd_label.setStyleSheet(u"font-size: 50px;\n"
"")
        self.s_pwd_label.setAlignment(Qt.AlignCenter)
        self.signup_label = QLabel(self.signup_page)
        self.signup_label.setObjectName(u"signup_label")
        self.signup_label.setGeometry(QRect(-4, -1, 1181, 141))
        self.signup_label.setFont(font)
        self.signup_label.setStyleSheet(u"font-size: 100px;")
        self.signup_label.setAlignment(Qt.AlignCenter)
        self.s_submit_frame = QFrame(self.signup_page)
        self.s_submit_frame.setObjectName(u"s_submit_frame")
        self.s_submit_frame.setGeometry(QRect(440, 490, 280, 80))
        self.s_submit_frame.setMinimumSize(QSize(280, 80))
        self.s_submit_frame.setMaximumSize(QSize(280, 80))
        self.s_submit_frame.setFrameShape(QFrame.StyledPanel)
        self.s_submit_frame.setFrameShadow(QFrame.Raised)
        self.s_submit_layout = QVBoxLayout(self.s_submit_frame)
        self.s_submit_layout.setSpacing(0)
        self.s_submit_layout.setObjectName(u"s_submit_layout")
        self.s_submit_layout.setContentsMargins(0, 0, 0, 0)
        self.s_user_type_label = QLabel(self.signup_page)
        self.s_user_type_label.setObjectName(u"s_user_type_label")
        self.s_user_type_label.setGeometry(QRect(0, 160, 641, 81))
        self.s_user_type_label.setFont(font)
        self.s_user_type_label.setStyleSheet(u"font-size: 50px;")
        self.s_user_type_label.setAlignment(Qt.AlignCenter)
        self.s_user_type = QComboBox(self.signup_page)
        self.s_user_type.addItem("")
        self.s_user_type.addItem("")
        self.s_user_type.setObjectName(u"s_user_type")
        self.s_user_type.setGeometry(QRect(710, 180, 311, 41))
        self.s_user_type.setStyleSheet(u"font-size: 35px;\n"
"background-color: rgb(27, 30, 35);\n"
"color: rgb(138, 149, 170);\n"
"text-align: center;")
        self.already_have_frame = QFrame(self.signup_page)
        self.already_have_frame.setObjectName(u"already_have_frame")
        self.already_have_frame.setGeometry(QRect(810, 50, 210, 60))
        self.already_have_frame.setMinimumSize(QSize(210, 60))
        self.already_have_frame.setMaximumSize(QSize(210, 60))
        self.already_have_frame.setFrameShape(QFrame.NoFrame)
        self.already_have_frame.setFrameShadow(QFrame.Raised)
        self.already_have_layout = QVBoxLayout(self.already_have_frame)
        self.already_have_layout.setSpacing(0)
        self.already_have_layout.setObjectName(u"already_have_layout")
        self.already_have_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.signup_page)
        self.signup_label.raise_()
        self.already_have_frame.raise_()
        self.s_email_frame.raise_()
        self.s_pwd_frame.raise_()
        self.s_email_label.raise_()
        self.s_pwd_label.raise_()
        self.s_submit_frame.raise_()
        self.s_user_type_label.raise_()
        self.s_user_type.raise_()
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_label = QLabel(self.login_page)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(-4, -1, 1181, 141))
        self.login_label.setFont(font)
        self.login_label.setStyleSheet(u"font-size: 100px;")
        self.login_label.setAlignment(Qt.AlignCenter)
        self.l_user_type = QComboBox(self.login_page)
        self.l_user_type.addItem("")
        self.l_user_type.addItem("")
        self.l_user_type.setObjectName(u"l_user_type")
        self.l_user_type.setGeometry(QRect(710, 180, 311, 41))
        self.l_user_type.setStyleSheet(u"font-size: 35px;\n"
"background-color: rgb(27, 30, 35);\n"
"color: rgb(138, 149, 170);\n"
"text-align: center;")
        self.l_pwd_frame = QFrame(self.login_page)
        self.l_pwd_frame.setObjectName(u"l_pwd_frame")
        self.l_pwd_frame.setGeometry(QRect(640, 390, 450, 80))
        self.l_pwd_frame.setMinimumSize(QSize(450, 80))
        self.l_pwd_frame.setMaximumSize(QSize(450, 80))
        self.l_pwd_frame.setFrameShape(QFrame.NoFrame)
        self.l_pwd_frame.setFrameShadow(QFrame.Raised)
        self.l_pwd_layout = QVBoxLayout(self.l_pwd_frame)
        self.l_pwd_layout.setSpacing(0)
        self.l_pwd_layout.setObjectName(u"l_pwd_layout")
        self.l_pwd_layout.setContentsMargins(0, 0, 0, 0)
        self.l_user_type_label = QLabel(self.login_page)
        self.l_user_type_label.setObjectName(u"l_user_type_label")
        self.l_user_type_label.setGeometry(QRect(0, 160, 641, 81))
        self.l_user_type_label.setFont(font)
        self.l_user_type_label.setStyleSheet(u"font-size: 50px;")
        self.l_user_type_label.setAlignment(Qt.AlignCenter)
        self.l_email_label_ = QLabel(self.login_page)
        self.l_email_label_.setObjectName(u"l_email_label_")
        self.l_email_label_.setGeometry(QRect(0, 270, 641, 81))
        self.l_email_label_.setFont(font)
        self.l_email_label_.setStyleSheet(u"font-size: 50px;")
        self.l_email_label_.setAlignment(Qt.AlignCenter)
        self.l_email_frame = QFrame(self.login_page)
        self.l_email_frame.setObjectName(u"l_email_frame")
        self.l_email_frame.setGeometry(QRect(640, 270, 450, 80))
        self.l_email_frame.setMinimumSize(QSize(450, 80))
        self.l_email_frame.setMaximumSize(QSize(450, 80))
        self.l_email_frame.setStyleSheet(u"border-radius: 15")
        self.l_email_frame.setFrameShape(QFrame.NoFrame)
        self.l_email_frame.setFrameShadow(QFrame.Raised)
        self.l_email_layout = QVBoxLayout(self.l_email_frame)
        self.l_email_layout.setSpacing(0)
        self.l_email_layout.setObjectName(u"l_email_layout")
        self.l_email_layout.setContentsMargins(0, 0, 0, 0)
        self.l_pwd_label = QLabel(self.login_page)
        self.l_pwd_label.setObjectName(u"l_pwd_label")
        self.l_pwd_label.setGeometry(QRect(0, 390, 641, 81))
        self.l_pwd_label.setFont(font)
        self.l_pwd_label.setStyleSheet(u"font-size: 50px;\n"
"")
        self.l_pwd_label.setAlignment(Qt.AlignCenter)
        self.dont_have_frame = QFrame(self.login_page)
        self.dont_have_frame.setObjectName(u"dont_have_frame")
        self.dont_have_frame.setGeometry(QRect(810, 50, 210, 60))
        self.dont_have_frame.setMinimumSize(QSize(210, 60))
        self.dont_have_frame.setMaximumSize(QSize(210, 60))
        self.dont_have_frame.setFrameShape(QFrame.NoFrame)
        self.dont_have_frame.setFrameShadow(QFrame.Raised)
        self.dont_have_layout = QVBoxLayout(self.dont_have_frame)
        self.dont_have_layout.setSpacing(0)
        self.dont_have_layout.setObjectName(u"dont_have_layout")
        self.dont_have_layout.setContentsMargins(0, 0, 0, 0)
        self.l_submit_frame = QFrame(self.login_page)
        self.l_submit_frame.setObjectName(u"l_submit_frame")
        self.l_submit_frame.setGeometry(QRect(440, 490, 280, 80))
        self.l_submit_frame.setMinimumSize(QSize(280, 80))
        self.l_submit_frame.setMaximumSize(QSize(280, 80))
        self.l_submit_frame.setFrameShape(QFrame.StyledPanel)
        self.l_submit_frame.setFrameShadow(QFrame.Raised)
        self.l_submit_layout = QVBoxLayout(self.l_submit_frame)
        self.l_submit_layout.setSpacing(0)
        self.l_submit_layout.setObjectName(u"l_submit_layout")
        self.l_submit_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.login_page)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.tc_home_label.setText(QCoreApplication.translate("MainPages", u"Home", None))
        self.st_score.setText(QCoreApplication.translate("MainPages", u"Score: ", None))
        self.st_name.setText(QCoreApplication.translate("MainPages", u"Student Name: ", None))
        self.st_name_label.setText(QCoreApplication.translate("MainPages", u"[Start a class first]", None))
        self.sc_1.setText(QCoreApplication.translate("MainPages", u"1", None))
        self.sc_2.setText(QCoreApplication.translate("MainPages", u"2", None))
        self.sc_3.setText(QCoreApplication.translate("MainPages", u"3", None))
        self.sc_4.setText(QCoreApplication.translate("MainPages", u"4", None))
        self.sc_5.setText(QCoreApplication.translate("MainPages", u"5", None))
        self.tc_profile_label.setText(QCoreApplication.translate("MainPages", u"Profile", None))
        self.tc_home_label_2.setText(QCoreApplication.translate("MainPages", u"Home", None))
        self.l_user_type_label_2.setText(QCoreApplication.translate("MainPages", u"Pick A Reward", None))
        self.l_user_type_label_3.setText(QCoreApplication.translate("MainPages", u"Redeem rewards with the scores that you earn from your interactions in class!", None))
        self.st_profile_label.setText(QCoreApplication.translate("MainPages", u"Profile", None))
        self.s_email_label.setText(QCoreApplication.translate("MainPages", u"Email", None))
        self.s_pwd_label.setText(QCoreApplication.translate("MainPages", u"Password", None))
        self.signup_label.setText(QCoreApplication.translate("MainPages", u"Signup", None))
        self.s_user_type_label.setText(QCoreApplication.translate("MainPages", u"User Type", None))
        self.s_user_type.setItemText(0, QCoreApplication.translate("MainPages", u"Teacher", None))
        self.s_user_type.setItemText(1, QCoreApplication.translate("MainPages", u"Student", None))

        self.login_label.setText(QCoreApplication.translate("MainPages", u"Login", None))
        self.l_user_type.setItemText(0, QCoreApplication.translate("MainPages", u"Teacher", None))
        self.l_user_type.setItemText(1, QCoreApplication.translate("MainPages", u"Student", None))

        self.l_user_type_label.setText(QCoreApplication.translate("MainPages", u"User Type", None))
        self.l_email_label_.setText(QCoreApplication.translate("MainPages", u"Email", None))
        self.l_pwd_label.setText(QCoreApplication.translate("MainPages", u"Password", None))
    # retranslateUi

