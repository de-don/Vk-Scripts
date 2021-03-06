import vk
import time
import config

token = config.VK_TOKENS[5]  #  token from group
api = vk.API(vk.Session(),
             access_token=token,
             v='5.50')

while 1:
    try:
        res = api.messages.getDialogs(
            count=200,
            unread=1
        )
    except Exception:
            pass

    time.sleep(0.6)

    if len(res["items"]) == 0:
        break

    for r in res["items"]:
        msg = r["message"]
        try:
            t = api.messages.markAsRead(
                peer_id=msg["user_id"]
            )
            time.sleep(0.3)
            t = api.messages.markAsAnsweredDialog(
                peer_id=msg["user_id"]
            )
        except Exception:
            pass

        print("[%s] " % t, msg["user_id"], " => ", msg["title"])
        time.sleep(0.5)
    time.sleep(5)