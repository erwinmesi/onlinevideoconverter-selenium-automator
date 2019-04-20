from os import listdir, path
import time
import json
from pathlib import Path

class ChromeDownloads:
    def has_pending(self):
        downloads_dir = self.get_downloads_dir()
        filenames = [f for f in listdir(downloads_dir) if f.endswith('.crdownload')]
        return bool(filenames)

    def wait_for_all_to_finish(self):
        while ChromeDownloads().has_pending():
            time.sleep(1)
    
    def get_downloads_dir(self):
        data = Path('config.json').read_text()
        config = json.loads(data)
        return config['downloads_dir']