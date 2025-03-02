import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QFileDialog, QMenu, QWidgetAction
from PyQt5 import QtGui

from PyQt5.QtCore import Qt



class ImageViewer(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")

        # Создаем виджет для отображения изображения
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ang = 90

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

        self.rot_180 = QWidgetAction(self)
        self.rot_180.setText("&180\u00B0")

        self.rot_200 = QWidgetAction(self)
        self.rot_200.setText("&200\u00B0")



        filemenu.addAction(self.newAction)
        rotation.addAction(self.rot_90)
        rotation.addAction(self.rot_45)
        rotation.addAction(self.rot_180)
        rotation.addAction(self.rot_200)

        # Главное меню

        # Компоновка
        layout = QVBoxLayout()

        layout.addWidget(self.image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.image = None  # Для хранения загруженного изображения
        self.scale = 1.0  # Начальный масштаб
        self.standart_size = 400


    def load_image(self):
        file_name = QFileDialog.getOpenFileName(self, "Выберите BMP файл", r"C:\users\"", "Images (*.bmp)")

        if file_name:
            try:
                self.image = QtGui.QPixmap(file_name[0])
                if self.image.isNull():  # Проверяем, было ли загружено изображение
                    raise ValueError("Ошибка: не удалось загрузить изображение.")
                else:
                    self.scale = 1.0
                    self.update_image()
            except Exception as e:
                self.image_label.setText(f"Ошибка: {str(e)}")
        else:
            self.image_label.setText("Нет выбранного файла.")


    def set_scale(self, new_scale):
        self.scale = new_scale
        self.update_image()

    def rotate_90(self):
        if self.image:
            t = QtGui.QTransform().rotate(float(90))
            self.image = self.image.transformed(t, Qt.SmoothTransformation)
            self.update_image()
        # transform = QTransform().rotate(90)
        # print(1)
        # if self.image:
        #     self.image = pixmap.transfromed(transform, Qt.TransformationMode)
        # self.update_image()
    def update_image(self):
        if self.image:
            scaled_image = self.image.scaled(int(self.standart_size * self.scale), int(self.standart_size * self.scale),
                                             Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(scaled_image)
            self.resize(scaled_image.size())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Обработка ошибок при запуске
    try:
        viewer = ImageViewer()
        viewer.resize(800, 600)
        viewer.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        sys.exit(1)
