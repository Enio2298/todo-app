import PySimpleGUI as sg

label1 = sg.Text("Enter feet: ")
textbox1 = sg.InputText()
label2 = sg.Text("Enter Inches: ")
textbox2 = sg.InputText()
buttom = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[label1, textbox1],
                                        [label2, textbox2],
                   [buttom]])
window.read()
window.close()