class Car:
    def __init__(self, TyreFL, TyreFR, TyreRL, TyreRR):
        self.TyreFL = TyreFL
        self.TyreFR = TyreFR
        self.TyreRL = TyreRL
        self.TyreRR = TyreRR

    def view_tyres(self):
        tyres = [self.TyreFL.view_tyre()[-1].copy(), self.TyreFR.view_tyre()
                 [-1].copy(), self.TyreRL.view_tyre()[-1].copy(), self.TyreRR.view_tyre()[-1].copy()]
        tyres[0]["position"] = "FL"
        tyres[1]["position"] = "FR"
        tyres[2]["position"] = "RL"
        tyres[3]["position"] = "RR"
        return tyres


class Tyre:
    def __init__(self, initial_record):
        self.history = [initial_record]

    def view_tyre(self):
        return self.history

    def record(self, record):
        self.history.append(record)
