import PySimpleGUI as sg
from taxes import *


class ScreenConsult:
    def __init__(self):
        self.tax = Calc()
        # Layout
        layout = [
            [sg.Text('CPF:', size=(5, 0)), sg.Input(size=(30, 0), key='cpf')],
            [sg.Button('Consult', key='cons1'), sg.Cancel(key='can1')],
            [sg.Output(key='out')],

        ]
        # Window
        self.wind = sg.Window('Consult Taxes').Layout(layout)
        # Extract the screen data

    def consult(self):
        while True:
            self.button, self.values = self.wind.Read()
            print(f"INSS: {self.tax.fee_inss(self.values['cpf'])}")
            print(f"IRRF: {self.tax.fee_irrf(self.values['cpf'])}")
            print('-' * 78)


if __name__ == '__main__':
    win = ScreenConsult()
    win.consult()