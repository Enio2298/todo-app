import PySimpleGUI as sg
from ZipCreator import make_archive

label1 = sg.Text("Select file to compress")
input1 = sg.Input()
buttom1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folde:")
input2 = sg.Input()
buttom2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output = sg.Text(key="output", text_color="green")
window = sg.Window("File compresor",
                   layout=[[label1, input1, buttom1],
                                             [label2, input2, buttom2],
                           [compress_button, output]])


while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed")

window.close()