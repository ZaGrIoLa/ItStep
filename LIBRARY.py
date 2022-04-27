import requests
res_parse_list=[]
response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text = response.text
response_parse = response_text.split("<tr>")
for parse_elem_1 in response_parse:
 if parse_elem_1.startswith("2"):
    for parse_elem_2 in parse_elem_1.split("</tr>"):
     if parse_elem_2.startswith("2")and parse_elem_2[1].isdigit():
       res_parse_list.append(parse_elem_2)
usd_exchange_rate = res_parse_list[4]
print(usd_exchange_rate)

