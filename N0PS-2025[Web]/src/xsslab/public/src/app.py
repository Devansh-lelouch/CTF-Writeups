from flask import Flask, render_template, request
import urllib.parse
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import re

app = Flask(__name__)

def filter_2(payload):
    regex = ".*(script|(</.*>)).*"
    if re.match(regex, payload):
        return "Nope"
    return payload

def filter_3(payload):
    regex = ".*(://|script|(</.*>)|(on\w+\s*=)).*"
    if re.match(regex, payload):
        return "Nope"
    return payload

def filter_4(payload):
    regex = "(?i:(.*(/|script|(</.*>)|document|cookie|eval|string|(\"|'|`).*(('.+')|(\".+\")|(`.+`)).*(\"|'|`)).*))|(on\w+\s*=)|\+|!"
    if re.match(regex, payload):
        return "Nope"
    return payload

@app.route('/', methods=['GET', 'POST'])
def xss1():
    if request.method == 'GET':
        payload = request.args.get('payload')
        if not payload:
            payload = ""
        return render_template("xss1.html", payload=payload)
    elif request.method == 'POST':
        try:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox") # linux only
            chrome_options.add_argument("--headless=new") # for Chrome >= 109
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("http://localhost/")
            url = "http://localhost/?payload=" + urllib.parse.quote_plus(request.form["payload"])
            driver.add_cookie({"name": "xss2", "value": "/xss2", "domain": "localhost"})
            driver.get(url)
            #print(driver.page_source.encode("utf-8"))
            driver.quit()
            return 'Page visited!'
        except:
            return 'An error occured.'


@app.route("/xss2", methods=['GET', 'POST'])
def xss2():
    if request.method == 'GET':
        payload = request.args.get('payload')
        if not payload:
            payload = ""
        return render_template("xss2.html", payload=filter_2(payload))
    elif request.method == 'POST':
        try:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox") # linux only
            chrome_options.add_argument("--headless=new") # for Chrome >= 109
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("http://localhost/")
            url = "http://localhost/xss2?payload=" + urllib.parse.quote_plus(request.form["payload"])
            driver.add_cookie({"name": "xss3", "value": "/xss3", "domain": "localhost"})
            driver.get(url)
            #print(driver.page_source.encode("utf-8"))
            driver.quit()
            return 'Page visited!'
        except:
            return 'An error occured.'
        
@app.route("/xss3", methods=['GET', 'POST'])
def xss3():
    if request.method == 'GET':
        payload = request.args.get('payload')
        if not payload:
            payload = ""
        return render_template("xss3.html", payload=filter_3(payload))
    elif request.method == 'POST':
        try:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox") # linux only
            chrome_options.add_argument("--headless=new") # for Chrome >= 109
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("http://localhost/")
            url = "http://localhost/xss3?payload=" + urllib.parse.quote_plus(request.form["payload"])
            driver.add_cookie({"name": "xss4", "value": "/xss4", "domain": "localhost"})
            driver.get(url)
            #print(driver.page_source.encode("utf-8"))
            driver.quit()
            return 'Page visited!'
        except:
            return 'An error occured.'
        
@app.route("/xss4", methods=['GET', 'POST'])
def xss4():
    if request.method == 'GET':
        payload = request.args.get('payload')
        if not payload:
            payload = ""
        return render_template("xss4.html", payload=filter_4(payload))
    elif request.method == 'POST':
        try:
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox") # linux only
            chrome_options.add_argument("--headless=new") # for Chrome >= 109
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("http://localhost/")
            url = "http://localhost/xss4?payload=" + urllib.parse.quote_plus(request.form["payload"])
            driver.add_cookie({"name": "flag", "value": "N0PS{placeholder}", "domain": "localhost"})
            driver.get(url)
            #print(driver.page_source.encode("utf-8"))
            driver.quit()
            return 'Page visited!'
        except:
            return 'An error occured.'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)