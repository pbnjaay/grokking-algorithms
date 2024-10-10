import qrcode

source = input('Enter the text or url: ').strip()
file_name = input('Enter the filename: ').strip()
img = qrcode.make(source)
img.save(file_name)

print(f'Qr code saved as {file_name}')
