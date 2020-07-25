# --- Chrome WebDriver Specific Imports from Selenium --- #
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
# --- Zip Import for Extension --- #
import zipfile
# --- Generic Imports --- #
import os
from os.path import exists
# --- Project Internal Imports --- #
from utility.config import BASE_DIR


# --- ChromeProxySetup Class --- #
class ChromeProxySetup(object):
    
    def __init__(self,proxy_host=None,proxy_port=None,proxy_auth_user=None,proxy_auth_pwd=None):
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_auth_user = proxy_auth_user
        self.proxy_auth_pwd = proxy_auth_pwd
        self.chrome_options = ChromeOptions()
        self.chrome_options.add_argument('--disable-infobars')
        self.chrome_options.add_argument('--dns-prefetch-disabled')
        self.extension_file = ''
    
    def set_proxy(self):
        proxy = {
                    'host': self.proxy_host,
                    'port': self.proxy_port,
                    'user': self.proxy_auth_user,
                    'pass': self.proxy_auth_pwd
                }   
        
        proxy_meta = proxy

        manifest_json = '''
                                {
                                    "version": "1.0.0",
                                    "manifest_version": 2,
                                    "name": "Chrome Proxy",
                                    "permissions": [
                                        "proxy",
                                        "tabs",
                                        "unlimitedStorage",
                                        "storage",
                                        "<all_urls>",
                                        "webRequest",
                                        "webRequestBlocking"
                                    ],
                                    "background": {
                                        "scripts": ["background.js"]
                                    },
                                    "minimum_chrome_version":"22.0.0"
                                }
                            '''
        
        background_js = '''
                            var config = {
                                mode:"fixed_servers",
                                rules:{
                                    singleProxy:{
                                        scheme:"http",
                                        host:"%s",
                                        port:parseInt(%s)                
                                    },
                                bypassList:["localhost"]
                                }
                            };
                            chrome.proxy.settings.set({value:config, scope:"regular"},
                            function() {});
                            function callbackFn(details) {
                                return{
                                    authCredentials:{
                                        username: "%s",
                                        password: "%s"
                                    }
                                };
                            }
                            chrome.webRequest.onAuthRequired.addListener(
                                callbackFn,
                                {urls:["<all_urls>"]},
                                ["blocking"]
                            );
                            chrome.runtime.onInstalled.addListener(function(){
                                chrome.tabs.reload()
                            })
                        ''' % (self.proxy_host, self.proxy_port, self.proxy_auth_user, self.proxy_auth_pwd)

        proxy = proxy_meta

        proxy_zip_filename = ('%s.zip' %self.proxy_host)

        self.extension_file = os.path.join(BASE_DIR, proxy_zip_filename)
        
        if not exists(self.extension_file):
            with zipfile.ZipFile(self.extension_file, 'w') as prxtn:
                prxtn.writestr('manifest.json', manifest_json)
                prxtn.writestr('background.js', background_js)
        
        self.chrome_options.add_extension(self.extension_file)

        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)

        return self.browser
