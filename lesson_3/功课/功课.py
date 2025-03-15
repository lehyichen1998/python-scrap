import requests

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'cookie': 'REC_T_ID=57946d7c-376f-11eb-b145-08f1ea7b48c8; SPC_EC=-; SPC_IA=-1; SPC_U=-; SPC_F=6nryLr3SNtMfoeGxR5v0yG2UU7wJ1GJq; language=zhHans; _gcl_aw=GCL.1620391582.Cj0KCQjwytOEBhD5ARIsANnRjVimdft-AzXC4Cu4u3KgynA01Q8HeFOd2ySHbpCuGtiSPiMTXjzpWyMaApWEEALw_wcB; _gcl_au=1.1.410984046.1620391582; csrftoken=hpR3Tr1i7QdhRYyHKvdphWkkxdlddh1C; SPC_SI=bfftocsg4.iasYdSAtIPYbEXPxamhQRuTix3F1hy6h; welcomePkgShown=true; _med=affiliates; _atnct=%7B%220f840be9b8db4d3fbd5ba2ce59211f55%22%3A%22wycQiKaOr5fTMTrJQ8dgSKoiVyt2GF4IPPYafgCDeZk97NoS%22%2C%22_hostname%22%3A%22shopee.com.my%22%7D; SPC_R_T_ID="dBc1xbNnj9G3cj0y4ouUcSftMUoq0cAm0SQ8fL2raM1rXBjr2Am4bGbtC0t/9TRrDSkxV9vwBG9W+XM1KKZn7WESap8+jwWERMq/6qdwnuM="; SPC_T_IV="HaESJT1gq5tQCojRAaKUDw=="; SPC_R_T_IV="HaESJT1gq5tQCojRAaKUDw=="; SPC_T_ID="dBc1xbNnj9G3cj0y4ouUcSftMUoq0cAm0SQ8fL2raM1rXBjr2Am4bGbtC0t/9TRrDSkxV9vwBG9W+XM1KKZn7WESap8+jwWERMq/6qdwnuM="'
}
r = requests.get('https://cf.shopee.com.my/file/4930c6263001ef67fe9c44609ae1d65d_tn', headers=header)
with open('new_shopee.png', 'wb') as f:
    f.write(r.content)