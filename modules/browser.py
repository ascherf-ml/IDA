import webbrowser
from modules.speechprocessing import *

def browser(page):
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    webbrowser.open_new_tab(f"https://www.{page}.com")
    time.sleep(5)
