import requests
a=requests.get('https://apd-c2483e72476ad7a6c85aa371c1e4c913.v.smtcdns.com/moviets.tc.qq.com/AClDaX-G0m8ShrxXLdAFTb87nBMJA_mR5OTNdbUGkmvc/B_Ui4-QEkRPfhTNlYdo0Hujm-a2cdEpzIOcpoUZ4PumfQ/svp_50112/g6u_Zoy4N4SJaq3yb4krnccEZd9cf4ea_ZI7wiTNpx8F1coZoWnSkS3LqBz-H_FENbswH3DJxC0aZ3Glwp7X1hiAeOHWYDsxj5O7hCrx_WZWFVOgXBWAqmhpAVB_sKjqc7W14HY7H3tLL26EQoMZGqUPRyPd6VcS99S2F5nkSCY/00_gzc_1000102_0b53amaeoaaayiajdsoys5r4aa6di5zqaq2a.f322062.1.ts?index=0&start=0&end=12000&brs=0&bre=558735&ver=4&token=0e47a96ef79cadf2d67ffcdc205d0892')
print(a.text)
with open('11.mp4','w') as f:
    f.write(a.content)
# print(a.text)