# -*- coding: utf-8 -*-
from PyQt5 import QtCore,  QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(950, 780)

        # ========== 全局样式定义 ==========
        # 主窗口样式
        form_style = """
            QWidget#Form {
                background-color: #F0F8FF; 
                font-family: "Microsoft YaHei"; 
                font-size: 12px;
            }
        """
        Form.setStyleSheet(form_style)

        # 标签页样式
        tab_widget_style = """
            QTabWidget::pane {
                border: 1.2px solid #4682B4; 
            }
            QTabBar::tab {
                background-color: #CAE8F6; 
                color: black;            
                padding: 10px 20px;
                border: 1px solid #4682B4;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                margin-right: 3px;
                font-size: 12px; 
            }
            QTabBar::tab:selected {
                background-color: #1F8DBA;   
                color: white;
                font-size: 12px;
            }
        """

        # 组框通用样式
        groupbox_style = """
            QGroupBox {
                font-weight: normal;
                font-size: 14px;
                color: #244677;
                border: 1.2px solid #87CEEB;
                border-radius: 8px;
                margin-top: 20px;
                padding: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 10px;
            }
        """

        # 按钮通用样式
        button_style = """
            QPushButton {
                background-color: #4169E1; 
                color: white;
                border-radius: 5px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #1E90FF; 
            }
        """

        # 输入控件通用样式（含图形视图、进度条）
        edit_style = """
            QTextEdit, QTextBrowser, QComboBox, QGraphicsView {
                font-size: 14px;
                border: 1px solid #4682B4; 
                border-radius: 5px;
                padding: 4px;
                background-color: white;   
                color: #333;               
            }
 
        """

        # 复选框通用样式
        check_box_style = """
            QCheckBox {
                color: #333; 
                font-size: 16px;
            }
        """

        # ========== 标签页容器 ==========
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(30, 90, 881, 641))
        self.tabWidget.setStyleSheet(tab_widget_style)
        self.tabWidget.setObjectName("tabWidget")

        # ========== 标签页1：分子性质预测 ==========
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab.setStyleSheet("background-color: white;")

        # 组框：数据输入
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 831, 81))
        self.groupBox_3.setStyleSheet(groupbox_style)
        self.groupBox_3.setObjectName("groupBox_3")

        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(30, 40, 100, 22))
        self.label_7.setObjectName("label_7")

        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_7.setGeometry(QtCore.QRect(130, 30, 221, 41))
        self.textEdit_7.setStyleSheet(edit_style)
        self.textEdit_7.setObjectName("textEdit_7")

        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(370, 40, 100, 22))
        self.label_8.setObjectName("label_8")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(730, 35, 75, 31))
        self.pushButton_4.setStyleSheet(button_style)
        self.pushButton_4.setObjectName("pushButton_4")

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(460, 30, 256, 41))
        self.textBrowser_3.setStyleSheet(edit_style)
        self.textBrowser_3.setObjectName("textBrowser_3")

        # 组框：模型选择
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 140, 831, 81))
        self.groupBox.setStyleSheet(groupbox_style)
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 32, 101, 41))
        self.label.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(130, 35, 591, 31))
        self.comboBox.setStyleSheet(edit_style)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(740, 35, 75, 31))
        self.pushButton.setStyleSheet(button_style)
        self.pushButton.setObjectName("pushButton")

        # 组框：高级筛选
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 240, 411, 351))
        self.groupBox_2.setStyleSheet(groupbox_style)
        self.groupBox_2.setObjectName("groupBox_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 300, 71, 41))
        self.pushButton_2.setStyleSheet(button_style)
        self.pushButton_2.setObjectName("pushButton_2")

        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 331, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setStyleSheet(check_box_style)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setStyleSheet(check_box_style)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_7.setStyleSheet(check_box_style)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 3, 0, 1, 1)

        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setStyleSheet(check_box_style)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 1, 1, 1)

        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_5.setStyleSheet(check_box_style)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 2, 0, 1, 1)

        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_8.setStyleSheet(check_box_style)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 3, 1, 1, 1)

        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setStyleSheet(check_box_style)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_6.setStyleSheet(check_box_style)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 2, 1, 1, 1)

        # 组框：结果输出
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(440, 240, 411, 351))
        self.groupBox_5.setStyleSheet(groupbox_style)
        self.groupBox_5.setObjectName("groupBox_5")

        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_5)
        self.graphicsView.setGeometry(QtCore.QRect(20, 35, 371, 221))
        self.graphicsView.setStyleSheet(edit_style)
        self.graphicsView.setObjectName("graphicsView")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 260, 371, 41))
        self.textBrowser_2.setStyleSheet(edit_style)
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 310, 75, 31))
        self.pushButton_3.setStyleSheet(button_style)
        self.pushButton_3.setObjectName("pushButton_3")

        self.tabWidget.addTab(self.tab, "")

        # ========== 标签页2：分子-靶标相互作用预测 ==========
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: white;")

        # 组框：数据输入
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 20, 831, 171))
        self.groupBox_6.setStyleSheet(groupbox_style)
        self.groupBox_6.setObjectName("groupBox_6")

        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(20, 45, 121, 31))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 111, 31))
        self.label_3.setObjectName("label_3")

        self.textEdit = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit.setGeometry(QtCore.QRect(150, 40, 231, 41))
        self.textEdit.setStyleSheet(edit_style)
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit_2.setGeometry(QtCore.QRect(150, 110, 231, 41))
        self.textEdit_2.setStyleSheet(edit_style)
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(400, 50, 101, 21))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(400, 120, 101, 21))
        self.label_5.setObjectName("label_5")

        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_4.setGeometry(QtCore.QRect(500, 40, 221, 41))
        self.textBrowser_4.setStyleSheet(edit_style)
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_5.setGeometry(QtCore.QRect(500, 110, 221, 41))
        self.textBrowser_5.setStyleSheet(edit_style)
        self.textBrowser_5.setObjectName("textBrowser_5")

        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_8.setGeometry(QtCore.QRect(740, 45, 75, 31))
        self.pushButton_8.setStyleSheet(button_style)
        self.pushButton_8.setObjectName("pushButton_8")

        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_9.setGeometry(QtCore.QRect(740, 115, 75, 31))
        self.pushButton_9.setStyleSheet(button_style)
        self.pushButton_9.setObjectName("pushButton_9")

        # 组框：基于序列
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 210, 391, 141))
        self.groupBox_7.setStyleSheet(groupbox_style)
        self.groupBox_7.setObjectName("groupBox_7")

        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(15, 63, 101, 41))
        self.label_6.setObjectName("label_6")

        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 60, 191, 41))
        self.comboBox_2.setStyleSheet(edit_style)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_10.setGeometry(QtCore.QRect(320, 65, 61, 31))
        self.pushButton_10.setStyleSheet(button_style)
        self.pushButton_10.setObjectName("pushButton_10")

        # 组框：基于结构
        self.groupBox_8 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_8.setGeometry(QtCore.QRect(440, 210, 411, 141))
        self.groupBox_8.setStyleSheet(groupbox_style)
        self.groupBox_8.setObjectName("groupBox_8")

        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 111, 31))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.groupBox_8)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 91, 31))
        self.label_11.setObjectName("label_11")

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 35, 75, 31))
        self.pushButton_5.setStyleSheet(button_style)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 95, 75, 31))
        self.pushButton_6.setStyleSheet(button_style)
        self.pushButton_6.setObjectName("pushButton_6")

        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_8)
        self.textBrowser.setGeometry(QtCore.QRect(140, 30, 161, 41))
        self.textBrowser.setStyleSheet(edit_style)
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_8 = QtWidgets.QTextBrowser(self.groupBox_8)
        self.textBrowser_8.setGeometry(QtCore.QRect(140, 90, 161, 41))
        self.textBrowser_8.setStyleSheet(edit_style)
        self.textBrowser_8.setObjectName("textBrowser_8")

        # 组框：结果输出
        self.groupBox_9 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 370, 831, 221))
        self.groupBox_9.setStyleSheet(groupbox_style)
        self.groupBox_9.setObjectName("groupBox_9")

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_9)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 35, 791, 171))
        self.graphicsView_2.setStyleSheet(edit_style)
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.tabWidget.addTab(self.widget, "")

        # ========== 标签页3：抗衰老活性分子智能筛选 ==========
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab_3.setStyleSheet("background-color: white;")

        # 组框：数据上传及预处理
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 20, 831, 201))
        self.groupBox_10.setStyleSheet(groupbox_style)
        self.groupBox_10.setObjectName("groupBox_10")

        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox_10)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 30, 681, 41))
        self.textBrowser_6.setStyleSheet(edit_style)
        self.textBrowser_6.setObjectName("textBrowser_6")

        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_11.setGeometry(QtCore.QRect(730, 35, 75, 31))
        self.pushButton_11.setStyleSheet(button_style)
        self.pushButton_11.setObjectName("pushButton_11")

        self.label_15 = QtWidgets.QLabel(self.groupBox_10)
        self.label_15.setGeometry(QtCore.QRect(30, 80, 151, 31))
        self.label_15.setObjectName("label_15")

        self.progressBar = QtWidgets.QProgressBar(self.groupBox_10)
        self.progressBar.setGeometry(QtCore.QRect(30, 110, 771, 31))
        self.progressBar.setStyleSheet(edit_style)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_12.setGeometry(QtCore.QRect(360, 150, 111, 41))
        self.pushButton_12.setStyleSheet(button_style)
        self.pushButton_12.setObjectName("pushButton_12")

        # 组框：结果展示
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 240, 831, 351))
        self.groupBox_11.setStyleSheet(groupbox_style)
        self.groupBox_11.setObjectName("groupBox_11")

        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_13.setGeometry(QtCore.QRect(130, 290, 171, 41))
        self.pushButton_13.setStyleSheet(button_style)
        self.pushButton_13.setObjectName("pushButton_13")

        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox_11)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 30, 371, 251))
        self.textBrowser_7.setStyleSheet(edit_style)
        self.textBrowser_7.setObjectName("textBrowser_7")

        self.graphicsView_3 = QtWidgets.QGraphicsView(self.groupBox_11)
        self.graphicsView_3.setGeometry(QtCore.QRect(430, 30, 371, 251))
        self.graphicsView_3.setStyleSheet(edit_style)
        self.graphicsView_3.setObjectName("graphicsView_3")

        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_14.setGeometry(QtCore.QRect(530, 290, 171, 41))
        self.pushButton_14.setStyleSheet(button_style)
        self.pushButton_14.setObjectName("pushButton_14")

        self.tabWidget.addTab(self.tab_3, "")

        # ========== 标题标签 ==========
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 871, 71))
        self.label_9.setStyleSheet("""
            color: #0066cc;
            font-size: 16pt;
            font-weight: bold;
            text-align: center;
        """)
        self.label_9.setObjectName("label_9")

        # ========== 文本翻译 ==========
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图神经网络架构下的抗衰老活性分子智能筛选系统"))

        # 标签页1：分子性质预测
        self.groupBox_3.setTitle(_translate("Form", "数据输入"))
        self.label_7.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">文本输入：</span></p></body></html>"))
        self.label_8.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">文件输入：</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "浏览"))

        self.groupBox.setTitle(_translate("Form", "模型选择"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">选择模型：</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "AttentiveFP"))
        self.comboBox.setItemText(1, _translate("Form", "FE-GNN"))
        self.comboBox.setItemText(2, _translate("Form", "FP-GNN"))
        self.comboBox.setItemText(3, _translate("Form", "GCN"))
        self.comboBox.setItemText(4, _translate("Form", "GAT"))
        self.comboBox.setItemText(5, _translate("Form", "GIN"))
        self.comboBox.setItemText(6, _translate("Form", "MPNN"))
        self.comboBox.setItemText(7, _translate("Form", "GraphSAGE"))
        self.pushButton.setText(_translate("Form", "确认"))

        self.groupBox_2.setTitle(_translate("Form", "高级筛选"))
        self.pushButton_2.setText(_translate("Form", "确认"))
        self.checkBox_3.setText(_translate("Form", "分子量"))
        self.checkBox.setText(_translate("Form", "分子结构图"))
        self.checkBox_7.setText(_translate("Form", "血脑屏障通过性"))
        self.checkBox_4.setText(_translate("Form", "半衰期"))
        self.checkBox_5.setText(_translate("Form", "抗衰性"))
        self.checkBox_8.setText(_translate("Form", "血浆蛋白结合率"))
        self.checkBox_2.setText(_translate("Form", "化学式"))
        self.checkBox_6.setText(_translate("Form", "口服生物利用度"))

        self.groupBox_5.setTitle(_translate("Form", "结果输出"))
        self.pushButton_3.setText(_translate("Form", "下载结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "分子性质预测"))

        # 标签页2：分子-靶标相互作用预测
        self.groupBox_6.setTitle(_translate("Form", "数据输入"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">SMILES输入：</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">蛋白质序列：</span></p></body></html>"))
        self.label_4.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">上传文件：</span></p></body></html>"))
        self.label_5.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">上传文件：</span></p></body></html>"))
        self.pushButton_8.setText(_translate("Form", "浏览"))
        self.pushButton_9.setText(_translate("Form", "浏览"))

        self.groupBox_7.setTitle(_translate("Form", "基于序列"))
        self.label_6.setText(_translate("Form",
                                        "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">模型选择：</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Form", "BG-DTI"))
        self.comboBox_2.setItemText(1, _translate("Form", "DCHG-DTI"))
        self.comboBox_2.setItemText(2, _translate("Form", "EEGDTI"))
        self.comboBox_2.setItemText(3, _translate("Form", "DTI-HETA"))
        self.comboBox_2.setItemText(4, _translate("Form", "GCHN-DTI"))
        self.comboBox_2.setItemText(5, _translate("Form", "GSRF-DTI"))
        self.comboBox_2.setItemText(6, _translate("Form", "MSI-DTI"))
        self.comboBox_2.setItemText(7, _translate("Form", "SCGL-DTI"))
        self.comboBox_2.setItemText(8, _translate("Form", "GCN-DTI"))
        self.comboBox_2.setItemText(9, _translate("Form", "CoaDTI"))
        self.comboBox_2.setItemText(10, _translate("Form", "iNGNN-DTI"))
        self.pushButton_10.setText(_translate("Form", "确认"))

        self.groupBox_8.setTitle(_translate("Form", "基于结构"))
        self.label_10.setText(_translate("Form",
                                         "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">蛋白质文件：</span></p></body></html>"))
        self.label_11.setText(_translate("Form",
                                         "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">配体文件：</span></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "浏览"))
        self.pushButton_6.setText(_translate("Form", "浏览"))

        self.groupBox_9.setTitle(_translate("Form", "结果输出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "分子-靶标相互作用预测"))

        # 标签页3：抗衰老活性分子智能筛选
        self.groupBox_10.setTitle(_translate("Form", "数据上传及预处理"))
        self.pushButton_11.setText(_translate("Form", "浏览.."))
        self.label_15.setText(_translate("Form",
                                         "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">数据处理进度:</span></p></body></html>"))
        self.pushButton_12.setText(_translate("Form", "数据处理"))

        self.groupBox_11.setTitle(_translate("Form", "结果展示"))
        self.pushButton_13.setText(_translate("Form", "分子抗衰老性质筛选"))
        self.pushButton_14.setText(_translate("Form", "衰老相关靶标筛选"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "抗衰老活性分子智能筛选"))

        self.label_9.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#0066cc;\">图神经网络架构下的抗衰老活性分子智能筛选系统</span></p></body></html>"))