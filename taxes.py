from databank import Databank
import unittest


class Calc:

    def __init__(self):
        self.db = Databank()

    def fee_inss(self, cpf: str):
        """ This function performs the calculation of the INSS fee according to the salary amount
        :param cpf: number
        :return fee INSS"""
        try:
            #  Receives salary from the database
            salary = float(self.db.select_by_tuple('salary', cpf))
            # Performing the calculation
            if salary <= 1045.00:
                track1 = ((salary / 100) * 7.5)
                return round(track1, 2)
            elif 1045.00 < salary <= 2089.60:
                track2 = (((salary / 100) * 9) - 15.68)
                return round(track2, 2)
            elif 2089.60 < salary <= 3134.41:
                track3 = (((salary / 100) * 12) - 78.38)
                return round(track3, 2)
            elif 3134.41 < salary <= 6101.06:
                track4 = (((salary / 100) * 14) - 141.07)
                return round(track4, 2)
            else:
                track5 = 713.08
                return track5
        except Exception as error:
            print(error)

    def fee_irrf(self, cpf: str):
        """This function performs the calculation of the IRRF fee according to the salary amount
        :param cpf: number
        :return IRRF fee"""
        try:
            salary = float(self.db.select_by_tuple('salary', cpf))
            dependents = self.db.select_by_tuple('dependents', cpf)
            liq_sal = ((salary - self.fee_inss(cpf)) - (dependents * 189.59))
            if liq_sal <= 1903.98:
                print('Exempt from IRRF.')
                return 0
            elif 1903.99 <= liq_sal <= 2826.65:
                aliq = (liq_sal * 0.075) - 142.80
                return round(aliq, 2)
            elif 2826.66 <= liq_sal <= 3751.05:
                aliq = (liq_sal * 0.15) - 354.80
                return round(aliq, 2)
            elif 3751.06 <= salary <= 4664.68:
                aliq = (liq_sal * 0.225) - 636.13
                return round(aliq, 2)
            else:
                aliq = (liq_sal * 0.275) - 869.35
                return round(aliq, 2)
        except Exception as error:
            print(error)


class Calctest(unittest.TestCase):
    """Class to test the components."""
    def test_inss(self):
        obj = Calc()
        self.assertEqual(obj.fee_inss(11384765311), 713.08)

    def test_irrg(self):
        obj = Calc()
        self.assertEqual(obj.fee_irrf(11384765311), 1476.00)


if __name__ == '__main__':
    # c = Calc()
    # print(c.fee_inss(11373412312))
    # help(c.fee_inss)
    # print(c.fee_irrf(11384765311))
    unittest.main()
    # c = Calc()
    # print(c.fee_irrf(11373412312))