def browser(page):
    webbrowser.open_new_tab(f"https://www.{page}.com")
    speak(f"{page} is open now")
    time.sleep(5)
