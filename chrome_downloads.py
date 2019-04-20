from os import listdir, path
import time

class ChromeDownloads:
    def has_pending(self):
        return bool([f for f in listdir('C:\\Users\\mesia\\Downloads') if f.endswith('.crdownload')])

    def wait_for_all_to_finish(self):
        while ChromeDownloads().has_pending():
            time.sleep(1)