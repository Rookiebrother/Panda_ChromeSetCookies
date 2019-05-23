

try:
    import tkinter
    from WebService import *
except:
    exit(0)

class WebServiceGui (object):
    def __init__(self,titleText = 'Title',width = '315',height = '200'):
        self.title = titleText
        self.geometry = width + 'x' + height
        self.tk = tkinter.Tk()


    def initApplication(self):
        self.tk.title(self.title)
        self.tk.geometry(self.geometry)
        self.tk.resizable(width=False,height=False)

        login = tkinter.Button(self.tk, text ="Go!",command=self.startAppaction,width=10,height=1)
        login.place(x=50,y=145)

        about = tkinter.Button(self.tk, text ="Go! GitHub",command=self.startAppaction,width=10,height=1)
        about.place(x=170,y=145)

        urlName = tkinter.Label(self.tk,text='Site Address')
        urlName.place(x=10,y=20)
        self.url = tkinter.Entry(self.tk)
        self.url.place(x=100,y=18)

        cookieName = tkinter.Label(self.tk,text='Site Cookie')
        cookieName.place(x=10,y=60)
        self.cookie = tkinter.Entry(self.tk)
        self.cookie.place(x=100,y=58)

        domainName = tkinter.Label(self.tk,text='Site Domain')
        domainName.place(x=10,y=100)
        self.domain = tkinter.Entry(self.tk)
        self.domain.place(x=100,y=98)

        self.tk.mainloop()

    def startAppaction (self):
        url    = self.url.get()
        domain = self.domain.get()
        cookie = self.cookie.get()
        (StartWebdriver(url=url,cookie=cookie,cookie_domain=domain)).run()


if __name__ == '__main__':
    titleText = 'Panda'
    (WebServiceGui(titleText)).initApplication()