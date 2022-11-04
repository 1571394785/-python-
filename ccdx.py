import json
import requests
def jwxt(xh, pwd):
    rep = requests.get("http://cdjwc.ccu.edu.cn/app.do?method=authUser&xh="+xh+"&pwd="+pwd)
    res = json.loads(rep.text)
    token=res["token"]
    urll = "http://cdjwc.ccu.edu.cn/app.do?method=getKbcxAzc&xh=012140817&xnxqid=2022-2023-1&zc=5"
    header = {
        "token":token
    }
    jwxt = requests.get(url=urll,headers=header)
    kb = json.loads(jwxt.text)
    #写出课表
    with open("kb.txt","w") as f:
        f.write(jwxt.text)
    print(kb)
    return jwxt.text
def fomat(res):
    json1= json.loads(res)
    # 查找json[]中列表的长度
    len1 = len(json1)
    week = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    list=""
    try:
        for i in range(len1):
            week1=int( json1[i]["kcsj"][0])-1
            print(week[week1],json1[i]['kcmc'],json1[i]['kssj'],json1[i]['jssj'],json1[i]['jsxm'])
            list=list+week[week1]+" "+json1[i]['kcmc']+" "+json1[i]['kssj']+"-"+json1[i]['jssj']+" "+json1[i]['jsxm']+"\r\n"
        return list
    except:
        return "课表获取失败，请检查学号和密码是否正确"
if __name__=="__main__":
    xh = input("请输入学号：")
    pwd = input("请输入密码：")
    jwxt(xh, pwd)
    f=open("kb.txt","r")
    res=f.read()
    f.close()
    fomat(res)
    