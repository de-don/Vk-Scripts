import vk
import time

import config

token = config.VK_TOKENS[1]

api = vk.API(vk.Session(),
             access_token=token,
             v='5.50')


while 1:
    res = api.groups.getBanned(
        group_id=28870275,
        count=200,
        unread=1
    )

    if len(res["items"]) == 0:
        break

    for r in res["items"]:
        id = r["id"]
        t = api.groups.unbanUser(
            group_id=28870275,
            user_id=id
        )

        print("[%s] " % t, id)
        time.sleep(0.5)