import PySimpleGUI as sg
from databank import Databank


class ScreenPython:
    def __init__(self):
        self.db = Databank()
        # Layout
        layout = [
            [sg.Text('CPF:', size=(10, 0)), sg.Input(size=(30, 0), key='cpf')],
            [sg.Text('Name:', size=(10, 0)), sg.Input(size=(30, 0), key='name')],
            [sg.Text('Last Name:', size=(10, 0)), sg.Input(size=(30, 0), key='last_name')],
            [sg.Text('Age:', size=(10, 0)), sg.Input(size=(30, 0), key='age')],
            [sg.Text('Salary:', size=(10, 0)), sg.Input(size=(30, 0), key='salary')],
            [sg.Text('Dependents:', size=(10, 0)), sg.Input(size=(30, 0), key='dependents')],
            [sg.Button('Submit')],
            [sg.Output(size=(40, 20))],
        ]
        # Window
        self.wind = sg.Window("Register employer!").Layout(layout)

    def start(self):
        while True:
            # Extract window data
            self.button, self.values = self.wind.Read()
            print(f"CPF: {self.values['cpf']}\n"
                  f"Name: {self.values['name']}\n"
                  f"Last name: {self.values['last_name']}\n"
                  f"Age: {self.values['age']}\n"
                  f"Salary: {self.values['salary']}\n"
                  f"Dependents: {self.values['dependents']}")
            self.db.register_employee(self.values['cpf'], self.values['name'], self.values['last_name'], self.values[
                'age'], self.values['salary'], self.values['dependents'])


if __name__ == '__main__':
    tela = ScreenPython()
    tela.start()
