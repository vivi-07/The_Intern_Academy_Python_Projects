from instapy import InstaPy

session = InstaPy(username="username", password="password")
session.login()

#Like by tags
session.like_by_tags(["datascience", "java"], amount=10, interact=True)

#Set comment
session.set_do_comment(True, percentage=100)
session.set_comments(["Nice", "Amazing", "Super"])

#Set follow
session.set_do_follow(enabled=True, percentage=100)

session.end()



