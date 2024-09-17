import requests

url_list = ['https://www.youtube.com/results?search_query=python+requests+library',
            'https://docs.ansible.com/automation-controller/latest/html/controllerapi/authentication.html',
            'https://www.sro.vic.gov.au/homebuyer/homebuyer-fund-case-studies',
            'https://api.github.com/',
            'https://api.github.com/invalid']

#for url in url_list:
    #response = requests.get(url)
    #print(url, '->' ,response.status_code)

for url in url_list:
    response = requests.get(url)

    if response:
        print(url,'-> Success')
    else:
        print(url, '-> An Error has occured')