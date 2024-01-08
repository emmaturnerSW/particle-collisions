for key, value in ext.items():
    value = value.split()
    ext[key] = value


def add_to_dir(ex, src_path, path):
def rename(search, ex, dest_path):
    count = 0
    os.chdir(dest_path)
    for filename in os.listdir():
        if filename.find(search, 0, len(search) - 1):
            count = count + 1

      class Downloder:
    def __init__(self):
        self.url = str(input("Enter the url of video : "))
        self.down = pytube.Double(
            self.url, on_progress_callback=YouTubeDownloder.onProgress
        )
        self.showTitle()
