from PIL import Image
import requests
from io import BytesIO

def readUrl(url):
    #from PIL import Image
    #import requests
    #from io import BytesIO
    try:
        if(requests.head(url).status_code == requests.codes.ok):
            response = requests.get(url, timeout=1)
            if(response.status_code == requests.codes.ok):
                if(response.headers["Content-Type"].startswith('image/jpeg') or response.headers["Content-Type"].startswith('image/png')):
                    return Image.open(BytesIO(response.content))
                else: print(url)
    except Exception: pass
    return None

def main():
    lines = []
    with open("data/horse/urls.txt") as f:
        for line in f:
            if(line[:-1].endswith("jpg") or line[:-1].endswith("JPG")):
                lines.append(line[:-1])

    count = 0
    for line in lines:
        count += 1
        print(str(count) + " " + line)
        img = readUrl(line)
        if(img is not None):
            img.save("data/horse/image"+str(count)+".jpg")

if __name__ == "__main__":
    main()
