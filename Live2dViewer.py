import sys
import traceback as tb
import live2d.v3 as live2d
from OpenGL.GL import *
from PyQt5.QtCore import QTimer, Qt, pyqtSignal, QObject, QEvent
from PyQt5.QtGui import QDropEvent, QDragEnterEvent
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QWidget, QLineEdit, QPushButton, QVBoxLayout, QTextEdit, \
    QMessageBox, QDialog, QLabel, QHBoxLayout, QScrollArea, QMainWindow, QSlider
from functools import partial


class EditTool(QMainWindow):

    def __init__(self):
        super().__init__()

        self.resize(1500, 1000)
        self.setWindowTitle("live2d 查看器    by:PVP_yanxi  使用到了开源项目:live2d-py   严禁商用此软件")
        self.centerWidget = QWidget()
        self.setCentralWidget(self.centerWidget)

        self.mainLayout = QHBoxLayout(self.centerWidget)

        self.scrollObj = QScrollArea()
        self.scrollObj.setWidgetResizable(True)
        self.scrollWidget = QWidget()
        self.scrollObj.setWidget(self.scrollWidget)
        self.scrollLayout = QVBoxLayout(self.scrollWidget)

        self.openGl = OpenglWidget(self)  # opengl
        self.mainLayout.addWidget(self.scrollObj)  # 添加滚动条部分
        self.openGl.setMinimumWidth(self.width() // 2)
        self.mainLayout.addWidget(self.openGl)  # opengl部分
        self.scrollLayout.addStretch()

        self.loadModelPage()

    def resizeEvent(self, a0):
        self.openGl.live2dResize()

    def loadModelPage(self):
        self.clearWidgets()
        dropWidget = FileDropWidget(self.scrollWidget)
        dropWidget.resize(int(self.width() * 0.4), int(self.height() * 0.6))
        dropWidget.file_dropped.connect(self.live2dEditPage)
        self.scrollLayout.addWidget(dropWidget)

        self.scrollLayout.addWidget(self.scrollWidget)

    def live2dEditPage(self, filePath):
        self.clearWidgets()
        print(bool(self.scrollLayout))
        self.openGl.loadModel(filePath, self.scrollLayout)

    def clearWidgets(self, layout=None):
        if not layout:
            layout = self.scrollLayout
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()  # 安全删除控件
                else:
                    # 如果是子布局，递归删除
                    self.clearWidgets(item.layout())


class Parameter:

    def __init__(self, live2d: live2d.LAppModel, id: str, type: int, value: int, max: int, min: int, default: float):
        self.default = default
        self.value = value
        self.live2d = live2d
        self.id = id
        self.type = type
        self.max = max
        self.min = min

        self.id_display: QLineEdit | None = None
        self.data_display: QLineEdit | None = None

    def SetValue(self, value: int):
        self.value = value
        self.live2d.SetParameterValue(self.id, value)

    def __eq__(self, other):
        if other == self.id:
            return True
        return False

    def getValue(self):
        return self.value


class OpenglWidget(QOpenGLWidget):
    def __init__(self, parent: EditTool = None):
        super().__init__()
        self.parent = parent
        self.backgroundColor = [0, 0, 0, 0]
        self.live2d: live2d.LAppModel | None = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.__update)
        self.parameters = []


    def live2dResize(self):
        if self.live2d:
            self.live2d.Resize(int(self.width()), int(self.height()))


    def loadModel(self, filePath, scrollLayout: QWidget):
        if live2d.LIVE2D_VERSION == 3:
            live2d.glInit()

        self.live2d: live2d.LAppModel = live2d.LAppModel()
        self.live2d.LoadModelJson(str(filePath))
        self.live2d.Resize(int(self.width()), int(self.height()))
        self.timer.start(16)

        try:
            for i in range(self.live2d.GetParameterCount()):
                args = {"live2d": self.live2d}
                for name in ["id", 'type', 'value', 'max', 'min', 'default']:
                    args[name] = getattr(self.live2d.GetParameter(i), name)
                obj = Parameter(**args)

                _mainWidget = QWidget()
                _mainLayout = QHBoxLayout(_mainWidget)

                _parameterName = QLineEdit()
                _parameterName.setReadOnly(True)
                _parameterName.setText(args["id"])

                _slider = QSlider(Qt.Horizontal)
                _slider.setRange(int(args["min"]), int(args["max"]))
                _slider.setValue(int(args["default"]))

                _slider.valueChanged.connect(partial(obj.SetValue))
                _mainLayout.addWidget(_parameterName)
                _mainLayout.addWidget(_slider)
                _mainLayout.addStretch()
                self.parameters.append(obj)
                scrollLayout.addWidget(_mainWidget)


        except Exception as e:
            print(f"{e}\n{tb.format_exc()}")

    def initializeGL(self):
        glEnable(GL_BLEND)
        glClearColor(*self.backgroundColor)

    def paintGL(self):
        glClearColor(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT)
        if self.live2d:
            self.live2d.Draw()

    def __update(self):
        self.live2d.Update()
        self.update()


class FileDropWidget(QWidget):
    """自定义文件拖放部件"""
    # 定义信号，当文件被拖入时发射
    file_dropped = pyqtSignal(str)  # 发射文件路径

    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置接受拖放
        self.setAcceptDrops(True)

        # 设置最小尺寸
        self.setMinimumSize(200, 150)
        self.setStyleSheet("""
        border: 2px dashed #aaa;""")
        # 创建布局和标签
        layout = QVBoxLayout(self)
        self.label = QLabel("拖放文件到此处\n(xxx.model3.json)")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px;")
        layout.addWidget(self.label)

        # 文件路径标签
        self.file_label = QLabel("")
        self.file_label.setAlignment(Qt.AlignCenter)
        self.file_label.setWordWrap(True)
        self.file_label.setStyleSheet("font-size: 20px; padding-top: 10px;")
        layout.addWidget(self.file_label)

    def dragEnterEvent(self, event: QDragEnterEvent):
        """拖拽进入事件"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            # 改变样式表示可以放置
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        """拖拽离开事件"""
        pass

    def dropEvent(self, event: QDropEvent):
        """放置事件"""

        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                # 获取第一个文件的绝对路径
                file_path = urls[0].toLocalFile()

                # 显示文件名
                self.label.setText("已选择文件:")
                self.file_label.setText(file_path)

                # 发射信号
                self.file_dropped.emit(file_path)

                event.acceptProposedAction()
        else:
            event.ignore()

    def clear(self):
        """清空显示"""
        self.label.setText("拖放文件到此处")
        self.file_label.setText("")


if __name__ == '__main__':
    try:
        live2d.init()
        app = QApplication(sys.argv)
        window = EditTool()
        window.show()
        app.exec_()
    except Exception as e:
        print(f"{e}\n{tb.format_exc()}")

