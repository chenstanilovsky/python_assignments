from SimpleFraction import SimpleFraction

class FractionTextPresenter:
    def __init__(self, fraction):
        self.fraction = fraction
        
    def draw(self):
        print(self.fraction, end=' ')

    def update_model(self, fraction):
        self.fraction = fraction
        self.update()
        
    def update(self):
        self.draw()

sf = SimpleFraction(1,1)
ftp = FractionTextPresenter(sf)
ftp.draw()
