from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')
def movie_news_view(request):
    news1='Kalank is going to release soon'
    news2='Lukka Chuppi is a Blockbuster'
    news3='Ranbir and Alia going to marry soon'
    news4='Salman enjoying his Holidays in UK'
    news5='Katrina not getting any movies'
    my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'testapp/mnews.html',my_dict)
def sports_news_view(request):
    news6='Virat Kohli scored his 41st Ton'
    news7='India fell to a 2-3 ODI series loss to Australia despite having a 2-0 lead'
    news8='Roger Federer, Rafael Nadal Steam Into Indian Wells Quarter-Finals'
    news9='All England Open 2019: Saina Nehwal, Kidambi Srikanth Enter Quarters'
    news10='Jennifer Lopez Engaged To This Baseball Great'
    my_dict1={'news6':news6,'news7':news7,'news8':news8,'news9':news9,'news10':news10}
    return render(request,'testapp/snews.html',my_dict1)
def politics_news_view(request):
    news11='Congress seeks Piyush Goyal resignation over Mumbai bridge collapse'
    news12='Jaish chief stayed in Ashok & Janpath hotels in Delhi in 1994'
    news13='Imran Khan says Pakistan will have better ties with India after polls'
    news14='Rahul Gandhi standing behind Robert Vadra in land scam, says RS Prasad'
    news15='West Bengal: TMC sitting MLA Arjun Singh joins BJP'
    my_dict2={'news11':news11,'news12':news12,'news13':news13,'news14':news14,'news15':news15}
    return render(request,'testapp/pnews.html',my_dict2)
