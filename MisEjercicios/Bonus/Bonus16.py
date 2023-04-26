import PySimpleGUI as sg

label1 = sg.Text("Select file to compress")
input1 = sg.Input()
buttom1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folde:")
input2 = sg.Input()
buttom2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")
window = sg.Window("File compresor",
                   layout=[[label1, input1, buttom1],
                                             [label2, input2, buttom2],
                           [compress_button]])

window.read()
window.close()