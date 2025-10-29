from AppKit import NSWorkspace, NSAppleScript
from urllib.parse import urlparse
from datetime import datetime
import subprocess, time

class ActivityTracker:
    # Tracks to the active app time usage and logs onto the database

    def __init__(self, db_manager):
        self.db = db_manager
        self.last_app = None
        self.last_info = None
        self.start = None
        self.stop_flag = False

    def app_file_name(self):
        osa = subprocess.run([
            "osascript", "-e",
            'tell application "System Events" to tell (first process whose frontmost is true)'
            'to if exists (window 1) then return name of window 1'
        ], capture_output=True, text=True)
        return osa.stdout.strip()
    
    def chrome_tab(self):
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
        
        return urlparse(url).netloc if url else None 
    
 # Main Loop

    def run(self, interval=10):
        print("Time Tracker started... (Ctrl + C to stop)/n")

        try:
            while not self.stop_flag:
                app = NSWorkspace.sharedWorkspace().activeApplication().get('NSApplicationName')
                info = self.app_file_name()

                if app == "Google Chrome":
                    domain = self.chrome_tab()
                    if domain:
                        info = domain

                if app != self.last_app or info != self.last_info:
                    now = datetime.now()

                    if self.last_app is not None:
                        self.db.save_session(self.last_app, self.last_info, self.start, now)

                    self.last_app, self.last_info, self.start = app, info, now
                    print(f'Active: {app} - {info}')
                
                time.sleep(interval)

        except KeyboardInterrupt:
            now = datetime.now()
            if self.last_app:
                self.db.save_session(self.last_app, self.last_info, self.start, now)
            print('Time Tracking now stopped, please restart if needed')                

        finally:
            self.db.close()


