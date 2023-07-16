def create_youtube_video(title, description):
	video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}}
	return video


def like(video):
	if "likes" in video:
		video["likes"] = video["likes"] + 1
	return video



def dislike(video):
	if "dislikes" in video:
		video["dislikes"] = video["dislikes"] + 1
	return video


def add_comment(youtubevideo, username, comment_text):
	if "comments" in youtubevideo:
		youtubevideo["comments"][username] = comment_text
	return youtubevideo




title = input("name your video")
description = input("describe the video")

video = create_youtube_video(title, description)

print(video)

video = like(video)
print(video)

video = dislike(video)
print(video)


username = input("enter your username")
comment = input("write a comment")

video = add_comment(video, username, comment)
print(video)


