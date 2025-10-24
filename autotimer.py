from __future__ import print_function
from AppKit import NSWorkspace, NSAppleScript
from urllib.parse import urlparse
import time
from Foundation import *
from os import system
import subprocess, time

# active_window_name = ""
# while True:
#     new_window_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])

#     if active_window_name != new_window_name:
#         active_window_name = new_window_name
#         print(active_window_name)
#         if active_window_name == 'Google Chrome':
#             textOfMyScript = """tell app 'google chrome' to get the url of the active tab window 1"""
#             s = NSAppleScript.initWithSource_(NSAppleScript.alloc(), textOfMyScript)
#             results, err = s.executeAndReturnError_(None)

#             print(results.stringValue())

def chrome_tab():
    script = '''
    tell application "Google Chrome"
        if (count of windows) > 0 then 
            return URL of active tab of front window
        else
            return missing value
        end if 
    end tell
        '''
    
    s = NSAppleScript.alloc().initWithSource_(script)
    result, err = s.executeAndReturnError_(None)
    if err or result is None:
        return None
    
    url = result.stringValue()
    # if not url:
        # return None 
    
    return urlparse(url).netloc if url else None

def app_file_name():
    osa = subprocess.run([
        "osascript", "-e",
        'tell application "System Events" to tell (first process whose frontmost is true)'
        'to if exists (window 1) then return name of window 1'
    ], capture_output=True, text=True)
    return osa.stdout.strip()

last_domain = None

# last = ""
try:
    while True:
        app = NSWorkspace.sharedWorkspace().activeApplication().get('NSApplicationName')
        # if app == "Google Chrome":
        # if last_domain != app:
        #     last_domain = app
        #     print(last_domain)
        #     domain = chrome_tab()
        #     if domain and domain != "Google Chrome":
        #         last = domain
        #         print(domain)
        info = app_file_name()

        if app == "Google Chrome":
            domain = chrome_tab()
            if domain:
                info = domain
        
        if info and info != last_domain:
            print(f'{app}: {info}')
            last_domain = info

        time.sleep(5)        

except KeyboardInterrupt:
    stop_flag = True
    print("Program stopped")

