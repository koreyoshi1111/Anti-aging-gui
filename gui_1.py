# -*- coding: utf-8 -*-
import sys
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,
                             QLabel, QDesktopWidget, QMessageBox, QGraphicsOpacityEffect)  # 新增QGraphicsOpacityEffect
from PyQt5.QtGui import QFont, QPixmap, QPainter, QMovie  # 新增QMovie
from PyQt5.QtCore import Qt


class StartInterface(QWidget):
    """抗衰老活性分子筛选系统的启动界面"""

    # 配置常量
    WINDOW_TITLE = '抗衰老活性分子筛选系统'
    WINDOW_MIN_SIZE = (800, 700)
    TITLE_TEXT = "图神经网络架构下的抗衰老活性分子智能筛选平台"
    TITLE_FONT = ("Microsoft YaHei", 32, QFont.Bold)
    BUTTON_TEXT = "开始使用"
    BUTTON_FONT = ("Microsoft YaHei", 18, QFont.Bold)
    BUTTON_SIZE = (240, 70)
    BACKGROUND_OPACITY = 0.8  # 背景透明度

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """初始化用户界面（新增GIF背景处理）"""
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setMinimumSize(*self.WINDOW_MIN_SIZE)

        # ========== 新增：GIF背景动画处理 ==========
        self.background_label = QLabel(self)  # 背景标签（最底层）
        self.background_label.setScaledContents(True)  # 自动缩放适应窗口
        self.background_label.setGeometry(0, 0, self.width(), self.height())  # 初始大小
        self.background_label.lower()  # 置于最底层，确保其他组件在上层

        # 设置背景透明度（通过QGraphicsOpacityEffect实现）
        opacity_effect = QGraphicsOpacityEffect(self)
        opacity_effect.setOpacity(self.BACKGROUND_OPACITY)
        self.background_label.setGraphicsEffect(opacity_effect)

        # 加载并播放GIF
        gif_path = r'C:\Users\Wang\Desktop\Anti-aging\4.gif'
        movie = QMovie(gif_path)
        if movie.isValid():  # 检查GIF是否有效
            self.background_label.setMovie(movie)
            movie.start()  # 启动动画
        else:
            print(f"错误：GIF文件 {gif_path} 无效或路径错误！")
        # ==========================================

        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(60, 60, 60, 60)
        main_layout.setSpacing(40)

        # 添加标题
        title_label = self._create_title_label()
        main_layout.addWidget(title_label)

        # 添加开始按钮
        start_button = self._create_start_button()
        main_layout.addWidget(self._create_button_container(start_button))

        self.center_window()

    def _create_title_label(self):
        """创建标题标签"""
        label = QLabel(self.TITLE_TEXT)
        label.setFont(QFont(*self.TITLE_FONT))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            color: #00004D;  
            text-shadow: 0 0 15px white, 0 0 8px white;  
        """)
        return label

    def _create_start_button(self):
        """创建开始按钮"""
        button = QPushButton(self.BUTTON_TEXT)
        button.setFont(QFont(*self.BUTTON_FONT))
        button.setMinimumSize(*self.BUTTON_SIZE)
        button.setStyleSheet("""
            QPushButton {
                background-color: #4AB8F7; 
                color: white;
                border-radius: 35px; 
                border: 3px solid white; 
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5); 
            }
            QPushButton:hover {
                background-color: #1D6FA5;
                transform: scale(1.08);
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
            }
            QPushButton:pressed {
                background-color: #2472A4;
                transform: scale(0.95);
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
            }
        """)
        button.clicked.connect(self.open_screening_system)
        return button

    def _create_button_container(self, button):
        """创建按钮容器以确保居中显示"""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(button)
        return container

    def center_window(self):
        """将窗口居中显示在屏幕上"""
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def open_screening_system(self):
        """打开筛选系统主程序"""
        try:
            target_script = r'C:\Users\Wang\Desktop\Anti-aging\app.py'
            python_exe = sys.executable
            subprocess.Popen(
                [python_exe, target_script],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            self.close()
        except Exception as e:
            print(f"启动筛选系统失败: {str(e)}")
            QMessageBox.critical(
                self,
                "启动错误",
                f"启动筛选系统时发生错误：\n{str(e)}\n\n请检查路径是否正确，或联系开发者。"
            )


    def resizeEvent(self, event):
        """窗口大小改变时调整背景标签大小"""
        if hasattr(self, 'background_label'):
            self.background_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setFont(QFont("Microsoft YaHei", 10))
    window = StartInterface()
    window.show()
    sys.exit(app.exec_())