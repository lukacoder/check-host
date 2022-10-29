from requests import get
import whois
import sys
print("""
----------------------------------------------------------------
                - H O S T    C H E C K E R -


                    ~ LUKAC0DER ~
                        
                    1- Who.İs
                    2- DnsLookUp
                    3- ReverseDns 
                    4- Geoİp
                    5- Nmap Scan
                    6- Reverse İp LookUp
                    7- Http Header and Page Link
                    8- Url Checker and Control(Check-Host)
----------------------------------------------------------------
""")
degisken = input(" ->  ")
if degisken == "1" : 
    wk = input(" Site (google.com) -> ")
    w = whois.whois(wk)
    print(w)
    input("")
if degisken == "2" : 
    inp = input("Site ('google.com') -> ")
    result = get('https://api.hackertarget.com/dnslookup/?q=' + inp).text
    print(result)
    input("")
if degisken == "3":
    inp = input("Site ('google.com') -> ")
    result = get('https://api.hackertarget.com/reversedns/?q=' + inp).text
    print(result)
    input("")
if degisken == "4":
    inp = input("Site ('google.com') -> ")
    result = get('https://api.hackertarget.com/geoip/?q=' + inp).text
    print(result)
    input("")
if degisken == "5":
    inp = input("Site ('google.com') -> ")
    result = get('https://api.hackertarget.com/nmap/?q=' + inp).text
    print(result)
    input("")
if degisken == "6":
    inp = input("Site ('google.com') -> ")
    result = get('https://api.hackertarget.com/reverseiplookup/?q=' + inp).text
    print(result)
    input("")
if degisken == "7":
    url = input(" URL  (google.com)   ->   ")
    response = get('https://api.hackertarget.com/httpheaders/?q=' + url).text
    response2 = get('https://api.hackertarget.com/pagelinks/?q=' + url).text
    sys.stdout.write(response)
    sys.stdout.write(response2)
    input("")
if degisken == "8":
    URL = input("Site {*http https*} ; ")
    try:
        response = requests.head(URL)
    except Exception as e:
        print(f"NOT OK: {str(e)}")
    else:
        if response.status_code == 200:
            print("Web Site Online ! ")
            input("")
        if response.status_code == 300:
            print("Multiple Choices-> 300")
            input("")
        if response.status_code == 301:
            print("Moved Permanently -> 301")
            input("")
        if response.status_code == 302:
            print("Moved Temporarily -> 302")
            input("")
        if response.status_code == 303:
            print("See Other -> 303")  
            input("")
        if response.status_code == 304:  
            print("Not Modified	 -> 304")  
            input("")
        if response.status_code == 400:
            print("Bad Request	-> 400 ")
            input("")
        if response.status_code == 401:
            print("Unauthorized	-> 401")
            input("")
        if response.status_code == 401:
            print("Payment Required	-> 402")
            input("")
        if response.status_code == 401:
            print("Method Not Allowed -> 405 ")
            input("")
        if response.status_code == 403:
            print("Access Denied -> 403")
            input("")
        if response.status_code == 404:
            print("Page Not Found -> 404")
            input("")
        if response.status_code == 500:
            print("İnternal Server Error -> 500")
            input("")
        if response.status_code == 501:
             print("501")
             input("")
        if response.status_code == 503:
             print("503 Service Unavailable Error -> 503")
             input("")

