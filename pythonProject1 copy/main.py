import requests
from bs4 import BeautifulSoup

cookies = {
    'BIGipServerprod-ethos_pool': '2785602314.58148.0000',
    '_ga': 'GA1.2.921598765.1603592657',
    'IDMSESSID': 'AEE650E19BDFF594D1F788AE7A503419DF350A204E52317479D9044F6222B2C8A7B405D2E12DC29C16C68E42B9789A3A2BFF49E449359AC3F226034B5016AB9A',
    'JSESSIONID': '7C8F2B76DD45BA76F6052CEF8BF37EBF',
    '_gid': 'GA1.2.1095708126.1605177352',
    'commonAuthId': '8724f9b9-417a-4e05-a8c0-82f8fb17bfdf',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://bannercas.cccs.edu',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://bannercas.cccs.edu/authenticationendpoint/login.do?Name=PreLoginRequestProcessor&commonAuthCallerPath=%252Fcas%252Flogin&forceAuth=true&passiveAuth=false&service=https%3A%2F%2Ffrcc.desire2learn.com%2Fd2l%2Fcustom%2Fcas&tenantDomain=carbon.super&vpdi=frcconline&sessionDataKey=d411bab0-38b1-4e56-bae3-508635aaeec3&relyingParty=D2L_FRCC&type=cas&sp=D2L_FRCC&isSaaSApp=false&authenticators=BasicAuthenticator:LOCAL',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
    'username': 'username',
    'password': 'password',
    'sessionDataKey': 'd411bab0-38b1-4e56-bae3-508635aaeec3'
}

response = requests.post('https://bannercas.cccs.edu/commonauth', headers=headers, cookies=cookies, data=data)


headers = {
    'authority': 'frcc.desire2learn.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://frcc.desire2learn.com/d2l/home/2805880',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'i18next=en-US; d2lSessionVal=To7ojGQzIcLIT4GmQwtYNIhX6; d2lSecureSessionVal=CiiE5Vk1WDctzFKssQhXqMGJh; ADRUM=s=1605180016640&r=https%3A%2F%2Ffrcc.desire2learn.com%2Fd2l%2Flp%2Fhomepage%2FLegacyWidgetViewer.d2l%3F331611277',
}

response = requests.get('https://frcc.desire2learn.com/d2l/le/news/2805880/4447419/view', headers=headers)


headers = {
    'Origin': 'https://frcc.desire2learn.com',
    'Referer': 'https://s.brightspace.com/lib/bsi/20.20.10-67/unbundled/d2l-navigation.js',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36',
}

response = requests.get('https://s.brightspace.com/lib/bsi/20.20.10-67/unbundled/polymer-element.js', headers=headers)





headers = {
    'authority': 'fa00bc7e-2da3-42ed-8c08-a2a1e55d8dce.organizations.api.brightspace.com',
    'accept': 'application/vnd.siren+json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjFlODMyYmUwLTI4MTAtNDcxMi1iZmU4LTgyNzcyNjA5NmFhYiJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNjA1MTgxMDc3LCJuYmYiOjE2MDUxNzc0NzcsInN1YiI6IjE1MjIwNzEiLCJ0ZW5hbnRpZCI6ImZhMDBiYzdlLTJkYTMtNDJlZC04YzA4LWEyYTFlNTVkOGRjZSIsImF6cCI6ImxtczpmYTAwYmM3ZS0yZGEzLTQyZWQtOGMwOC1hMmExZTU1ZDhkY2UiLCJzY29wZSI6Iio6KjoqIiwianRpIjoiOTZjYWZjZDctMjk2MS00NDQyLWJkOTItNTE0ODFmZThhNzEyIn0.D5pYx-2LbHoYmMk3axzMkJuLUuhwhKyJ-XUQ21ZWF7tkCjdOBnb8Cmv5ZXCC2WDkF-A4XBPQBCAvWkWzuc0OrFV0ZvEtPqRJansOEbuRM-xXwsT-VLjAWNy2VyccoKeGVMBC2gukck-qdSRZibcN_tA_tXooBZQSzl7oykOk3QIkq1e2BNZnfg6V-8USnoMPT31dA3sGuOHYdSuEQEF17MIyRxxiAMu3ygqGYvfXC8URqnxLZoZjbZ9YbU_zTsuWHEm83yst3BgaNvd64cx-issC_xQpKdoJhkI9zfLXNPT9zswxw9PUpU1ovMhsnVMhJAjxcpkUwATAySD9yEfvvw',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36',
    'origin': 'https://frcc.desire2learn.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://frcc.desire2learn.com/',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'ACC077CE',
}

response = requests.get('https://fa00bc7e-2da3-42ed-8c08-a2a1e55d8dce.organizations.api.brightspace.com/2722655', headers=headers)











## pre-cal scrape
## pull headers etc from DEV TOOLS google chrome

headers = {
    'authority': 'frcc.desire2learn.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://frcc.desire2learn.com/d2l/le/news/2805880/4447419/view',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'i18next=en-US; d2lSessionVal=To7ojGQzIcLIT4GmQwtYNIhX6; d2lSecureSessionVal=CiiE5Vk1WDctzFKssQhXqMGJh; ADRUM=s=1605181996491&r=https%3A%2F%2Ffrcc.desire2learn.com%2Fd2l%2Flms%2Fnews%2Fmain.d2l%3F-910641543',
}

response = requests.get('https://frcc.desire2learn.com/d2l/home/2722655', headers=headers)






#url = 'https://frcc.desire2learn.com/d2l/home/2805880'

#results = requests.get('https://frcc.desire2learn.com/d2l/le/news/2805880/4447419/view')
content = response.content
soup = BeautifulSoup(content, features='lxml')
items = soup.find_all(id="<li>")

print(soup.prettify())

#WE NOW HAVE OUR SOURCE HTML FILE TO PULL FROM, NON-HASHMAPPED
#NO ERRORS ON REQUESTS


#find all instances of the divs/classes that contain data we want
scrape_data = soup.find_all('div', attrs= {'class', 'd2l-htmlblock d2l-htmlblock-deferred d2l-htmlblock-untrusted'})


##number of useful text blocks, or announcments
print("\n")
print('total useful segments found so far : ', len(scrape_data))
print(" ")

##source code for math announcments
for data in scrape_data:
    print(data)


##extract the information
for items in scrape_data:
    data_points = soup.find('p')
    data_lists = soup.find('l')

    ##debug statment
    ##print(data_points, data_lists)


#decompose unneccessary DIVS
#for data in scrape_data:
remove = "<p class="
for remove in soup.find_all("div", {'p class': 'div class="d2l-htmlblock d2l-htmlblock-deferred d2l-htmlblock-untrusted'}):
    soup.decompose()

for data in scrape_data:
    dataList = [] = soup.find_all('class', '"d2l-navigation-s-mobile-menu-first d2l-offscreen"')
    soup.decompose()

#soup.decompose("d2l-navigation-s-mobile-menu-first-d2l-offscreen")
##Store all the data so far



all_data = []

for data in scrape_data:

    ## start a dictionary

    all_data = [data_points]
    all_data += [data_lists]
for data_lists in all_data:
    soup.find_all('class', soup.decompose())
    #for  in data_lists:
        #soup.find_all('class', soup.decompose())

    #print(all_data)
