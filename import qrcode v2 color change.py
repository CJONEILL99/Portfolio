import qrcode

data_1 = 'Don\'t forget to Check out my portfolio!'

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data_1)

qr.make(fit = True)

img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('FOLDER/PATHWAY') #where the qrcode is saved. !If copy & paste, make sure to change the backslash to a slash!