import requests

url = 'https://shopee.com.my/api/v4/search/search_items?by=relevancy&keyword=watch&limit=50&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'cookie': 'REC_T_ID=57946d7c-376f-11eb-b145-08f1ea7b48c8; SPC_EC=-; SPC_IA=-1; SPC_U=-; SPC_F=6nryLr3SNtMfoeGxR5v0yG2UU7wJ1GJq; language=zhHans; _gcl_aw=GCL.1620391582.Cj0KCQjwytOEBhD5ARIsANnRjVimdft-AzXC4Cu4u3KgynA01Q8HeFOd2ySHbpCuGtiSPiMTXjzpWyMaApWEEALw_wcB; _gcl_au=1.1.410984046.1620391582; _med=refer; csrftoken=JPAGdwVfoQXCtoevw67aen21oap9UgGD; SPC_SI=mall.Y5GS01JmPS1AX1XfBeotofv06qd7LdsX; welcomePkgShown=true; SPC_R_T_ID="2rD4lv/dcLx5SZ4eTzzLZWxPqsECkzgU7Db0CZ8cxNiwGUtPKGYFf15zEwn3Z4NopSQxapzk/xgmUzwX5Yne6cQ7XpqlyFyP4mVtCbyQKhs="; SPC_T_IV="JL7b4y+n5TnZYdDc4w767w=="; SPC_R_T_IV="JL7b4y+n5TnZYdDc4w767w=="; SPC_T_ID="2rD4lv/dcLx5SZ4eTzzLZWxPqsECkzgU7Db0CZ8cxNiwGUtPKGYFf15zEwn3Z4NopSQxapzk/xgmUzwX5Yne6cQ7XpqlyFyP4mVtCbyQKhs="'
}
response = requests.get(url, headers=headers)
print(response.text)