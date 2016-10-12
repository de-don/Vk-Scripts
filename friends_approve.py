import vk
import time
import config

token = config.VK_TOKENS[4]
api = vk.API(vk.Session(),
             access_token=token,
             v='5.50')

while 1:
    s = 0
    try:
        res = api.friends.getRequests(
            count=1000,
            out=0
        )
    except Exception:
            pass

    time.sleep(0.6)

    for r in res["items"]:
        try:
            t = api.friends.add(
                user_id=r
            )
        except Exception:
            pass

        print("[%s] " % t, r)
        s += 1
        time.sleep(0.5)
    print("Added %s users" % s)
    time.sleep(300)