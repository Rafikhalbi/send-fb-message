import requests,re
from bs4 import BeautifulSoup as parser
import asyncio

url = "https://free.facebook.com" # you can use "https://mbasic.facebook.com"

cookie = "" # set your cookie in here !
# cookies datr

mess = "Hello Friend!" # set your message in here !

headers = {
    "cookie": cookie
}


def send_messages(res):
    try:
        reg = requests.get(res, headers=headers)
        url_post_messages = re.search('form method="post" action="(.*?)"', str(reg.text))[1]
        fb_dtsg = re.search(r'name="fb_dtsg" value="(.*?)"', str(reg.text))[1]
        jazoest = re.search(r'name="jazoest" value="(.*?)"', str(reg.text))[1]
        
        tids = re.search(r'name="tids" value="(.*?)"', str(reg.text))[1]
        wwwupp = re.search(r'name="wwwupp" value="(.*?)"', str(reg.text))[1]
        csid = re.search(r'name="csid" value="(.*?)"', str(reg.text))[1]
        data = {
            "fb_dtsg": fb_dtsg,
            "jazoest": jazoest,
            "body": mess,
            "send": "Kirim",
            "tids": tids,
            "wwwupp": wwwupp,
            "platform_xmd": "",
            "referrer": "",
            "ctype": "",
            "cver": "legacy",
            "csid": csid
        }
        post_messages = requests.post(url+url_post_messages, headers=headers, data=data)
        if post_messages.status_code == 200:
            print(f"Succes send to: {url_post_messages}")
        else:
            print(f"Error send to: {url_post_messages}")
    except:
        pass

async def get_pesan():
    try:
        reg = requests.get(url, headers=headers)
        parsing = parser(reg.text, "html.parser")
        for data in parsing.find_all("a", string="Pesan"):
            return data["href"]
    except Exception as e:
        exit(e)
        
def home():
        pes = asyncio.run(get_pesan())
        url_message = f"{url}{pes}"
        #print(url_message)
        reg = requests.get(url_message, headers=headers)
        parsing = parser(reg.text, "html.parser")
        for data in parsing.find_all("a"):
            if "/messages/read/" in str(data):
                try:
                    send_messages(f"{url}{data['href']}")
                except: continue


if __name__ == "__main__":
    home()
