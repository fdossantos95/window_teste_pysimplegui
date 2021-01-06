import PySimpleGUI as sg 

sg.theme('DarkAmber')

layout = [ [sg.Text('Some text on Row 1')],
           [sg.Text('Enter something on Row 2'), sg.InputText()],
           [sg.Button('OK'), sg.Button('CANCEL')]]

window = sg.Window('Window title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'CANCEL':
        break
    print('You entered', values[0])

window.close()
