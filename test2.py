__author__ = 'ideabove01'

from datetime import datetime

from pymongo import MongoClient

env = 'production'
if env == 'localhost':
    MONGODB_URI = 'mongodb://127.0.0.1:27017/listr'
elif env == 'development':
    MONGODB_URI = 'mongodb://54.186.79.239:27017/listr'
elif env == 'production':
    MONGODB_URI = 'mongodb://mongo.swizzle.fm:27017/listr'



from datetime import datetime, timedelta

def main():
    client = MongoClient(MONGODB_URI)
    db = client.listr
    notifications = db['notifications']
    results = notifications.find({}, {'action' : 1 })
    results2 = notifications.find({}, {'action' : 1, 'recent' : 1 })

    action = ['ADD_SONG_TO_PLAYLIST_YOU_LIKE', 'ADD_SONG_TO_PLAYLIST', 'LIKE_PLAYLIST', 'INVITED', 'FOLLOW_ME', 'ADD_COMMENT_TO_PLAYLIST']

    # COUNT2 / COUNT3 / COUNT5 / COUNT 6

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0

    for i in results :
        if i['action'] == action[0] :
            count1 = count1 + 1
        elif i['action'] == action[1] :
            count2 = count2 + 1
        elif i['action'] == action[2] :
            count3 += 1
        elif i['action'] == action[3] :
            count4 += 1
        elif i['action'] == action[4] :
            count5 += 1
        elif i['action'] == action[5] :
            count6 += 1
    a = str(count2)
    b = str(count3)
    c = str(count5)
    d = str(count6)

    a0 = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    l0 =0
    l1 =0
    l2 =0
    l3 =0
    l4 =0
    l5 =0
    l6 =0
    f0 =0
    f1 =0
    f2 =0
    f3 =0
    f4 =0
    f5 =0
    f6 =0
    c0 =0
    c1 =0
    c2 =0
    c3 =0
    c4 =0
    c5 =0
    c6 =0
    for i in results2 :
        for o in range(4):
            if i['recent'] >= datetime.now() - timedelta(days=1) and i['recent'] <= datetime.now() :
                if i['action'] == 'ADD_SONG_TO_PLAYLIST':
                    a0 += 1
                elif i['action'] == 'LIKE_PLAYLIST' :
                    l0 +=1
                elif i['action'] == 'FOLLOW_ME':
                    f0 +=1
                elif i['action'] == 'ADD_COMMENT_PLAYLIST' :
                    c0 +=1
            elif i['recent'] >= datetime.now() - timedelta(days=2) and i['recent'] <= datetime.now()-timedelta(days=1) :
                if i['action'] == 'ADD_SONG_TO_PLAYLIST':
                    a1 += 1
                elif i['action'] == 'LIKE_PLAYLIST' :
                    l1 +=1
                elif i['action'] == 'FOLLOW_ME':
                    f1 +=1
                elif i['action'] == 'ADD_COMMENT_PLAYLIST' :
                    c1 +=1
            elif i['recent'] >= datetime.now() - timedelta(days=3) and i['recent'] <= datetime.now()-timedelta(days=2) :
                if i['action'] == 'ADD_SONG_TO_PLAYLIST':
                    a2 += 1
                elif i['action'] == 'LIKE_PLAYLIST' :
                    l2 +=1
                elif i['action'] == 'FOLLOW_ME':
                    f2 +=1
                elif i['action'] == 'ADD_COMMENT_PLAYLIST' :
                    c2 +=1
            elif i['recent'] >= datetime.now() - timedelta(days=4) and i['recent'] <= datetime.now()-timedelta(days=3) :
                if i['action'] == 'ADD_SONG_TO_PLAYLIST':
                    a3 += 1
                elif i['action'] == 'LIKE_PLAYLIST' :
                    l3 +=1
                elif i['action'] == 'FOLLOW_ME':
                    f3 +=1
                elif i['action'] == 'ADD_COMMENT_PLAYLIST' :
                    c3 +=1
            elif i['recent'] >= datetime.now() - timedelta(days=5) and i['recent'] <= datetime.now()-timedelta(days=4) :
                if i['action'] == 'ADD_SONG_TO_PLAYLIST':
                    a4 += 1
                elif i['action'] == 'LIKE_PLAYLIST' :
                    l4 +=1
                elif i['action'] == 'FOLLOW_ME':
                    f4 +=1
                elif i['action'] == 'ADD_COMMENT_PLAYLIST' :
                    c4 +=1
            elif i['recent'] >= datetime.now() - timedelta(days=6) and i['recent'] <= datetime.now()-timedelta(days=5) :
                if i['action'] == 'ADD_SONG_TO_PLAYLIST':
                    a5 += 1
                elif i['action'] == 'LIKE_PLAYLIST' :
                    l5 +=1
                elif i['action'] == 'FOLLOW_ME':
                    f5 +=1
                elif i['action'] == 'ADD_COMMENT_PLAYLIST' :
                    c5 +=1
            elif i['recent'] >= datetime.now() - timedelta(days=7) and i['recent'] <= datetime.now()-timedelta(days=6) :
                if i['action'] == 'ADD_SONG_TO_PLAYLIST':
                    a6 += 1
                elif i['action'] == 'LIKE_PLAYLIST' :
                    l6 +=1
                elif i['action'] == 'FOLLOW_ME':
                    f6 +=1
                elif i['action'] == 'ADD_COMMENT_PLAYLIST' :
                    c6 +=1
    print (a0, a1, a2, a3, a4, a5, a6)
    print (l0, l1, l2, l3, l4, l5, l6)
    print (f0, f1, f2, f3, f4, f5, f6)
    print (c0, c1, c2, c3, c4, c5, c6)

if __name__ == '__main__':
    main()