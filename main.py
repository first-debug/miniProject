import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import uic

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    static_url = 'http://static-maps.yandex.ru/1.x/'

    def __init__(self):
        super().__init__()
        self.coords = [37.530887, 55.703118]
        self.scale = 0.002
        self.map_type = 'map'
        uic.loadUi('ui.ui', self)
        self.getImage()

    def getImage(self):
        params = {
            'll': ','.join(map(str, self.coords)),
            'spn': f'{self.scale},{self.scale}',
            'l': self.map_type
        }
        response = requests.get(self.static_url, params=params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(response.url)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        pixmap = QPixmap()
        pixmap.loadFromData(response.content, 'PNG')
        self.image.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
