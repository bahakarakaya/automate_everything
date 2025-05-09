from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path


def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files')   #filenames will be a list which contains selected files abs. file paths
    message.setText('\n'.join(filenames))

def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()   #will delete the file
    message.setText('Destruction Successful!')


app = QApplication([])
window = QWidget()
window.setWindowTitle('File Destroyer')
layout = QVBoxLayout()      #MAIN LAYOUT

description = QLabel('Select the files you want to destroy. The files will be <font color="red">permanently</font> deleted')
layout.addWidget(description)


open_btn = QPushButton('Open Files')
open_btn.setToolTip('Opens file')       #shows info about the widget when holding cursor on it
open_btn.setFixedWidth(100)             #button width
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)


destroy_btn = QPushButton('Destroy Files')
destroy_btn.setToolTip('Selected files will be destroyed permanently')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)


message = QLabel()
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)


window.setLayout(layout)
window.show()
app.exec()
