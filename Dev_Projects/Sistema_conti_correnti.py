
class ContoCorrente:
    def __init__(self, saldo_iniziale=0):
        self.saldo = saldo_iniziale

    def deposito(self, ammontare):
        self.saldo += ammontare
        print(f"È stato depositato {ammontare}")
        self.visualizza_saldo()
        
    def prelievo(self, ammontare):
        if self.saldo >= ammontare:
          self.saldo -= ammontare
          print(f"È stato prelevato {ammontare}")
          self.visualizza_saldo()
        else:
            print("Fondi insufficienti")

    def visualizza_saldo (self):
        print(f"Il tuo saldo attuale è :{self.saldo}")





class ContoCorrenteInteressi (ContoCorrente):
    def __init__(self, saldo_iniziale=0, tasso_interesse=0.05):
        super().__init__(saldo_iniziale)
        self.tasso_interesse = tasso_interesse

    def calcola_interessi(self):
        interessi = self.saldo * self.tasso_interesse
        print (f"Interessi maturati: {interessi}")
        self.deposito(interessi)




contoCorrente= ContoCorrenteInteressi(0)
contoCorrente.visualizza_saldo()
contoCorrente.deposito(1200)
contoCorrente.prelievo(200)
contoCorrente.calcola_interessi()