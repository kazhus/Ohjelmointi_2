class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Nimi:", self.name)


class Book(Publication):
    def __init__(self, name, autor, pages):
        super().__init__(name)
        self.autor = autor
        self.pages = pages

    def print_info(self):
        super().print_info()
        print("Author:", self.autor)
        print("pages:", self.pages)


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_info(self):
        super().print_info()
        print("Chef editor:", self.chief_editor)


donald_duck = Magazine("Donald Duck", "Aki Hyypeä")
hyyti_no_6 = Book("Hyyti No. 6", "Rosa Liksom", 192)
donald_duck.print_info()
hyyti_no_6.print_info()