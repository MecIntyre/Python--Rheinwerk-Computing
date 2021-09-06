import qrcode

img = qrcode.make(
    'https://youtu.be/dQw4w9WgXcQ'
)
img.save('myQRcode.png')
img.show()
