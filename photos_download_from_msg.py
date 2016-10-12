import vk
import time
from urllib.request import urlretrieve

import config

token = config.VK_TOKENS[1]
api = vk.API(vk.Session(),
             access_token=token,
             v='5.50')

chat_id = 2000000000 + 167
offset = 0
s = 0
sizes = "wzyrqpoxms"

while 1:
    res = api.messages.getHistoryAttachments(
        peer_id=chat_id,
        media_type="photo",
        count=200,
        start_from=offset,
        photo_sizes=1
    )
    time.sleep(0.5)

    for r in res["items"]:
        photos = dict.fromkeys(list(sizes))

        for photo in r['photo']['sizes']:
            photos[photo['type']] = photo['src']

        src = ""
        for i in sizes:
            if photos[i] != None:
                src = photos[i]
                break
        if src:
            id = r['photo']['id']
            urlretrieve(src, "./pic/"+str(id)+".jpg")
            print(s, "|", src)
            s += 1
            offset = id

    offset = res["next_from"]
    if len(res["items"]) == 1:
        break