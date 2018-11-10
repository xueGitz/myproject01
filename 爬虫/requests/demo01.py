import requests

kw = {'wd':'长城'}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
           "Cookie": "BAIDUID = 0EFB4417D4D3C567FF90AB6E47BB16FD: FG = 1;PSTM = 1537155948;BIDUPSID = E7276F3866AB3A09E154B578652049E2;BD_UPN = 123353;H_PS_PSSID = 1458_21099_27401;BDRCVFR[dG2JNJb_ajR] = mk3SLVN4HKm;BDRCVFR[-pGxjrCMryR] = mk3SLVN4HKm;BDRCVFR[tox4WRQ4 - Km] = mk3SLVN4HKm;userFrom = null;delPer = 0;BD_CK_SAM = 1;PSINO = 5;H_PS_645EC = 6e36KSS0zRgUF2ZdtF2i5WgAbBkUkGYASMM8h2vvEVkSNoeJvT5iGCHyyyE;BDORZ = B490B5EBF6F3CD402E515D22BCDA1598",
           }

response = requests.get('https://www.baidu.com/s?',params=kw,headers=headers)

content = response.content

with open('{}.html'.format(kw['wd']),'wb') as f:
    f.write(content)
# print(response.text)
# print(response.content.decode())
print(response.status_code)
print(response.url)
print(response.encoding)