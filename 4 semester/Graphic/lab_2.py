import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFileDialog, QMenu, QWidgetAction, QScrollArea
from PyQt5 import QtGui
from PyQt5.QtCore import Qt



class ImageRotator(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Rotator")

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flag = False

        menubar = self.menuBar()
        filemenu = QMenu("&Файл", self)
        menubar.addMenu(filemenu)

        rotation = QMenu("&Поворот по часовой стрелке", self)
        menubar.addMenu(rotation)

        self.newAction = QWidgetAction(self)
        self.newAction.setText("&Загрузить")
        self.newAction.triggered.connect(self.load_image)

        self.rot_90 = QWidgetAction(self)
        self.rot_90.setText("&90\u00B0")
        self.rot_90.triggered.connect(self.rotate_90)

        self.rot_45 = QWidgetAction(self)
        self.rot_45.setText("&45\u00B0")
        self.rot_45.triggered.connect(self.rotate_45)

        self.rot_180 = QWidgetAction(self)
        self.rot_180.setText("&180\u00B0")
        self.rot_180.triggered.connect(self.rotate_180)

        self.rot_200 = QWidgetAction(self)
        self.rot_200.setText("&200\u00B0")
        self.rot_200.triggered.connect(self.rotate_200)



        filemenu.addAction(self.newAction)
        rotation.addAction(self.rot_90)
        rotation.addAction(self.rot_45)
        rotation.addAction(self.rot_180)
        rotation.addAction(self.rot_200)

        layout = QVBoxLayout()


        scroll = QScrollArea(self)
        layout.addWidget(scroll)
        scroll.setWidgetResizable(True)

        scroll.setWidget(self.image_label)




        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.image = None
        self.image_size = 400


    def load_image(self):
        file = QFileDialog.getOpenFileName(self, "Выберите BMP файл", r"C:\users\"", "Images (*.bmp)")

        if file:
            try:
                self.image = QtGui.QPixmap(file[0])
                if self.image.isNull():
                    raise ValueError("Не удалось загрузить изображение.")
                else:
                    self.image_label.setPixmap(self.image)
                    self.showMaximized()
            except Exception as e:
                self.image_label.setText(f"Ошибка: {str(e)}")
        else:
            self.image_label.setText("Нет выбранного файла.")



    def rotate_90(self):
        if self.image:
            t = QtGui.QTransform().rotate(float(90))
            self.image = self.image.transformed(t, Qt.SmoothTransformation)
            self.update_image()
            if self.flag is False:
                self.showMaximized()
                self.flag = True
    def rotate_45(self):
        if self.image:
            t = QtGui.QTransform().rotate(float(45))
            self.image = self.image.transformed(t, Qt.SmoothTransformation)
            self.update_image()
    def rotate_180(self):
        if self.image:
            t = QtGui.QTransform().rotate(float(180))
            self.image = self.image.transformed(t, Qt.SmoothTransformation)
            self.update_image()
    def rotate_200(self):
        if self.image:
            t = QtGui.QTransform().rotate(float(200))
            self.image = self.image.transformed(t, Qt.SmoothTransformation)
            self.update_image()

    def update_image(self):
        self.image_label.setPixmap(self.image)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        viewer = ImageRotator()
        viewer.resize(800, 600)
        viewer.show()
        sys.exit(app.exec())
    except Exception as error:
        print(f"Произошла ошибка: {str(error)}")
        sys.exit(1)
