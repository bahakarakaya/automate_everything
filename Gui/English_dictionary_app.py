from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit
from PyQt6.QtCore import Qt
import requests

#TODO: adjust layout positions (QSizePolicy?)

def show_definition():
    word = input_text.text()
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)

    try:
        content = response.json()
    except Exception as e:
        output_label.setText("Could not retrieve valid data from the API.")
        return

    if isinstance(content, dict) and content.get('title') == 'No Definitions Found':
        output_label.setText(content.get("message", "No definition found."))
        return

    output = ""
    for entry in content:
        meanings = entry.get("meanings", [])
        for meaning in meanings:
            part_of_speech = meaning.get("partOfSpeech", "unknown")
            output += f"{part_of_speech.upper()}:\n"

            definitions = meaning.get("definitions", [])
            for d in definitions:
                definition_text = d.get("definition", "")
                example_text = d.get("example", "")

                output += f'  Definition:  - {definition_text}\n'
                if example_text:
                    output += f'    - Example: {example_text}\n\n'
                else:
                    output += '\n'

    output_label.setText(output)


app = QApplication([])
window = QWidget()
window.setWindowTitle("English Word Definition App")
layout = QVBoxLayout()  #MAIN LAYOUT


# ------------ LAYOUT 1 ------------
layout1 = QHBoxLayout()
layout.addLayout(layout1)

input_text = QLineEdit()
layout1.addWidget(input_text, alignment=Qt.AlignmentFlag.AlignTop)

search_btn = QPushButton('Search')
layout1.addWidget(search_btn, alignment=Qt.AlignmentFlag.AlignTop)
search_btn.clicked.connect(show_definition)


# ------------ LAYOUT 2 ------------
layout2 = QHBoxLayout()
layout.addLayout(layout2)

output_label = QLabel('')
#output_label.setFixedWidth(600)
layout2.addWidget(output_label, alignment=Qt.AlignmentFlag.AlignTop)


window.setLayout(layout)
window.show()
app.exec()