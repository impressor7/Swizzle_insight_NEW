from datetime import datetime

from pymongo import MongoClient

from pymongo import MongoClient
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
    searchbarlogs = db['searchbarlogs']
    searchkeywordlogaddsongs = db['searchkeywordlogaddsongs']
    results = searchbarlogs.find({},{'keywords' : 1,'searchtime' :1})
    results1 = searchkeywordlogaddsongs.find({},{'keywords' : 1,'searchtime' :1})

    # 지난 1주동안 가장 많이 검색된 키워드!
    keyword_list = []
    all_keyword_list = []
    for item in results :
        if item['searchtime'] <= datetime.today() and item['searchtime'] >= datetime.today() - timedelta(days=1) and item['keywords'] != 'none' :
            keyword_list.append(item['keywords'])
        if item['searchtime'] <= datetime.today() and item['searchtime'] >= datetime.today() - timedelta(days=7) and item['keywords'] != 'none' :
            all_keyword_list.append(item['keywords'])
    for item1 in results1 :
        if item1['searchtime'] <= datetime.today() and item1['searchtime'] >= datetime.today() - timedelta(days=1) and item1['keywords'] != 'none' :
            keyword_list.append(item1['keywords'])
        if item1['searchtime'] <= datetime.today() and item1['searchtime'] >= datetime.today() - timedelta(days=7) and item1['keywords'] != 'none' :
            all_keyword_list.append(item1['keywords'])

    results_list = (Counter(keyword_list).most_common(5))

    final_key = []
    final_value = []
    for item3 in results_list :
        final_key.append(item3[0])
        final_value.append(item3[1])
    first = str(final_key[0])
    first1 = str(final_value[0])
    second = str(final_key[1])
    second1 = str(final_value[1])
    third = str(final_key[2])
    third1 = str(final_value[2])
    fourth = str(final_key[3])
    fourth1 = str(final_value[3])
    fifth = str(final_key[4])
    fifth1 = str(final_value[4])

    a = all_keyword_list.count(first)
    b = all_keyword_list.count(second)
    c = all_keyword_list.count(third)
    d = all_keyword_list.count(fourth)
    e = all_keyword_list.count(fifth)

    import matplotlib.pyplot as plt

    x = [0, 1, 2, 3, 4]
    y = [a,b,c,d,e]
    plt.scatter (x,y,linewidth =7, label = "Search Keyword")
    plt.title('About Search Keywords` Graph')
    plt.xlabel('KEY WORDS 0=FIRST, 1=SECOND, 2=THRID, 3=FOURTH, 4=FIFTH')
    plt.ylabel("The number for user to search with this keyword for a week")
    plt.legend(loc=1)
    plt.grid(True, color='b')
    plt.savefig('4.png')

    f = open('btn_4.html', 'w')

    message = "<!DOCTYPE html>" \
                "<html>" \
                    "<head>" \
                        "<link rel='stylesheet' href='btn_4.css'>"\
                        "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>"\
                    "</head>" \
                        "<body>" \
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
                                        "<a class = 'btn3' href ='btn_3.html'>ABOUT USER`S ACTION</a>" \
                                        "<a class = 'btn4' href ='btn_4.html'>ABOUT SEARCH KEYWORDS</a>" \
                                      "</ul>" \
                                "</div>" \
                            "</div>" \
                            "<div class = 'content'>" \
                                "<div class = 'container1 col-sm-3'>" \
                                    "<ul>" \
                                        "<li>"+"1. "+first+"</li>" \
                                        "<li>"+"2. "+second+"</li>" \
                                        "<li>"+"3. "+third+"</li>" \
                                        "<li>"+"4. "+fourth+"</li>" \
                                        "<li>"+"5. "+fifth+"</li>" \
                                        "<p>This is data only from website for now</p>" \
                                        "<p>For one day,These are five top search keyword and the number for user to search with these keywords</p>" \
                                    "</ul>" \
                                "</div>" \
                                "<div class = 'container2 col-sm-3'>" \
                                      "<ul>" \
                                        "<li>"+": "+first1+ " times"+"</li>" \
                                        "<li>"+": "+second1+ " times"+"</li>" \
                                        "<li>"+": "+third1+ " times"+"</li>" \
                                        "<li>"+": "+fourth1+" times"+"</li>" \
                                        "<li>"+": "+fifth1+" times"+"</li>" \
                                      "</ul>" \
                                "</div>" \
                                "<div class = 'container3 col-sm-6'>" \
                                "<ul>"\
                                    "<a href ='#'>Update</a>"\
                                "</ul>" \
                                  "<img src='4.png'>" \
                                "</div>" \
                            "</div>"\
                            "<div class = 'last'>"\
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
