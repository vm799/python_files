import PySimpleGUI as sg

layout = [[sg.Text("Hey hey beautiful!")], [sg.Button("Exit here")]]
window = sg.Window(title="Booykashaa", layout=[[]], margins=(100,50))

while True:
    event, values = window.read()
    if event == "Exit here" or event == sg.WIN_CLOSED:
        break
window.close()