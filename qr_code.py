import qrcode

qr = qrcode.make("Follow me : https://www.youtube.com/@liumath6")
qr.save("my_qrcode.png")
print("QR Code generated and saved as 'my_qrcode.png!'")