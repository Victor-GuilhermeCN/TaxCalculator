from databank import Databank


class Calc:

    def __init__(self):
        self.db = Databank()

    def inss(self, cpf):
        salary = []
        try:
            consult = self.db.checking_register_employer(cpf)
            if consult:
                cons_sal = self.db.cursor.execute('SELECT salary FROM func where cpf = %s', (cpf,))
                for i in self.db.cursor.fetchall():
                    salary.append(i[0])
                if salary[0] <= 1045.00:
                    aliq = (salary[0] / 100) * 7.5
                    print(aliq)
                elif 1045.01 < salary[0] <= 2089.60:
                    aliq = (salary[0] / 100) * 9
                    print(aliq)
                elif 2089.61 < salary[0] <= 3134.40:
                    aliq = (salary[0] / 100) * 12
                    print(aliq)
                elif 3134.31 < salary[0] <= 6101.06:
                    aliq = (salary[0] / 100) * 14
                    print(aliq)
                else:
                    aliq = (salary[0] / 100) * 14
                    print(aliq)
            else:
                print('tem nada')
        except:
            print('porra')
            print(salary[0])
        else:
            print(salary[0])


if __name__ == '__main__':
    c = Calc()
    c.inss(11384765311)






