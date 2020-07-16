import pymysql


class Databank:

    def __init__(self):
        self.con = pymysql.connect(db='employee', user='root', passwd='')
        self.cursor = self.con.cursor()

    def create_table(self):
        """This function starts the table 'func' if the table don't exists."""
        try:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS func (cpf int(11) PRIMARY KEY not null, name varchar(255) '
                                'not null, last_name varchar(255) not null, age int(3) not null, salary decimal(10,2)'
                                ' not null)')
        except Warning:
            print('Table already exists.')

    def checking_register_employer(self, cpf: str):
        """This function checks if the employee is already registered in the database.
        :param cpf: number
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
            except IndexError:
                return False

    def register_employee(self, cpf: str, name: str, last_name: str, age: int, salary: float, dependents=0):
        """This function register the employee if he isn't registered in the database.
        :param cpf: number
        :param name: str
        :param last_name: str
        :param age: int
        :param salary: float
        :param dependents: number"""
        try:
            checking = self.checking_register_employer(cpf)
            if not checking:
                self.cursor.execute('INSERT INTO func (cpf, name, last_name, age, salary, dependents) values '
                                    '(%s, %s, %s, %s, %s, %s)', (cpf, name, last_name, age, salary, dependents))
                print('Employee registered successfully!')
            else:
                print("You're already registered.")
        except Warning:
            pass
        else:
            self.con.commit()
            self.con.close()

    def update_employee(self, cpf: str, name: str, last_name: str, age: int, salary: float):
        """This function updates the employee's data.
        :param cpf: number
        :param name: str
        :param last_name: str
        :param age: int
        :param salary: float"""
        checking = self.checking_register_employer(cpf)
        if not checking:
            print("Employee does not exist.")
        else:
            try:
                self.cursor.execute('UPDATE func SET name = %s, last_name = %s, age = %s, salary =%s WHERE cpf = %s',
                                    (name, last_name, age, salary, cpf))
                print('Updated successfully.')
                self.con.commit()
                self.con.close()
            except Exception:
                print('Error in the update!')

    def delete_employee(self, cpf: str):
        """This function delete the employee
        :param cpf: number"""
        try:
            self.cursor.execute('DELETE FROM func WHERE cpf = %s', (cpf,))
        except Exception:
            print("Employee does not exist.")
        else:
            self.con.commit()
            self.con.close()
            print('Employee deleted successfully!')

    def select_by_tuple(self, name: str, cpf: str):
        """This function makes a select in the database and obtains the employee's information according to the previous
         parameter passed in the method description by cpf
         :param name: string
         :param cpf: number"""
        data = []
        try:
            sql = f'SELECT {name} from func where cpf = {cpf}'
            self.cursor.execute(sql)
            for i in self.cursor.fetchall():
                data.append(i[0])
        except Exception as error:
            print(error)
        else:
            return data[0]


if __name__ == '__main__':
    # Testing the functions in the database.
    db = Databank()
    # db.register_employee(38734112319, 'Alan', 'Arroume', 34, 5000)
    # db.register_employee(11384765317, 'Ervald', 'Perlo', 33, '1322.30')
    # db.update_employee('11384765317', 'Everaldo', 'Pedro', 33, 1550.4)
    # db.delete_employee(11384765313)
    # print(db.checking_register_employer(11384765312))
    # print(db.select_salary(11373412312))
    # print(db.select_num_dependents(11373412312))
    db.select_by_tuple('name', 11373412312)
