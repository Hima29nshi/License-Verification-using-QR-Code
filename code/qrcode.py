import cv2
import numpy as np
from pyzbar.pyzbar import decode
from tabulate import tabulate
import csv


def data_list():
    myDataList = list()
    with open('hello.csv', 'r', newline='') as cs:
        reader = csv.DictReader(cs)
        for row in reader:
            myDataList.append(row['Name'])
        return myDataList


def print_data():
    with open('hello.csv', 'r', newline='') as cs:
        reader = csv.DictReader(cs)
        for r in reader:
            li = list(r.values())
            keys = list(r.keys())
            if li[0] == myData:
                table = [keys, li]
                print(tabulate(table, headers='firstrow',
                               tablefmt='fancy_grid'))


url = "http://192.168.1.100:8080/video"
#! img = cv2.imread('qrcodes/Megha.png')

cap = cv2.VideoCapture(url)
#! Size of the output window
cap.set(1, 250)
cap.set(2, 250)

myDataList = data_list()

while True:
    #! Reading data on QR code
    success, img = cap.read()
    for code in decode(img):
        #! Decoding the unicode 8-bit data
        myData = code.data.decode('utf-8')
        #! Printing the decoded data
        print(myData)

        #! If data is in the list will display authorized above polygon
        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
            print(myOutput)
            print_data()

        #! If data is not in the list will display un-authorized above polygon
        else:
            myOutput = 'Un-Authorized'
            print(myOutput)
            myColor = (0, 0, 255)

        #! This is for polygon(green/red for authorized/un-authorized)
        pts = np.array([code.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = code.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)
        #! End of polygon

    #! Image display
    cv2.imshow('Result', img)

    #! To quit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
