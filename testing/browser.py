# webview_window.py
import webview
import sys

def open_page(url):
    """Creates and starts the pywebview window."""
    window = webview.create_window('Misumi', url)
    webview.start()

if __name__ == '__main__':
    # The URL is passed as a command-line argument from FreeCAD
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        open_page(target_url)
    else:
        print("No URL provided.")
