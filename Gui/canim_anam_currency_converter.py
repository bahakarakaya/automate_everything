from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text    #gets source code
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()  #only get text
    rate = float(rate[:-4])

    return rate

def show_currency():
    input_text = float(text.text())       # Kullanıcıdan metni alır
    in_curr = input_combo.currentText()   # Dropdown list'in mevcut seçimini alır
    target_curr = target_combo.currentText()
    rate = get_currency(in_curr, target_curr)
    output = round(input_text * rate, 2)
    message = f"{input_text} {in_curr}  =>  {rate} {target_curr}"
    output_label.setText(message)     # İlk harfi büyük yap, sonuna nokta koy

app = QApplication([])                  # PyQt başlatır
window = QWidget()                      # Ana pencereyi oluşturur
window.setWindowTitle('Canım Anam Para Birimi Dönüştürücü') # Pencere başlığını ayarlar

# MAIN LAYOUT
layout = QVBoxLayout()      # Arayüz öğelerini dizmek için dikey layout oluşturur. yatay için QHBoxLayout

layout1 = QHBoxLayout()
layout.addLayout(layout1)  # Child layout of Main layout

output_label = QLabel('')            # Başlangıçta boş olan bir etiket eklenir, Butona basıldığında güncellenir
layout.addWidget(output_label, alignment=Qt.AlignmentFlag.AlignLeft)

layout2 = QVBoxLayout()    # Child layout of layout1
layout1.addLayout(layout2)

layout3 = QVBoxLayout()    # Child layout of layout1
layout1.addLayout(layout3)


input_combo = QComboBox()
currencies = ['USD', 'TRY', 'EUR', 'GBP', 'CAD']
input_combo.addItems(currencies)
layout2.addWidget(input_combo)

target_combo = QComboBox()
currencies = ['USD', 'TRY', 'EUR', 'GBP', 'CAD']
target_combo.addItems(currencies)
layout2.addWidget(target_combo)


text = QLineEdit()          # Kullanıcının yazı yazacağı metin kutusu
layout3.addWidget(text)


btn = QPushButton('Convert')            # Make adında buton oluşturur
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)    # Mevcut layout'un zeminine hizalar
btn.clicked.connect(show_currency)      # Butona tıklandığında show_currency fonk çağırılır (signal-slot bağlantısı)
# Signal -> Slot (fonksiyon)    PyQt'nin temel etkileşim mekanizması


window.setLayout(layout)             # Pencereye layout'u uygular
window.show()                        # Pencereyi ekranda gösterir
app.exec()                           # Uygulamayı çalıştıran olay döngüsünü başlatır
