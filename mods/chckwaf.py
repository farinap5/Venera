import requests

def checkwaf(urlht,header):
    def _exit():
        print("1")
        exit("[\033[1;33m!\033[0;0m] - Quitting")

    print("\nTest WAF:")
    r = requests.get(urlht,headers=header)

    opt = ["Yes","yes","Y","y"]
    try:
        if r.headers["server"] == "cloudflare":
            print("[\033[1;31m!\033[0;0m]The Server is Behind a CloudFlare Server.")
            ex = input("[\033[1;31m!\033[0;0m]Exit y/n: ")
            if ex in opt:
                _exit()
            else:
                pass
    except:
        pass

    noise = "?=<script>alert()</script>"
    fuzz = urlht + noise
    waffd = requests.get(fuzz,headers=header)
    if waffd.status_code == 406 or waffd.status_code == 501:
        print("[\033[1;31m!\033[0;0m] WAF Detected.")
    if waffd.status_code == 999:
        print("[\033[1;31m!\033[0;0m] WAF Detected.")
    if waffd.status_code == 419:
        print("[\033[1;31m!\033[0;0m] WAF Detected.")
    if waffd.status_code == 403:
        print("[\033[1;31m!\033[0;0m] WAF Detected.")
    else:
        print("[\033[1;32mOK\033[0;0m] No WAF Detected.")