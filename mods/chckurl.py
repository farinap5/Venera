import re
import requests

def check(urlht,header):
    def tite(urlht):
        url1 = requests.get(urlht, headers=header).text
        url2 = re.findall("<title>(.*)</title>", url1)
        print("\033[1;32mTitle\033[0;0m:", url2[0])
    try:
        tite(urlht)
    except:
        print("[\033[1;31mX\033[0;0m] No title found.")

    ok = "[\033[1;32mOK\033[0;0m]"
    q = "[\033[1;33m!\033[0;0m]"
    f = "[\033[1;31mX\033[0;0m]"

    print("\nTest Status:")
    check = requests.get(urlht,headers=header)
    #this frist connection with the target needs to be 200
    #this is why there is just one option of status code.
    if check.status_code == 200:
        print(ok, "Target:", urlht)
        print("Status Code: \033[1;32m200\033[0;0m")
        print(ok, "Connection Estabilished.")
    else:
        print(q, "Target:", urlht)
        print(q,"Status Code: ",check.status_code)

#status code OK
