import requests
from bs4 import BeautifulSoup
from lxml import html
import re

headers = {
        "Host": "accesscard.campuscardcenter.com",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Origin": "https://accesscard.campuscardcenter.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://accesscard.campuscardcenter.com/ch/login.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh;q=0.8,zh-CN;q=0.6,zh-TW;q=0.4"
    }
    
def get():
	payload = {
		"username": "username", 
		"password": "password", 
		"action":"Login"
	}

	session_requests = requests.session()

	login_url = "https://accesscard.campuscardcenter.com/ch/login.html"
	result = session_requests.get(login_url, headers = headers)

	result = session_requests.post(
		login_url, 
		data = payload, 
		headers = headers
	).text

	soup_result = BeautifulSoup(result, 'html.parser')
	table = soup_result.find('div', {'class': 'feature'}).find_all('table')

	print(table[2])
	mealplan = table[2].find(text = re.compile(r' Meals'))

	plan_total_string = re.findall('\\d+', mealplan)
	plan_total = int(plan_total_string[0])

	meal_left = mealplan.parent.findNext('td').findNext('td').find('div')
	meal_left_int = int(meal_left.text.strip())

	return { 'meal_plan' : plan_total,
			'meal_left': meal_left_int
	}







	#print(Text)
	#result = session_requests.get(login_url)

