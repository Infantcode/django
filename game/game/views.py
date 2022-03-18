from django.http import HttpResponse

def index(request):
    line1='<h1 style="text-align:center">my first web </h1 >'
    line3='<a href= "/play/">to next page </a>'
    line4='<hr>'
    line2='<img src ="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.91zhuti.com%2Fuploads%2Fallimg%2F131202%2F4-131202111224.jpg&refer=http%3A%2F%2Fwww.91zhuti.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1650190212&t=a104bf514b14bd56ebded54c0d1262d0" width=1200>'
    return HttpResponse(line1+line3+line4+line2)

def play(request):
    line1='<h1 style="text-align:center">the next page </h1 >'
    line3 ='<a href = "/">return first page</a>'
    line4='<hr>'
    line2='<img src ="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201508%2F12%2F20150812212139_iFKSv.jpeg&refer=http%3A%2F%2Fb-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1650191547&t=5dcd4ad8d5741517bc96f4bf019ec21e" width=1200>'
    return HttpResponse(line1+line3+line4+line2)
