import twitter

#以下でTwitter APIのキーを指定
auth = twitter.OAuth(consumer_key="",consumer_secret="",token="",token_secret="")

t = twitter.Twitter(auth=auth)

#以下で投稿するツイート指定
bunsho="これはテストツイートです。"
t.statuses.update(status=bunsho)

#時間指定はcrontabで瞬殺
#import os
#os.system("echo '* * * * * twitter_bot.pyのパス' >> crontabファイルのパス")
#みたいな感じで。
#crond入れんとだめだが。

