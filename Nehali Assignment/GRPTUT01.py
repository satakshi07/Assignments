#Spelling Checker
"""
from textblob import TextBlob
myList = ["Incorret","spellin"]
corrected_list= []
for word in myList:
    corrected_list.append(TextBlob(word))
print("corrected List words are:")
for word in corrected_list:
    print(word.correct(),end="")
    """
#QRCode Generation
import pyqrcode
import png
from pyqrcode import QRCode
QRstring = "WWW.google.com"
url=pyqrcode.create(QRstring)
url.png('My_QR.png',scale=8)