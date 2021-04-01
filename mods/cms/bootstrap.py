import re
import requests

def bootstrap(urlht,header):
    req = requests.get(urlht, headers=header).text
    if "/css/bootstrap" in req:
        print("\n[\033[1;33m!\033[0;0m] - Bootstrap")
        try:

            list = []
            ver1 = re.findall(r'href=["\'](.*?)["\']',req)
            for q in ver1:
                if "/css/bootstrap" in q:
                    list.append(q)
                else:
                    pass
            lin = list[0]
            try:
                ver = requests.get(lin).text
            except:
                urlr = urlht + "/" + lin
                ver = requests.get(urlr).text

            version = re.findall(r'Bootstrap v(.*?) [(]https?://getbootstrap.com/?[)]',ver)
            v = version[0]
            print("Bootstrap v",v)
            print("---------------------------")



        except:
            pass