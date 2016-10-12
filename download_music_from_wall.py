import vk
import time
import re
import os.path
from urllib.request import urlretrieve

import config

token = config.VK_TOKENS[1]

api = vk.API(vk.Session(),
             access_token=token,
             v='5.50')

owner = -30089088
count = 100
path = "F:\\"

offset = 1
s = 0
while s < count:
    res = api.wall.get(
        owner_id=owner,
        count=100,
        offset=offset
    )
    time.sleep(0.5)

    for post in res["items"]:
        try:
            attach = post["attachments"]

            for att in attach:
                if att["type"] == "audio":
                    audio = att["audio"]

                    url = audio["url"]
                    if url:
                        name = audio["artist"] + " - " + audio["title"]
                        name = re.sub(r"vk\.com\/[\w\d\.\_]*", '', name)
                        name = re.sub(r"[^\w\s\-]", '', name)

                        dir = path + name + ".mp3"
                        if not os.path.exists(dir):
                            print(name)
                            urlretrieve(url, dir)
                            s+=1
        except Exception:
            pass

    offset += len(res['items'])