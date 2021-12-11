import PySimpleGUI as sg

def func(message):
    print(message)

layout = [[sg.Button('1',key="mot"), sg.Button('1',key="hai"),sg.Button('2',key='Ba'), sg.Exit()] ]

window = sg.Window('ORIGINAL').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if(event=='1'):
        if event == "mot":
            func('Pressed button 1')
        elif (event == 'hai'):
            func('Pressed button 2')
window.Close()
