from django.shortcuts import render
import random
# Create your views here.
def lotto(request):
    lotto_list=[]
    while len(lotto_list)<6:
        new_number=random.randint(1,45)
        if new_number in lotto_list:
            continue
        else:
            lotto_list.append(new_number)
            
    return render(request,'lotto.html',{'result':lotto_list})