import easyocr
import re


reader = easyocr.Reader(['en','ch_sim'],gpu=True)
with open('2006070112蓝洁欣.jpg','rb') as f:

    result = reader.readtext(f.read())
# for i in result:
#     if 'JD:' in i[1]:
#         print(i[1][-11:-5])
#         break
print(result)

