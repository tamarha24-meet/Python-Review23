def create_youtube_video(title, description):
	video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {}, "hashtag" : []}
	for i in range(5):
		flag = input("would you like to add a hashtag? yes/no: ")
		if flag == "yes":
			hashtag = input("write your hashtag: ")
			video["hashtag"].append(hashtag)
		else:
			break 


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

def similarity_to_video(video, videos):
	length = len(video["hashtag"])
	for vid in videos:  #iterate trough every video
		same = 0  
		for ht in video["hashtag"]: #for every hashtag of that video
			for inner_ht in vid["hashtag"]:
				if inner_ht == ht:
					same += 1
		precentage = same/length
		print()
		print("your video have a " + str(precentage) + " precent of similarty to the video: " + str(vid["title"]))
		print()


videos = []

stop = "False"
restart = "False"

while stop == "False": #to stop the entire program
	check = input("do you want to create a new video? (yes/no) ")
	print()
	if check == "yes":
		title = input("name your video: ")
		description = input("describe the video: ")
		video = create_youtube_video(title, description)

		print()
		print("you've created your video succesfully!")
		print("--------------------------")
		print("title: " + str(video["title"]))
		print("description: " + str(video["description"]))
		print("hashtags: " + str(video["hashtag"]))
		print("amount of likes: " + str(video["likes"]))
		print("amount of dislikes: " + str(video["dislikes"]))
		print("current comments: " + str(video["comments"]))
		print("--------------------------")
		print()

		similarity_to_video(video, videos)
		videos.append(video)

		while restart == "False":
			what = input("what would you like to do now? (like/dislike/comment/restart): ")
			print()


			if what == "like":
				video = like(video)
				print("the video has " + str(video["likes"]) + " likes")

			elif what == "add 495 likes":
				video["likes"] = video["likes"] + 495
				print("the video has " + str(video["likes"]) + " likes")

			elif what == "dislike":
				video = dislike(video)
				print("the video has " + str(video["dislikes"]) + " dislikes")

			elif what == "comment":
				username = input("enter your username: ")
				comment = input("write a comment: ")

				video = add_comment(video, username, comment)
				print("these are the comments " + str(video["comments"]))
			else:
				restart = "True"
	else:
		stop = "True"




	
