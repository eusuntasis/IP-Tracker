import requests

print(""""

▪   ▄▄▄·    ▄▄▌         ▄▄·  ▄▄▄· ▄▄▄▄▄      ▄▄▄  
██ ▐█ ▄█    ██•  ▪     ▐█ ▌▪▐█ ▀█ •██  ▪     ▀▄ █·
▐█· ██▀·    ██▪   ▄█▀▄ ██ ▄▄▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█▌▐█▪·•    ▐█▌▐▌▐█▌.▐▌▐███▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
▀▀▀.▀       .▀▀▀  ▀█▄▀▪·▀▀▀  ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
                                                  
----------------------------------------------
| Author:   | @thescriptkiddie1              |
| Github:   | https://github.com/hxlxmjxbbxs |
| Released: | 02/05/2024                     |
----------------------------------------------\n""")

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.text)
        return None
def main():
    ip = input("Target IP = ")
    ip_info = get_ip_info(ip)
    if ip_info:
        print("IP adress information: \n")
        print("---------------------------------|")
        print("IP:", ip_info.get("ip"))
        print("---------------------------------|")
        print("Country:", ip_info.get("country"))
        print("---------------------------------|")
        print("Region:", ip_info.get("region"))
        print("---------------------------------|")
        print("City:", ip_info.get("city"))
        print("---------------------------------|")
        print("Postal code:", ip_info.get("postal"))
        print("---------------------------------|")
        print("Coordinates:", ip_info.get("loc"))
        print("---------------------------------|")
        print("Company:", ip_info.get("org"))
        print("---------------------------------|")
    else:
        print("Error:IP address information could not be obtained.")

if __name__ == "__main__":
    main()
