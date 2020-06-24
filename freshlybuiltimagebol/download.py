from requests import get
from os import makedirs
from os.path import join,isdir
from tqdm import tqdm

download_urls={
    'east': 'https://raw.githubusercontent.com/FreshlyBuilt/freshlybuiltimagebol/master/freshlybuiltimagebol/models/frozen_east_text_detection.pb',
}

if not isdir('freshlybuiltimagebol/models'):
    makedirs('freshlybuiltimagebol/models')
class Download:
    def download(item):
        chunk_size=1024
        url=download_urls[item]
        filename=url.split('/')[-1]
        path=join('freshlybuiltimagebol','models',filename)
        r = get(url, stream=True)
        total_size = int(r.headers['content-length'])

        with open(path, 'wb') as f:
            for data in tqdm(iterable = r.iter_content(chunk_size),total=total_size/chunk_size, unit = 'KB'):
                f.write(data)
        print ("Successfully downloaded "+ filename)
