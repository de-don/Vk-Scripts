import vk
import time
import config

tokens = config.VK_TOKENS.values()

api = []
for token in tokens:
    api.append(vk.API(vk.Session(),
                      access_token=token,
                      v='5.50'
                      ))


def MultiApi(apis):
    i = 0
    n = len(apis)
    while 1:
        yield apis[i % n]
        i += 1


api = MultiApi(api)
owner = -23054528
offset = 0

s = 0
while 1:
    try:
        res = next(api).photos.get(
            owner_id=owner,
            album_id="wall",
            rev=0,
            count=10,
            offset=offset
        )

        k = res["count"]
    except Exception:
        pass
    try:
        for r in res["items"]:
            id = r["id"]

            t = next(api).photos.delete(
                owner_id=owner,
                photo_id=id
            )
            if t == 1:
                k -= 1
                print(k, "| Удалено id=%s" % id, t)
                time.sleep(0.7)
    except Exception:
        pass
