import requests

def get_tigo_link():
    # URL de respaldo si la API no responde
    backup_url = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/py_tigosports.m3u8"
    api_url = "https://api.tigosports.com.py/api/v1/get-live-stream?channelId=1"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Kali Linux x86_64) IPTV-Project/1.0",
        "Origin": "https://www.tigosports.com.py"
    }

    try:
        r = requests.get(api_url, headers=headers, timeout=5)
        if r.status_code == 200:
            return r.json().get('url', backup_url)
        return backup_url
    except:
        return backup_url

if __name__ == "__main__":
    print(get_tigo_link())
