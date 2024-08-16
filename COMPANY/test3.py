import test2
import webbrowser

chrome_path ="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
#chrome_path ="C:/Users/sys/AppData/Local/Google/Chrome/Application/chrome.exe %s"


fileobj=open('web2.html','w')
fileobj.write(test2.web2)
fileobj.close()
webbrowser.get(chrome_path).open_new_tab('web2.html')


