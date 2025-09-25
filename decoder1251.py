text = 'Фамилия Имя Отчество'
encoded_text = text.encode('1251')
for byte in encoded_text:
    print(byte)
