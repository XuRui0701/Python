# author:JiuAi
# QQ:3295370381
import requests
import json
username = input('元本账号:')
password = input('元本密码:')
ip = input('请输入熊猫代理api:')
id = input('请输入藏品ID:')
ip_url = ip
resp = requests.get(url=ip_url)
print(resp.text)
content = json.loads(resp.text)
result = content['obj']
for index in content['obj']:
    ip = index['ip']
    port = index['port']
    # print(ip)
    # print(port)

    proxies = {
        'http': 'http://'+ip + ':' + port
    }

    print(proxies)
    # 13位时间戳
    # millis = int(round(time.time() * 1000))
    # print(millis)
    login_url = 'https://api.3rdplanet.cn/api/v1.0/user/loginByPassword'
    dic = {"userTel": username, "passWord": password,
           "verificationCode": "", "device": "APP"}
    login_data = json.dumps(dic)
    login_headers = {
        'Host': 'api.3rdplanet.cn',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.1171 SLBChan/105',

                'Origin': 'https://art.ybspace.cn',
                'Referer': 'https://art.ybspace.cn/',
                'content-Type': "application/json;charset=utf-8",

    }

    login_resp = requests.post(
        url=login_url, headers=login_headers, data=login_data, proxies=proxies)

    content = json.loads(login_resp.text)
    Token = content['data']['token']
    print(Token)

    for i in range(1, 9999):
        selectAll_url = 'https://api.3rdplanet.cn/api/v1.0/product/selectAll'
        dic = {"orderBy": 0, "pageNum": 1, "pageSize": 10,
               "totalPage": 1, "categoryId": id}
        selectAll_data = json.dumps(dic)
        selectAll_headers = {
            'Host': 'api.3rdplanet.cn',
                    'Connection': 'keep-alive',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.1171 SLBChan/105',
                    'token': Token,
                    'Origin': 'https://art.ybspace.cn',
                    'Referer': 'https://art.ybspace.cn/',
                    'content-Type': "application/json;charset=utf-8",

        }

        selectAll_resp = requests.post(
            url=selectAll_url, headers=selectAll_headers, data=selectAll_data, proxies=proxies)
        print(selectAll_resp.text)
        content = json.loads(selectAll_resp.text)
        for index in content['data']['list']:
            productId = index['productId']
            print(productId)

            pay_url = 'https://api.3rdplanet.cn/api/v1.0/order/createOrder'
            dic = {"payType": 2, "productId": productId,
                   "systemType": "H5", "type": 0, "userId": 1399113}
            pay_data = json.dumps(dic)
            pay_headers = {
                'Host': 'api.3rdplanet.cn',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.1171 SLBChan/105',
                'token': Token,
                'Origin': 'https://art.ybspace.cn',
                'Referer': 'https://art.ybspace.cn/',
                'content-Type': "application/json;charset=utf-8",

            }

            pay_resp = requests.post(
                url=pay_url, headers=pay_headers, data=pay_data, proxies=proxies)
            print(pay_resp.text)
            content = json.loads(pay_resp.text)
            result = content['data']
            print('支付链接:' + str(result))
