# -*- coding: utf-8 -*-

try:
    import json
    from urllib import parse
    from selenium import webdriver
    from http.server import HTTPServer, BaseHTTPRequestHandler

except:
    input('import error')

'''Open HTTP service'''
class WebService ():
    def __init__(self,http_service_port = 3993):
        self.http_service_port = http_service_port
        self.http_service_host = '127.0.0.1'
    def run(self):
        httpd = HTTPServer((self.http_service_host, self.http_service_port), HTTPRequestHandler)
        print('Listening port on %d...' % self.http_service_port)
        print('Press Ctrl + C to exit...')
        httpd.serve_forever()

'''Handling Http requests'''
class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if '/' == self.path:
            params = (parse.parse_qs(self.rfile.read(int(self.headers['Content-length'])).decode('UTF-8')))
            if not params.get('url') == None:
                if not params.get('cookie') == None:
                    try:
                        _StartWebdriver = StartWebdriver(params.get('url')[0],params.get('cookie')[0])
                    except:
                        self._SendResponse(200, 'system Error')
                else:
                    self._SendResponse(200,'cookie Error')
            else:
                self._SendResponse(200,'type Error')
    def _SendResponse(self, code,message=None):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps({'code':code,'message':message}).encode('UTF-8'))

'''The browser sets the Cookie to open the corresponding site'''
class StartWebdriver(object):
    def __init__(self,url,cookie,cookie_domain = 'qq.com'):
        self.url = 'http://' + url
        self.cookie = cookie.replace('&amp;','&').strip()
        self.browser = webdriver.Chrome()
        self.cookie_domain = '.' + cookie_domain
        self.run()
    def run (self):
        self.browser.get(self.url)
        self.browser.delete_all_cookies()
        self.cookie = self.handleCookie(self.cookie)
        for key in self.cookie:
            self.browser.add_cookie({'name':key,'value':self.cookie[key],'domain': self.cookie_domain})
        self.browser.get(self.url)
        HTTPRequestHandler._SendResponse(200, 'Start Success')
    def handleCookie(self,cookie):
        return dict([l.split("=", 1) for l in self.cookie.split("; ")])

if __name__ == '__main__':
    (WebService()).run()
