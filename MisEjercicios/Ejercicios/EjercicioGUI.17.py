def convert(feet, inches):
    meters = feet * .3048 + inches * .0254
    return meters

import PySimpleGUI as sg

label_feet = sg.Text("Enter feet")
label_inches = sg.Text("Enter inches")
feet_text = sg.InputText(tooltip="Enter feet", key="feet")
inch_text = sg.InputText(tooltip="Enter inches", key="Inch")
convert_button = sg.Button("Convert")
output_label = sg.Text("",key="output")
window =sg.Window("Convertor", layout=[[label_feet, feet_text],
                                       [label_inches, inch_text],
                                       [convert_button, output_label]])
while True:
    event, values = window.read()
    match event:
        case "convert":
            feet = float(values["feet"])
            inches = float(values["Inch"])
            con = convert(feet, inches)
            window["output"].update(f"{con}m",text_color="white")
        case sg.WIN_CLOSED:
            break
window.close()
