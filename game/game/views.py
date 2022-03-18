from django.http import HttpResponse

def index(request):
    line1='<h1 style="text-align:center">my first web </h1 >'
    line2='<img src ="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.91zhuti.com%2Fuploads%2Fallimg%2F131202%2F4-131202111224.jpg&refer=http%3A%2F%2Fwww.91zhuti.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1650190212&t=a104bf514b14bd56ebded54c0d1262d0" width=1200>'
    return HttpResponse(line1+line2)
