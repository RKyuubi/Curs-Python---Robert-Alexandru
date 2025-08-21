class Room:
    def __init__(self, numar):
        self.numar = numar
        self.disponibila = True

    def check_in(self):
        if self.disponibila:
            self.disponibila = False
        else:
            raise Exception("Camera nu este disponibila")

    def check_out(self):
        if not self.disponibila:
            self.disponibila = True
        else:
            raise Exception("Camera nu este ocupata")