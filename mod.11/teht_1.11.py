# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi
# olla kirja tai lehti. Jokaisella julkaisulla on nimi. Kirjalla on
# lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi
# tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo
# pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6
# (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot
# toteuttamiesi metodien avulla.

class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Julkaisun nimi: {self.name}")


class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja: {self.editor} \n")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        super().print_info()
        print(f"Kirjailija: {self.author}\n"
              f"Sivut: {self.page_count}\n")


pub = []
pub.append(Magazine("Aku Ankka", "Aki Hyyppä"))
pub.append(Book("Hytti n:o 6", "Rosa Liksom", 200))

for p in pub:
    p.print_info()
