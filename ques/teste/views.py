from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
import json   

# Create your views here.

def create_ques(request):
    return render(request,'questions.html')
@csrf_exempt
def checking(request):
    print("sriiiiiiiii")
    right=0
    wrong=0
    if request.method =='POST':
        ans1=request.POST.get('val')
        ans2=request.POST.get('val2')
        ans3=request.POST.get('val3')
        print(ans1,ans2,ans3)

        if ans1 == 'maison':
            right=right+1
        else:
            wrong=wrong+1
        if ans2 == 'valise':
            right=right+1
        else:
            wrong=wrong+1
        if ans3 == 'soleil':
            right=right+1
        else:
            wrong=wrong+1
        print('right:',right)
        print('wrong:',wrong)
        html=render_to_string('answer.html',{'answer':'success','ans1':'maison','ans2':'valise','ans3':'soleil','right':right,'wrong':wrong,'sel1':ans1,'sel2':ans2,'sel3':ans3})
        data ={'html':html}
    return HttpResponse(json.dumps(data))


    