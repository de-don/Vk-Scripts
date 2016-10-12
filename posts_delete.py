import vk
import time

import config

token = config.VK_TOKENS[1]

api = vk.API(vk.Session(),
             access_token=token,
             v='5.50')

owner = -122672448
offset_wall = 0
s = 0
while 1:
    try:
        res = api.wall.get(
            owner_id=owner,
            count=100,
            offset=offset_wall,
             filter="all"
        )
    except Exception:
        pass
    try:
        # offset_wall += 100
        for r in res["items"]:
            post_id = r["id"]

            t = api.wall.delete(
                owner_id=owner,
                post_id=post_id
            )
            s = s + 1
            print(s, "| Удалено id=%s" % post_id)
            time.sleep(1)
    except Exception:
        pass
