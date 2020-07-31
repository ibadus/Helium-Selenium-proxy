# Helium-Selenium-proxy

```
There might be some errors in the scripts
```

Using **ip:port:username:password proxy** for your [Chromedriver](https://chromedriver.chromium.org/) for [Selenium](https://selenium-python.readthedocs.io/) and [Helium](https://github.com/mherrmann/selenium-python-helium).

## Installation

+ Download Selenium and Helium
```bash
pip install selenium helium
```

+ Download [Chrome-Webdriver-Proxy](https://github.com/nkpydev/Chrome-Webdriver-Proxy) and add the Utility file to your project

+ Download [Chromedriver](https://chromedriver.chromium.org/) to use Selenium or Helium

## Usage

Get the proxies from the proxies.txt
```python
# VAR FOR THE PROXY PARTS
proxies = []
ip = []
port = []
username = []
psw = []

# PATH TO THE PROXIES.TXT FILE
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
proxies_file = os.path.join(THIS_FOLDER, 'proxies.txt')
#OPEN THE PROXIES.TXT AND READ LINE BY LINE TO GET THE INFOS
file = open(str(proxies_file), "r")
for line in file:
    prox = line.rstrip("\n")
    prox = prox.split(":")
    ip.append(prox[0])
    port.append(prox[1])
    username.append(prox[2])
    psw.append(prox[3])
    proxies.append(line.rstrip("\n"))
file.close()
```
start the browser
```python
# LOAD PROXY
proxy_1 = CPS(ip[0],port[0],username[0],psw[0])
# START SELENIUM BROWSER WITH PROXY
driver = proxy_1.set_proxy()
# CHANGE SELENIUM TO HELIUM 
set_driver(driver)
```
For more informations about chrome_proxy_driver_setup (CPS) please visit this [repo](https://github.com/nkpydev/Chrome-Webdriver-Proxy)

## Thanks
Thanks to [nkpydev](https://github.com/nkpydev) for [Chrome-Webdriver-Proxy](https://github.com/nkpydev/Chrome-Webdriver-Proxy)
