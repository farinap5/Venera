import requests

def req_code(urlht,header):
    t = requests.head(urlht,headers=header)
    code = t.status_code
    return code
def req_content(urlht,header):
    t1 = requests.get(urlht,headers=header).text
    return t1
def req_header(urlht,header):
    t2 = requests.get(urlht,headers=header)
    headerss = t2.headers
    return headerss