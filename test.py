__author__ = 'ideabove01'


from pymongo import MongoClient

env = 'production'
if env == 'localhost':
    MONGODB_URI = 'mongodb://127.0.0.1:27017/listr'
elif env == 'development':
    MONGODB_URI = 'mongodb://54.186.79.239:27017/listr'
elif env == 'production':
    MONGODB_URI = 'mongodb://mongo.swizzle.fm:27017/listr'


from datetime import datetime, timedelta
from collections import Counter

def main():
    client = MongoClient(MONGODB_URI)
    db = client.listr
    playlists = db['playlists']
    results = playlists.find({}, {'country' : 1})
    results2 = playlists.find({},{'country':1,'published':1})

    a = []
    for i in results :
        if i['country'] not in a :
            a.append(i['country'])
    b = {}
    for n in range(len(a)) :
        results1 = playlists.find({'country' : a[n]}, {'country' : 1}).count()
        b.update({a[n] : results1})

    results_list = Counter(b).most_common(5)


    final_key = []
    final_value = []
    for item in results_list :
        final_key.append(item[0])
        final_value.append(item[1])

    first = str(final_key[0])
    first1 =str(final_value[0])
    second = str(final_key[1])
    second1 =str(final_value[1])
    third = str(final_key[2])
    third1 =str(final_value[2])
    fourth = str(final_key[3])
    fourth1 =str(final_value[3])
    fifth = str(final_key[4])
    fifth1 =str(final_value[4])

    print (first,second,third,fourth,fifth)
    print (first1,second1,third1,fourth1,fifth1)

    a0 = 0
    a1 = 0
    a2 = 0
    a3=0
    a4=0
    a5=0
    a6=0
    b0 = 0
    b1 = 0
    b2 = 0
    b3=0
    b4=0
    b5=0
    b6=0
    c0 = 0
    c1 = 0
    c2 = 0
    c3=0
    c4=0
    c5=0
    c6=0
    d0 = 0
    d1 = 0
    d2 = 0
    d3=0
    d4=0
    d5=0
    d6=0
    e0 = 0
    e1 = 0
    e2 = 0
    e3=0
    e4=0
    e5=0
    e6=0
    for item in results2 :
        if item['published'] >= datetime.today() - timedelta(days=7) and item['published']<=datetime.today()-timedelta(days=6):
            if item['country'] ==first :
                a0 +=1
            elif item['country'] == second :
                b0 +=1
            elif item['country'] == third :
                c0 +=1
            elif item['country'] == fourth :
                d0 +=1
            elif item['country'] == fifth :
                e0 +=1
        elif item['published'] >= datetime.today() - timedelta(days=6) and item['published']<=datetime.today()-timedelta(days=5):
            if item['country'] ==first :
                a1 +=1
            elif item['country'] == second :
                b1 +=1
            elif item['country'] == third :
                c1 +=1
            elif item['country'] == fourth :
                d1 +=1
            elif item['country'] == fifth :
                e1 +=1
        elif item['published'] >= datetime.today() - timedelta(days=5) and item['published']<=datetime.today()-timedelta(days=4):
            if item['country'] ==first :
                a2 +=1
            elif item['country'] == second :
                b2 +=1
            elif item['country'] == third :
                c2 +=1
            elif item['country'] == fourth :
                d2 +=1
            elif item['country'] == fifth :
                e2 +=1
        elif item['published'] >= datetime.today() - timedelta(days=4) and item['published']<=datetime.today()-timedelta(days=3):
            if item['country'] ==first :
                a3 +=1
            elif item['country'] == second :
                b3 +=1
            elif item['country'] == third :
                c3 +=1
            elif item['country'] == fourth :
                d3 +=1
            elif item['country'] == fifth :
                e3 +=1
        elif item['published'] >= datetime.today() - timedelta(days=3) and item['published']<=datetime.today()-timedelta(days=2):
            if item['country'] ==first :
                a4 +=1
            elif item['country'] == second :
                b4 +=1
            elif item['country'] == third :
                c4 +=1
            elif item['country'] == fourth :
                d4 +=1
            elif item['country'] == fifth :
                e4 +=1
        elif item['published'] >= datetime.today() - timedelta(days=2) and item['published']<=datetime.today()-timedelta(days=1):
            if item['country'] ==first :
                a5 +=1
            elif item['country'] == second :
                b5 +=1
            elif item['country'] == third :
                c5 +=1
            elif item['country'] == fourth :
                d5 +=1
            elif item['country'] == fifth :
                e5 +=1
        elif item['published'] >= datetime.today() - timedelta(days=1) and item['published']<=datetime.today():
            if item['country'] ==first :
                a6 +=1
            elif item['country'] == second :
                b6 +=1
            elif item['country'] == third :
                c6 +=1
            elif item['country'] == fourth :
                d6 +=1
            elif item['country'] == fifth :
                e6 +=1

    print (a0,a1,a2,a3,a4,a5,a6)
    print (b0,b1,b2,b3,b4,b5,b6)
    print (c0,c1,c2,c3,c4,c5,c6)
    print (d0,d1,d2,d3,d4,d5,d6)
    print (e0,e1,e2,e3,e4,e5,e6)


    # import matplotlib.pyplot as plt
    #
    #
    # x = [0,1,2,3,4,5,6]
    # y = [a0,a1,a2,a3,a4,a5,a6]
    # x1 = [0,1,2,3,4,5,6]
    # y1 = [b0,b1,b2,b3,b4,b5,b6]
    # x2 = [0,1,2,3,4,5,6]
    # y2 = [c0,c1,c2,c3,c4,c5,c6]
    # x3 = [0,1,2,3,4,5,6]
    # y3 = [d0,d1,d2,d3,d4,d5,d6]
    # x4 = [0,1,2,3,4,5,6]
    # y4 = [e0,e1,e2,e3,e4,e5,e6]
    # plt.grid(True,'b')
    # plt.plot (x,y, linewidth=5,label =first)
    # plt.plot(x1,y1, linewidth=5,label =second)
    # plt.plot(x2,y2, linewidth=5,label =third)
    # plt.plot(x3,y3, linewidth=5,label = fourth)
    # plt.plot(x4,y4, linewidth=5,label = fifth)
    # plt.legend(loc=1)
    # plt.title('About Country Graph')
    # plt.xlabel('The number of song in a playlist')
    # plt.ylabel('The number of playlist')
    # plt.savefig('test.png')

if __name__ == '__main__':
    main()
