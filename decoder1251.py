text = 'Смирнов Евгений Михайлович'
encoded_text = text.encode('1251')
for byte in encoded_text:
    print(byte)

# 209 236 232 240 237 238 226 
# 32
# 197 226 227 229 237 232 233 
# 32 
# 204 232 245 224 233 235 238 226 232 247