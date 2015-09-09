from datetime import datetime

from pymongo import MongoClient

env = 'production'
if env == 'localhost':
    MONGODB_URI = 'mongodb://127.0.0.1:27017/listr'
elif env == 'development':
    MONGODB_URI = 'mongodb://54.186.79.239:27017/listr'
elif env == 'production':
    MONGODB_URI = 'mongodb://mongo.swizzle.fm:27017/listr'


from datetime import datetime
from collections import Counter
import operator


def main():
    client = MongoClient(MONGODB_URI)
    db = client.listr
    playlists = db['playlists']
    results = playlists.find({}, {'country' : 1})

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

    import matplotlib.pyplot as plt
    x = []
    y = []
    plt.plot (x,y)
    plt.title('About Playlist Graph')
    plt.xlabel('The number of song in a playlist')
    plt.ylabel('The number of playlist')
    plt.savefig('1.png')


    f = open('btn_2.html', 'w')

    message = "<!DOCTYPE html>" \
                "<html>" \
                  "<head>" \
                    "<link rel='stylesheet' href='btn_2.css'>" \
                    "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>" \
                  "</head>" \
                    "<body>"\
                      "<div class = 'header'>" \
                        "<div class = 'container'>" \
                          "<h1 class='topic'>Swizzle Insight</h1>" \
                          "<p>All information from Swizzle Database, you can get here</p>" \
                        "</div>" \
                      "</div>" \
                      "<div class = 'nav'>" \
                        "<div class = 'container'>" \
                          "<ul>" \
                            "<a class = 'btn1' href ='btn_1.html'>ABOUT PLAYLIST</a>" \
                            "<a class = 'btn2' href ='btn_2.html'>ABOUT COUNTRY</a>" \
                            "<a class = 'btn3' href ='btn_3.html'>ABOUT USER`S ACTION</a>"\
                            "<a class = 'btn4' href ='btn_4.html'>ABOUT SEARCH KEYWORDS</a>"\
                          "</ul>"\
                        "</div>" \
                      "</div>" \
                    "<div class = 'content'>" \
                        "<div class = 'container1 col-sm-3'>" \
                          "<ul>" \
                            "<li>"+"1. "+first+"</li>"\
                            "<li>"+"2. "+second+"</li>" \
                            "<li>"+"3. "+third+"</li>" \
                            "<li>"+"4. "+fourth+"</li>" \
                            "<li>"+"5. "+fifth+"</li>" \
                            "<p>This is based on the number of playlist created in each country</p>" \
                          "</ul>"\
                        "</div>" \
                        "<div class = 'container2 col-sm-3'>" \
                          "<ul>" \
                            "<li>"+": "+first1+"</li>" \
                            "<li>"+": "+second1+"</li>" \
                            "<li>"+": "+third1+"</li>" \
                            "<li>"+": "+fourth1+"</li>" \
                            "<li>"+": "+fifth1+"</li>" \
                          "</ul>" \
                        "</div>" \
                        "<div class = 'container3 col-sm-6'>" \
                          "<h3>Graph</h3>"\
                        "</div>"\
                    "</div>" \
                      "<div class = 'last'>" \
                        "<div class = 'container'>" \
                          "<p class='copyright'>MADE BY SEAN KIM IN SWIZZLE</p>" \
                        "</div>" \
                      "</div>" \
                    "<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js'></script>" \
                    "<script src='1.js'></script>"\
                    "</body>" \
                "</html>" \

    f.write(message)
    f.close()

if __name__ == '__main__':
    main()


