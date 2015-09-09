'''
The way to write something on file using python
'''



from pymongo import MongoClient

env = 'production'
if env == 'localhost':
    MONGODB_URI = 'mongodb://127.0.0.1:27017/listr'
elif env == 'development':
    MONGODB_URI = 'mongodb://54.186.79.239:27017/listr'
elif env == 'production':
    MONGODB_URI = 'mongodb://mongo.swizzle.fm:27017/listr'


from datetime import datetime

def main():

    client = MongoClient(MONGODB_URI)
    db = client.listr
    playlists = db['playlists']
    results = playlists.find({}, {'_id' : 1, '_songs' : 1})

    i0 = []
    i1 = []
    i2 = []
    i3 = []
    i4=[]
    i5 = []
    i6=[]
    i7=[]
    i8=[]
    i9=[]
    i10 = []
    i_more = []

    for i in results:
        if len(i['_songs']) == 0 :
            i0.append(i['_id'])
        elif len(i['_songs']) == 1 :
            i1.append(i['_id'])
        elif len(i['_songs']) == 2 :
            i2.append(i['_id'])
        elif len(i['_songs']) == 3 :
            i3.append(i['_id'])
        elif len(i['_songs']) == 4 :
            i4.append(i['_id'])
        elif len(i['_songs']) == 5 :
            i5.append(i['_id'])
        elif len(i['_songs']) == 6 :
            i6.append(i['_id'])
        elif len(i['_songs']) == 7 :
            i7.append(i['_id'])
        elif len(i['_songs']) == 8 :
            i8.append(i['_id'])
        elif len(i['_songs']) == 9 :
            i9.append(i['_id'])
        elif len(i['_songs']) == 10 :
            i10.append(i['_id'])
        elif len(i['_songs']) > 10 :
            i_more.append(i['_id'])


    a = str(len(i0))
    b = str(len(i1))
    c = str(len(i2))
    d = str(len(i3))
    e = str(len(i4))
    m = str(len(i5))
    g = str(len(i6))
    h = str(len(i7))
    i = str(len(i8))
    j = str(len(i9))
    k = str(len(i10))
    l = str(len(i_more))

    import matplotlib.pyplot as plt
    x = [0,1,2,3,4,5,6,7,8,9,10,11]
    y = [a,b,c,d,e,m,g,h,i,j,k,l]
    plt.plot (x,y,linewidth = 5, label = 'the number of playlist')
    plt.title('About Playlist Graph')
    plt.xlabel('The number of song in a playlist')
    plt.ylabel('The number of playlist')
    plt.legend()
    plt.grid(True, color = 'b')
    plt.savefig('1.png')


    f = open('btn_1.html', 'w')

    message = '<!DOCTYPE html>' \
          '<html>' \
            '<head>' \
                '<link rel="stylesheet" href="btn_1.css">' \
                '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">'\
            '</head>' \
                '<body>' \
                    "<div class = 'header'>" \
                        "<div class = 'container'>" \
                            "<h1 class='topic'>Swizzle Insight</h1>"\
                            "<p>All information from Swizzle Database, you can get here</p>" \
                        "</div>" \
                    "</div>" \
                    "<div class = 'nav'>" \
                        "<div class = 'container'>"\
                            "<ul>"\
                                '<a class = "btn1" href ="btn_1.html">ABOUT PLAYLIST</a>' \
                                '<a class = "btn2" href ="btn_2.html">ABOUT COUNTRY</a>' \
                                '<a class = "btn3" href ="btn_3.html">ABOUT USER`S ACTION</a>' \
                                '<a class = "btn4" href ="btn_4.html">ABOUT SEARCH KEYWORDS</a>' \
                            "</ul>"\
                        "</div>" \
                   "</div>" \
                    "<div class = 'content'>" \
                        "<div class = 'container1 col-xs-6 col-sm-3'>" \
                            "<ul>" \
                                "<li>Playlist 0</li>" \
                                "<li>Playlist 1</li>" \
                                "<li>Playlist 2</li>" \
                                "<li>Playlist 3</li>" \
                                "<li>Playlist 4</li>" \
                                "<li>Playlist 5</li>" \
                                "<li>Playlist 6</li>"\
                                "<li>Playlist 7</li>" \
                                "<li>Playlist 8</li>"\
                                "<li>Playlist 9</li>" \
                                "<li>Playlist 10</li>" \
                                "<li>Playlist_more</li>" \
                            "</ul>" \
                        "</div>" \
                        "<div class = 'container2 col-xs-6 col-sm-3'>" \
                            "<ul>" \
                                "<li>" +":  " + a + "</li>" \
                                "<li>" +":  "+ b + "</li>" \
                                "<li>" +":  "+ c + "</li>" \
                                "<li>" +":  "+ d + "</li>" \
                                "<li>" +":  "+ e + "</li>" \
                                "<li>" +":  "+ m + "</li>" \
                                "<li>" +":  "+ g + "</li>" \
                                "<li>" +":  "+ h + "</li>" \
                                "<li>" +":  "+ i + "</li>" \
                                "<li>" +":  "+ j + "</li>" \
                                "<li>" +":  "+ k + "</li>" \
                                "<li>" +":  "+ l + "</li>" \
                            "</ul>" \
                        "</div>" \
                        "<div class = 'container3 col-sm-6'>" \
                            "<img src='1.png'>" \
                        "</div>" \
                    "</div>" \
                    "<div class = 'last'>" \
                        "<div class = 'container'>" \
                            "<p class='copyright'>MADE BY SEAN KIM IN SWIZZLE</p>" \
                        "</div>" \
                    "</div>" \
                    "<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js'></script>" \
                    "<script src='1.js'></script>" \
                "</body>" \
            "</html>" \


    f.write(message)
    f.close()

if __name__ == '__main__':
    main()


