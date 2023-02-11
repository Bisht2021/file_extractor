import PySimpleGUI as sg
from extract_archive import extract_archive

label1 = sg.Text("Select file")
input1 = sg.Input()
button1= sg.FileBrowse("choose",key="archive")

label2 = sg.Text("Select folder")
input2 = sg.Input()
button2= sg.FolderBrowse("choose",key = "Folder")

extract_button = sg.Button("Extract")
extract_text = sg.Text(key="output")

window = sg.Window("file Extractor",layout = [[label1,input1,button1],
                                                [label2,input2,button2],
                                                [extract_button,extract_text]])
while True:

    event,value = window.read()
    print(event,value)
    file_path = window['archive']
    folder_path = window['Folder']
    extract_archive(file_path,folder_path)
    window['output'].update(value='Extraction complete')
window.close()
