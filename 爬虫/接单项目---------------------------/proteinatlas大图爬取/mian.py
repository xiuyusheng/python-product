import requests
import re
if __name__=="__main__":
    session=requests.Session()
    head={
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58"
    }
    resp=session.get('https://www.proteinatlas.org/ENSG00000148832-PAOX/subcellular',headers=head)
    url=re.findall(r'<a class="cellImg thumb imid_\d+" data-name="\d+" href="(.*?)"',resp.text,re.DOTALL)
    
    Location=re.findall(r'cellThumbs.*?<td>(.*?)</td>',resp.text,re.DOTALL)
    for i,j in enumerate(url):
        with open('P/{}.jpg'.format(i),'wb') as f:
            resp=session.get('https:{}'.format(j),headers=head)
            f.write(resp.content)
            print(Location[i//2])