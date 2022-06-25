import time
import PySimpleGUI as sg
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time


def main():

    sg.theme('Black')

    # define the window layout
    layout = [[sg.Text('QRator', size=(40, 1), justification='center', font='Helvetica 20')],
              [sg.Image(filename='',size = (40,40), key='image')],
              [
               sg.Text('Scanning...', size=(10, 1), font='Helvetica 14',key='status'), ]]

    # create the window and show it without the plot
    window = sg.Window('QRator - QR Scanner',
                       layout, location=(800, 400))

    # ---===--- Event LOOP Read and display frames, operate the GUI --- #
    cap = cv2.VideoCapture(0)
    recording = False

    def verify(qr):
        return True

    def qrfound(qr):
        if verify(qr):
            window.Element('status').update('Verified')
            
            window['image'].update('rename.gif',size=(650,300))
            window.refresh()
            t1 = time.time()
            while True:
                t2 = time.time()
                if (t2 - t1) > 4:
                    window.Element('status').update('Scanning...')
                    break
        print(qr)

    def decoder(img):
        gray = cv2.cvtColor(img,0)
        qr = decode(gray)

        return qr
    while True:
        
        event, values = window.read(timeout=15)

        if event == 'Exit' or event == sg.WIN_CLOSED:
            return
        recording = True
        if recording:
            ret, frame = cap.read()
            qr = decoder(frame)
            if len(qr) == 0:
                pass
            else:
                qrfound(qr[0].data.decode('utf-8'))
            
            imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
            window['image'].update(data=imgbytes)


main()
