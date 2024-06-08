import requests
import time

# URL for HTTP GET request
#填写校园网登录地址
url = ""


def check_website_accessibility_no_redirect():
    """
    检查网站是否可访问，不跟随重定向。
    
    该函数尝试访问https://www.baidu.com，并检查响应状态码。
    - 如果状态码为200，表示网站可访问且没有重定向。
    - 如果状态码为301、302、307、308中的任意一个，表示网站尝试重定向，但被禁止，视为不可访问。
    - 如果出现其他状态码或请求异常，也视为网站不可访问。
    
    返回:
    - True: 如果网站可访问且没有重定向。
    - False: 如果网站不可访问或尝试重定向。
    """
    try:
        # 发起GET请求，设置超时时间为5秒，不允许重定向。
        response = requests.get("https://www.baidu.com", timeout=5, allow_redirects=False)
        # 如果响应状态码为200，表示请求成功，网站可访问。
        if response.status_code == 200:
            return True
        # 如果响应状态码为重定向状态码之一，打印提示信息并返回False。
        elif response.status_code in [301, 302, 307, 308]:
            print(f"{url} 尝试进行重定向，但已被禁止。")
            return False
        # 如果响应状态码既不是200也不是重定向状态码，返回False。
        else:
            return False
    except requests.exceptions.RequestException as e:
        # 如果请求过程中发生异常，返回False。
        return False


def send_http_request(url):
    """
    发送HTTP GET请求并禁止重定向。
    
    :param url: 请求的URL。
    """
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            print("HTTP GET登录请求发送成功。")
        else:
            print(f"HTTP GET登录请求失败，状态码: {response.status_code}")
    except Exception as ex:
        print(f"HTTP GET请求失败: {ex}")


# 循环检测外网连接
while True:
    if check_website_accessibility_no_redirect():
        print("连接到外网成功。")
        break
    else:
        print("无法连接到外网。")
        # 发送HTTP GET请求
        send_http_request(url)
        # 等待一段时间后再次尝试
        time.sleep(1)  # 延迟5秒再尝试