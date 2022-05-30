import PySimpleGUI as sg
import manieri.model.connectorDB.ConnectorMariaFatimaDB as Con
import manieri.model.queryDB.QueryDB as Qry

def TestMenus():

    sg.ChangeLookAndFeel('Dark')
    sg.SetOptions(element_padding=(0, 0))


    menu_def = [['File', ['new',['Order','User','Tool'], 'Save', ]],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'], ]

    # ------ GUI Defintion ------ #
    layout = [
        [sg.Menu(menu_def)],
        [[sg.Text('Some text on 1')],[sg.Output(size=(60, 50))]],
        [sg.Text('Some text on Row 1')]
    ]

    form = sg.FlexForm("Windows-like program", default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,
                       default_button_element_size=(12, 1))
    form.Layout(layout)

    # ------ Loop & Process button menu choices ------ #
    while True:
        button, values = form.Read()
        if button is None or button == 'Exit':
            return
        print('Button = ', button)
        # ------ Process menu choices ------ #
        if button == 'About...':
            sg.Popup('About this program','Version 1.0', 'PySimpleGUI rocks...')
        elif button == 'Open':
            filename = sg.PopupGetFile('file to open', no_window=True)
            print(filename)
        elif button == 'Order':
            print('testas')


TestMenus()
