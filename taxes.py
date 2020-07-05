from databank import Databank


class Calc:

    def __init__(self):
        self.db = Databank()

    def fee_inss(self, cpf: str):
        """ This function performs the calculation of the INSS fee according to the salary amount
        :param cpf: number"""
        try:
            #  Receives salary from the database
            salary = self.db.select_salary(cpf)
            # Performing the calculation
            if salary <= 1045.00:
                track1 = round(((salary / 100) * 7.5), 2)
                return track1
            elif 1045.00 < salary <= 2089.60:
                track2 = round((((salary / 100) * 9) - 15.68), 2)
                return track2
            elif 2089.60 < salary <= 3134.41:
                track3 = round((((salary / 100) * 12) - 78.38), 2)
                return track3
            elif 3134.41 < salary <= 6101.06:
                track4 = round((((salary / 100) * 14) - 141.07), 2)
                return track4
            else:
                track5 = 713.08
                return track5
        except Exception as error:
            print(error)


if __name__ == '__main__':
    c = Calc()
    print(c.fee_inss(11384765311))
    help(c.fee_inss)
