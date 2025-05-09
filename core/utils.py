from PyQt5.QtGui import QPixmap, QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

def apply_theme(app, theme):

    pass

def set_circular_pixmap(label, image_path):
    if image_path:
        pixmap = QPixmap(image_path).scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        mask = QPixmap(50, 50)
        mask.fill(Qt.transparent)
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(0, 0, 50, 50)
        painter.end()
        pixmap.setMask(mask.createMaskFromColor(Qt.transparent))
        label.setPixmap(pixmap)
    else:
        label.setPixmap(QPixmap())

def format_speed(speed):
    if speed > 1000000:
        return f"{speed / 1000000:.2f} MB/s"
    elif speed > 1000:
        return f"{speed / 1000:.2f} KB/s"
    else:
        return f"{speed} B/s"

def format_time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h:
        return f"{int(h)}h {int(m)}m {int(s)}s"
    elif m:
        return f"{int(m)}m {int(s)}s"
    else:
        return f"{int(s)}s"
