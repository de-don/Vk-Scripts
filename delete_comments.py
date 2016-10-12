import vk
import time

import config

token = config.VK_TOKENS[1]
api = vk.API(vk.Session(),
             access_token=token,
             v='5.50')

owner = -23054528
offset_wall = 300
s = 0
while 1:
    res = api.wall.get(
         owner_id=owner,
         count=100,
         offset=offset_wall
    )
    time.sleep(0.5)
    offset_wall += 100

    for r in res["items"]:
        post_id = r["id"]

        print("post_id=%s"%post_id, "| Comments = %s"% r["comments"]["count"])
        if r["comments"]["count"] > 0:

            # получаем комменты и удаляем нахуй
            while True:
                try:
                    comments = api.wall.getComments(
                        owner_id=owner,
                        post_id=post_id,
                        count=100
                    )
                    time.sleep(0.5)
                except:
                    pass

                if len(comments["items"]) == 0:
                    break

                if len(comments["items"]) > 10:
                    t = api.wall.delete(
                        owner_id=owner,
                        post_id=post_id
                    )
                    break


                for comment in comments["items"]:
                    comment_id = comment['id']
                    try:
                        t = api.wall.deleteComment(
                            owner_id=owner,
                            comment_id=comment_id
                        )
                    except:
                        pass
                    time.sleep(0.5)
                    s+=t
                    print(s,"| Удалено id=%s"%comment_id)