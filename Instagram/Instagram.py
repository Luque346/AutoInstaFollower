#
#─█▀▀█ █──█ ▀▀█▀▀ █▀▀█ 　 ░█▀▀▀ █▀▀█ █── █── █▀▀█ █───█ 
#░█▄▄█ █──█ ──█── █──█ 　 ░█▀▀▀ █──█ █── █── █──█ █▄█▄█ 
#░█─░█ ─▀▀▀ ──▀── ▀▀▀▀ 　 ░█─── ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ─▀─▀─
#If you don't know how to use it, read the manual on the



from instapy import InstaPy

session = InstaPy(username = "Username", password = "PassWord")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage = 100)
session.like_by_tags(["follow4followback", "followforfollowback"], ["followbackinstantly"], amount= 3)
session.set_dont_like(["grasa"], ["nsfw"])

session.end

