# License-Detection-using-QR-Code
We have implemented a system which checks whether the License is authorized or un- authorized. 
In this system, we can generate a QR code and can enter the data of applicant and generate new QR code. 
We can scan this QR code through webcam or mobile phone to retrieve the data present in QR code, if data 
retrieved in scanner app and data in the csv file mismatches then we can conclude that the license belongs 
to an un-authorized person. 
To build this project: 
1. The Python libraries – pyzbar, PIL, pillow, pyqrcode, opencv-python, etc. was used in the system. 
2. Using pyqrcode, QR code were generated with the data. 
3. IP webcam application was used for scanning purpose.
