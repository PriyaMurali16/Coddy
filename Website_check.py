import requests
def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Website is Up"
        else:
            return "Website is Down"
    except requests.ConnectionError:
        return "Website is Down"
