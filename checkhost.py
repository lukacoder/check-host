import requests

print("""

------------------------------

 

        ~ Kedy Coder ~

------------------------------

""")

URL = input("Site {*http https*} ; ")

try:

    response = requests.head(URL)

except Exception as e:

    print(f"NOT OK: {str(e)}")

else:

    if response.status_code == 200:

        print("Web Site Online ! ")

    if response.status_code == 301:

    	print("Moved Permanently-> 301")    if response.status_code == 403:

    	print("Access Denied -> 403")

    if response.status_code == 404:

    	print("Page Not Found -> 404")

    if response.status_code == 500:

    	print("İnternal Server Error -> 500")

    if response.status_code == 503:

    	print("503 Service Unavailable Error -> 503")
