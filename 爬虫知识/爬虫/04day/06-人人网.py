import urllib.request
import parser

url = 'http://zhibo.renren.com/anchor/946609648'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Cookie':'anonymid=jpxm50jfaer5jk; depovince=BJ; _r01_=1; ick_login=d17257ec-2298-4d2d-873b-745f4f446c5e; t=5e37059641b2b5d05f79ae3d0d639eae9; societyguester=5e37059641b2b5d05f79ae3d0d639eae9; id=969189269; xnsid=30b1107c; ch_id=10016; JSESSIONID=abcB-SqAIZZQxhebVtpFw; jebe_key=a5fd2427-222f-4af6-9aa5-9defdf717c79%7Cc40ddec597de90e5719f04dd3bfd55fc%7C1545371322944%7C1%7C1545371322141; wp_fold=0; XNESSESSIONID=1fefe314259a; jebecookies=a1c777f2-18be-48b7-a3db-99aef069de50|||||; ver=7.0; loginfrom=null; WebOnLineNotice_969189269=1; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1545371857; _ga=GA1.2.142020713.1545371857; _gid=GA1.2.41838757.1545371857; _ga=GA1.3.142020713.1545371857; _gid=GA1.3.41838757.1545371857; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1545371860'
}


request = urllib.request.Request(url=url,headers=headers)

respose = urllib.request.urlopen(request)

content = respose.read().decode()

with open('xiaoge.html','w') as f:
    f.write(content)