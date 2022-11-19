
class Pojistenec:
    """ Trieda predstavuje poistenu osobu, obsahuje funkciu na inicializaciu poistenca a funkciu string na vypsanie informacii o poistencovi """
   
    '''konstruktor inicializacie pojistenca'''
    def __init__(self, jmeno, prijmeni, vek, tel_cislo): 
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    """vrati textovu reprezentaciu pojistenca"""
    def __str__(self):
        return f"{'jmeno':<6s}{self.jmeno:<12s}{'prijmeni':<9s}{self.prijmeni:<12s}{'vek':<4s}{self.vek:<5s}{'tel':<4s}{self.tel_cislo:<12s}"

          
        


       

    
