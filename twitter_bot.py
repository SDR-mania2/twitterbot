import twitter

#以下四カ所でTwitter APIのキーを指定
auth = twitter.OAuth(consumer_key="key1",consumer_secret="key2",token="key3",token_secret="key4")

t = twitter.Twitter(auth=auth)

#以下で投稿するツイート指定
bunsho="これはテストツイートです。"
t.statuses.update(status=bunsho)

#時間指定はcrontabで瞬殺
#import os
#os.system("echo '0 * * * * * twitter_bot.pyのパス' >> crontabファイルのパス")
#みたいな感じで。
#crond入れんとだめだが。

