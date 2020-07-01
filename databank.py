import pymysql


class Databank:

    def __init__(self):
        self.con = pymysql.connect(db='employee', user='root', passwd='')
        self.cursor = self.con.cursor()

    def create_table(self):
        """This function starts the func table"""
        try:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS func (cpf int(11) PRIMARY KEY not null, name varchar(255) '
                                'not null, last_name varchar(255) not null, age int(3) not null, salary decimal(10,2)'
                                ' not null)')
        except Warning:
            print('Table already exists.')

    def checking_register_employer(self, cpf: str):
        """This function checks if the employee is already registered in the database.
        :param cpf: str
        :rtype: boolean
        """
        data_user = []
        try:
            self.cursor.execute('SELECT cpf FROM func where cpf = %s', cpf)
            for i in self.cursor.fetchall():
                data_user.append(i[0])
        except Exception:
            pass
        else:
            try:
                # Returning boolean values(True or False)
                if data_user[0] == str(cpf):
                    return True
                else:
                    return False
            except IndexError:
                pass

    def register_employee(self, cpf: str, name: str, last_name: str, age: int, salary: float):
        """This function register the employee if he isn't registered in the database.
        :param cpf: number
        :param name: str
        :param last_name: str
        :param age: int
        :param salary: float"""
        try:
            checking = self.checking_register_employer(cpf)
            if not checking:
                self.cursor.execute('INSERT INTO func (cpf, name, last_name, age, salary) values (%s, %s, %s, %s, %s)',
                                    (cpf, name, last_name, age, salary))
            else:
                print("You're already registered.")
        except Exception:
            pass
        else:
            self.con.commit()
            self.con.close()


if __name__ == '__main__':
    print('Funcionou')