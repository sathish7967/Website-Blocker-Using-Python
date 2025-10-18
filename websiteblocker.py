import time
from datetime import datetime as dt
hostd_path=r"C:\Windows\System32\drivers\etc"
redirect=”127.0.0.1”
websites_lists=["www.facebook.com","facebook.com","instagram.com","www.instagram.com","www.youtube.com","youtube.com","www.Myntra.com","myntra.com"]
while True;
    if dt(dt.now().year,dt.now().month,dt.nw().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("working hours...")
        with open(hosts_path,'r+')as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
        else:
            with open(hosts_path,'r+') as file:
                content=file.readline()
                file.seek(0)
                for line in content:
                    if not any(website in kine for website in wesites_lists):
                          file.write(line)
                        file.truncate()
            print("fun hours...")
file.write(redirect+""+website+"\n")
        time.sleep(5)
