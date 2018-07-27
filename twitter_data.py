import json

#(r=read)
tweetFile = open("tweets.json","r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id: ", tweeData[0]["id"])
print("Tweet text: ", tweetData[0]["text"])

for i in range(len(tweetData)):
        print("Tweet text:", tweetDatata[i]["text"])

for tweet in tweetData:
    print("Tweet text: ", tweet["text"])
