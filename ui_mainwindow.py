# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 718)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(-1, -1, 30, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_time_elapsed = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(12)
        self.label_time_elapsed.setFont(font)
        self.label_time_elapsed.setObjectName(_fromUtf8("label_time_elapsed"))
        self.gridLayout_2.addWidget(self.label_time_elapsed, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.progressBar_total = QtGui.QProgressBar(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_total.sizePolicy().hasHeightForWidth())
        self.progressBar_total.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(12)
        self.progressBar_total.setFont(font)
        self.progressBar_total.setStyleSheet(_fromUtf8(""))
        self.progressBar_total.setMaximum(1000)
        self.progressBar_total.setProperty("value", 0)
        self.progressBar_total.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_total.setFormat(_fromUtf8(""))
        self.progressBar_total.setObjectName(_fromUtf8("progressBar_total"))
        self.gridLayout_2.addWidget(self.progressBar_total, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.progressBar_current = QtGui.QProgressBar(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_current.sizePolicy().hasHeightForWidth())
        self.progressBar_current.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(12)
        self.progressBar_current.setFont(font)
        self.progressBar_current.setStyleSheet(_fromUtf8("/*\n"
"QProgressBar {\n"
"    border: 2px solid gray;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgba(0, 200, 0);\n"
"    width: 1px;\n"
"}*/"))
        self.progressBar_current.setMaximum(1000)
        self.progressBar_current.setProperty("value", 0)
        self.progressBar_current.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_current.setFormat(_fromUtf8(""))
        self.progressBar_current.setObjectName(_fromUtf8("progressBar_current"))
        self.gridLayout_2.addWidget(self.progressBar_current, 2, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setMargin(30)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_start = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.verticalLayout_2.addWidget(self.pushButton_start)
        self.pushButton_cancel = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_cancel.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.verticalLayout_2.addWidget(self.pushButton_cancel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_config = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_config.sizePolicy().hasHeightForWidth())
        self.groupBox_config.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_config.setFont(font)
        self.groupBox_config.setStyleSheet(_fromUtf8("QGroupBox{border:1px ridge gray;margin-top: 1ex;} QGroupBox::title{subcontrol-origin: margin;subcontrol-position:top center;padding:0 3px;}"))
        self.groupBox_config.setFlat(False)
        self.groupBox_config.setCheckable(False)
        self.groupBox_config.setObjectName(_fromUtf8("groupBox_config"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_config)
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.groupBox_config)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.radioButton_google = QtGui.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_google.setFont(font)
        self.radioButton_google.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_google.setChecked(True)
        self.radioButton_google.setObjectName(_fromUtf8("radioButton_google"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButton_google)
        self.horizontalLayout.addWidget(self.radioButton_google)
        self.radioButton_bing = QtGui.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_bing.setFont(font)
        self.radioButton_bing.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_bing.setObjectName(_fromUtf8("radioButton_bing"))
        self.buttonGroup.addButton(self.radioButton_bing)
        self.horizontalLayout.addWidget(self.radioButton_bing)
        self.radioButton_baidu = QtGui.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_baidu.setFont(font)
        self.radioButton_baidu.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButton_baidu.setObjectName(_fromUtf8("radioButton_baidu"))
        self.buttonGroup.addButton(self.radioButton_baidu)
        self.horizontalLayout.addWidget(self.radioButton_baidu)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtGui.QWidget(self.groupBox_config)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout = QtGui.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_keywords = QtGui.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_keywords.setFont(font)
        self.lineEdit_keywords.setWhatsThis(_fromUtf8(""))
        self.lineEdit_keywords.setInputMask(_fromUtf8(""))
        self.lineEdit_keywords.setObjectName(_fromUtf8("lineEdit_keywords"))
        self.gridLayout.addWidget(self.lineEdit_keywords, 0, 1, 1, 2)
        self.checkBox_from_file = QtGui.QCheckBox(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_from_file.sizePolicy().hasHeightForWidth())
        self.checkBox_from_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.checkBox_from_file.setFont(font)
        self.checkBox_from_file.setObjectName(_fromUtf8("checkBox_from_file"))
        self.gridLayout.addWidget(self.checkBox_from_file, 1, 0, 1, 1)
        self.lineEdit_path2file = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_path2file.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_path2file.setFont(font)
        self.lineEdit_path2file.setObjectName(_fromUtf8("lineEdit_path2file"))
        self.gridLayout.addWidget(self.lineEdit_path2file, 1, 1, 1, 1)
        self.pushButton_load_file = QtGui.QPushButton(self.widget_2)
        self.pushButton_load_file.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load_file.sizePolicy().hasHeightForWidth())
        self.pushButton_load_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_load_file.setFont(font)
        self.pushButton_load_file.setObjectName(_fromUtf8("pushButton_load_file"))
        self.gridLayout.addWidget(self.pushButton_load_file, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout.setColumnStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_6 = QtGui.QWidget(self.groupBox_config)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_7 = QtGui.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_5.addWidget(self.label_7)
        self.lineEdit_output = QtGui.QLineEdit(self.widget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_output.sizePolicy().hasHeightForWidth())
        self.lineEdit_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_output.setFont(font)
        self.lineEdit_output.setInputMask(_fromUtf8(""))
        self.lineEdit_output.setObjectName(_fromUtf8("lineEdit_output"))
        self.horizontalLayout_5.addWidget(self.lineEdit_output)
        self.pushButton_output = QtGui.QPushButton(self.widget_6)
        self.pushButton_output.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_output.sizePolicy().hasHeightForWidth())
        self.pushButton_output.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_output.setFont(font)
        self.pushButton_output.setObjectName(_fromUtf8("pushButton_output"))
        self.horizontalLayout_5.addWidget(self.pushButton_output)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 6)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_3 = QtGui.QWidget(self.groupBox_config)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBox_face_only = QtGui.QCheckBox(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_face_only.sizePolicy().hasHeightForWidth())
        self.checkBox_face_only.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_face_only.setFont(font)
        self.checkBox_face_only.setObjectName(_fromUtf8("checkBox_face_only"))
        self.horizontalLayout_4.addWidget(self.checkBox_face_only)
        self.checkBox_safe_mode = QtGui.QCheckBox(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_safe_mode.sizePolicy().hasHeightForWidth())
        self.checkBox_safe_mode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_safe_mode.setFont(font)
        self.checkBox_safe_mode.setCheckable(True)
        self.checkBox_safe_mode.setChecked(True)
        self.checkBox_safe_mode.setObjectName(_fromUtf8("checkBox_safe_mode"))
        self.horizontalLayout_4.addWidget(self.checkBox_safe_mode)
        self.label_6 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.spinBox_max_number = QtGui.QSpinBox(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_max_number.sizePolicy().hasHeightForWidth())
        self.spinBox_max_number.setSizePolicy(sizePolicy)
        self.spinBox_max_number.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_max_number.setFont(font)
        self.spinBox_max_number.setMinimum(1)
        self.spinBox_max_number.setMaximum(2000)
        self.spinBox_max_number.setProperty("value", 100)
        self.spinBox_max_number.setObjectName(_fromUtf8("spinBox_max_number"))
        self.horizontalLayout_4.addWidget(self.spinBox_max_number)
        self.label_5 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spinBox_num_threads = QtGui.QSpinBox(self.widget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_num_threads.sizePolicy().hasHeightForWidth())
        self.spinBox_num_threads.setSizePolicy(sizePolicy)
        self.spinBox_num_threads.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_num_threads.setFont(font)
        self.spinBox_num_threads.setMinimum(1)
        self.spinBox_num_threads.setMaximum(200)
        self.spinBox_num_threads.setProperty("value", 50)
        self.spinBox_num_threads.setObjectName(_fromUtf8("spinBox_num_threads"))
        self.horizontalLayout_4.addWidget(self.spinBox_num_threads)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(4, 1)
        self.horizontalLayout_4.setStretch(5, 1)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtGui.QWidget(self.groupBox_config)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox_proxy = QtGui.QCheckBox(self.widget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_proxy.sizePolicy().hasHeightForWidth())
        self.checkBox_proxy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_proxy.setFont(font)
        self.checkBox_proxy.setObjectName(_fromUtf8("checkBox_proxy"))
        self.horizontalLayout_2.addWidget(self.checkBox_proxy)
        self.widget_5 = QtGui.QWidget(self.widget_4)
        self.widget_5.setEnabled(False)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_http = QtGui.QRadioButton(self.widget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_http.sizePolicy().hasHeightForWidth())
        self.radioButton_http.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_http.setFont(font)
        self.radioButton_http.setFocusPolicy(QtCore.Qt.TabFocus)
        self.radioButton_http.setChecked(True)
        self.radioButton_http.setObjectName(_fromUtf8("radioButton_http"))
        self.buttonGroup_2 = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.radioButton_http)
        self.horizontalLayout_3.addWidget(self.radioButton_http)
        self.radioButton_socks5 = QtGui.QRadioButton(self.widget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_socks5.sizePolicy().hasHeightForWidth())
        self.radioButton_socks5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_socks5.setFont(font)
        self.radioButton_socks5.setFocusPolicy(QtCore.Qt.TabFocus)
        self.radioButton_socks5.setChecked(False)
        self.radioButton_socks5.setObjectName(_fromUtf8("radioButton_socks5"))
        self.buttonGroup_2.addButton(self.radioButton_socks5)
        self.horizontalLayout_3.addWidget(self.radioButton_socks5)
        self.lineEdit_proxy = QtGui.QLineEdit(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_proxy.setFont(font)
        self.lineEdit_proxy.setObjectName(_fromUtf8("lineEdit_proxy"))
        self.horizontalLayout_3.addWidget(self.lineEdit_proxy)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 4)
        self.horizontalLayout_2.addWidget(self.widget_5)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)
        self.gridLayout_3.addWidget(self.groupBox_config, 0, 0, 1, 1)
        self.plainTextEdit_log = QtGui.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        self.plainTextEdit_log.setFont(font)
        self.plainTextEdit_log.setReadOnly(True)
        self.plainTextEdit_log.setPlainText(_fromUtf8(""))
        self.plainTextEdit_log.setTabStopWidth(4)
        self.plainTextEdit_log.setMaximumBlockCount(0)
        self.plainTextEdit_log.setObjectName(_fromUtf8("plainTextEdit_log"))
        self.gridLayout_3.addWidget(self.plainTextEdit_log, 2, 0, 1, 2)
        self.gridLayout_3.setColumnStretch(0, 8)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setRowStretch(0, 7)
        self.gridLayout_3.setRowStretch(1, 3)
        self.gridLayout_3.setRowStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.label.setBuddy(self.lineEdit_keywords)
        self.label_7.setBuddy(self.lineEdit_output)
        self.label_6.setBuddy(self.spinBox_max_number)
        self.label_5.setBuddy(self.spinBox_num_threads)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.checkBox_from_file, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_keywords.setDisabled)
        QtCore.QObject.connect(self.checkBox_from_file, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButton_load_file.setEnabled)
        QtCore.QObject.connect(self.checkBox_from_file, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_path2file.setEnabled)
        QtCore.QObject.connect(self.checkBox_proxy, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.widget_5.setEnabled)
        QtCore.QObject.connect(self.checkBox_proxy, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lineEdit_proxy.setFocus)
        QtCore.QObject.connect(self.radioButton_google, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkBox_safe_mode.setEnabled)
        QtCore.QObject.connect(self.radioButton_bing, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkBox_safe_mode.setChecked)
        QtCore.QObject.connect(self.radioButton_baidu, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkBox_safe_mode.setChecked)
        QtCore.QObject.connect(self.radioButton_google, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkBox_safe_mode.setChecked)
        QtCore.QObject.connect(self.checkBox_from_file, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButton_load_file.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_keywords, self.checkBox_from_file)
        MainWindow.setTabOrder(self.checkBox_from_file, self.lineEdit_path2file)
        MainWindow.setTabOrder(self.lineEdit_path2file, self.pushButton_load_file)
        MainWindow.setTabOrder(self.pushButton_load_file, self.lineEdit_output)
        MainWindow.setTabOrder(self.lineEdit_output, self.pushButton_output)
        MainWindow.setTabOrder(self.pushButton_output, self.checkBox_face_only)
        MainWindow.setTabOrder(self.checkBox_face_only, self.checkBox_safe_mode)
        MainWindow.setTabOrder(self.checkBox_safe_mode, self.spinBox_max_number)
        MainWindow.setTabOrder(self.spinBox_max_number, self.spinBox_num_threads)
        MainWindow.setTabOrder(self.spinBox_num_threads, self.checkBox_proxy)
        MainWindow.setTabOrder(self.checkBox_proxy, self.radioButton_http)
        MainWindow.setTabOrder(self.radioButton_http, self.radioButton_socks5)
        MainWindow.setTabOrder(self.radioButton_socks5, self.lineEdit_proxy)
        MainWindow.setTabOrder(self.lineEdit_proxy, self.pushButton_start)
        MainWindow.setTabOrder(self.pushButton_start, self.pushButton_cancel)
        MainWindow.setTabOrder(self.pushButton_cancel, self.radioButton_google)
        MainWindow.setTabOrder(self.radioButton_google, self.radioButton_bing)
        MainWindow.setTabOrder(self.radioButton_bing, self.radioButton_baidu)
        MainWindow.setTabOrder(self.radioButton_baidu, self.plainTextEdit_log)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Progress", None))
        self.label_4.setText(_translate("MainWindow", "Time Elapsed:", None))
        self.label_time_elapsed.setText(_translate("MainWindow", "00:00:00", None))
        self.label_2.setText(_translate("MainWindow", "Total Progress:", None))
        self.label_3.setText(_translate("MainWindow", "Current Progress:", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Control", None))
        self.pushButton_start.setText(_translate("MainWindow", "Start", None))
        self.pushButton_start.setShortcut(_translate("MainWindow", "Return", None))
        self.pushButton_cancel.setText(_translate("MainWindow", "&Cancle", None))
        self.groupBox_config.setTitle(_translate("MainWindow", "Config", None))
        self.radioButton_google.setText(_translate("MainWindow", "&Google", None))
        self.radioButton_bing.setText(_translate("MainWindow", "&Bing", None))
        self.radioButton_baidu.setText(_translate("MainWindow", "B&aidu", None))
        self.label.setText(_translate("MainWindow", "&Keywords:", None))
        self.lineEdit_keywords.setToolTip(_translate("MainWindow", "Input keywords, seperated by comma  \", \"", None))
        self.lineEdit_keywords.setStatusTip(_translate("MainWindow", "Hint: e.g. To download image of Micheal Jordan and Yao Ming, input \"Micheal Jordan, Yao Ming\"", None))
        self.lineEdit_keywords.setPlaceholderText(_translate("MainWindow", "Seperates by comma ( , )", None))
        self.checkBox_from_file.setText(_translate("MainWindow", "&Load File:", None))
        self.lineEdit_path2file.setStatusTip(_translate("MainWindow", "Hint: Enter path to a text file. Each line of the file contains a group of keywords", None))
        self.lineEdit_path2file.setPlaceholderText(_translate("MainWindow", "Path to file", None))
        self.pushButton_load_file.setText(_translate("MainWindow", "...", None))
        self.label_7.setText(_translate("MainWindow", "&Output:", None))
        self.lineEdit_output.setToolTip(_translate("MainWindow", "Path to output directory.", None))
        self.lineEdit_output.setStatusTip(_translate("MainWindow", "Path to output directory.", None))
        self.lineEdit_output.setText(_translate("MainWindow", "./download_images", None))
        self.lineEdit_output.setPlaceholderText(_translate("MainWindow", "Path to output directory.", None))
        self.pushButton_output.setText(_translate("MainWindow", "...", None))
        self.checkBox_face_only.setText(_translate("MainWindow", "&Face Only", None))
        self.checkBox_safe_mode.setText(_translate("MainWindow", "&Safe Mode", None))
        self.label_6.setText(_translate("MainWindow", "Max &number\n"
"per keywords", None))
        self.label_5.setText(_translate("MainWindow", "&Threads:", None))
        self.checkBox_proxy.setText(_translate("MainWindow", "&Proxy:", None))
        self.radioButton_http.setText(_translate("MainWindow", "HTTP", None))
        self.radioButton_socks5.setText(_translate("MainWindow", "Socks5", None))
        self.lineEdit_proxy.setToolTip(_translate("MainWindow", "input ip:port", None))
        self.lineEdit_proxy.setStatusTip(_translate("MainWindow", "xxx.xxx.xxx.xx:port", None))
        self.lineEdit_proxy.setPlaceholderText(_translate("MainWindow", "xxx.xxx.xxx.xx:port", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

