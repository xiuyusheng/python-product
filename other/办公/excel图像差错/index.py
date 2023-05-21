import easyocr
import re


reader = easyocr.Reader(['en','ch_sim'],gpu=True)
with open('2006200101周凯鸣 .jpg', 'rb') as f:

    result = reader.readtext(f.read())
# for i in result:
#         print(i)
data=(list(result[i][1] for i in list(range(18,30,3))[:3]))
print(data)
    

