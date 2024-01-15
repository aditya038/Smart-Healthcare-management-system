from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Symptoms
import pickle
import numpy as np
import random
# Create your views here.
@login_required(login_url='login')
def HomePage(request):

    if request.method =="POST":
        newname = request.POST["fname"]            
        age = request.POST['age']
        blood_group = request.POST['Blood_Group']
        itching = request.POST['itching']
        Stomach_Pain = request.POST['Stomach_Pain']
        Continuous_Sneezing = request.POST['Continuous_Sneezing']
        Diarrhoea = request.POST['Diarrhoea']
        Cough = request.POST['Cough']
        Joint_Pain = request.POST['Joint_Pain']
        Acidity = request.POST['Acidity']
        Vomiting = request.POST['Vomiting']
        Fatigue = request.POST['Fatigue']
        Weight_Loss = request.POST['Weight_Loss']
        Anxiety = request.POST['Anxiety']
        High_Fever = request.POST['High_Fever']
        Dehydration = request.POST['Dehydration']
        Indigestion = request.POST['Indigestion']
        Headache = request.POST['Headache']
        Nausea = request.POST['Nausea']
        Back_pain = request.POST['Back_pain']
        Constipation = request.POST['Constipation']
        Chest_Pain = request.POST['Chest_Pain']
        FastHeartRate = request.POST['FastHeartRate']
        Dizziness = request.POST['Dizziness']
        Cramps = request.POST['Cramps']
        Obesity = request.POST['Obesity']
        KneePain = request.POST['KneePain']
        MuscleWeakness = request.POST['MuscleWeakness']
        Coma = request.POST['Coma']
        LackofConcentration = request.POST['LackofConcentration']

        Symptoms.objects.create(name_of_patient=newname,age=age,blood_group=blood_group,itching=itching,Stomach_Pain=Stomach_Pain,Continuous_Sneezing=Continuous_Sneezing,Diarrhoea=Diarrhoea,Cough=Cough,Joint_Pain=Joint_Pain,Acidity=Acidity,Vomiting=Vomiting,Fatigue=Fatigue,Weight_Loss=Weight_Loss,Anxiety=Anxiety,High_Fever=High_Fever,Dehydration=Dehydration,Indigestion=Indigestion,Headache=Headache,Nausea=Nausea,Back_pain=Back_pain,Constipation=Constipation,Chest_Pain=Chest_Pain,FastHeartRate=FastHeartRate,Dizziness=Dizziness,Cramps=Cramps,Obesity=Obesity,KneePain=KneePain,MuscleWeakness=MuscleWeakness,Coma=Coma,LackofConcentration=LackofConcentration)


        cls = pickle.load(open('model.pkl', 'rb'))
        encoder = pickle.load(open('encoder.pkl', 'rb'))

        lis=[]
        
        limit = 105
        lis2 = [random.randint(0,1) for iter in range(limit)]

        lis.append(int(request.POST['itching']))
        lis.append(int(request.POST['Stomach_Pain']))
        lis.append(int(request.POST['Acidity']))
        lis.append(int(request.POST['Continuous_Sneezing']))
        lis.append(int(request.POST['Diarrhoea']))
        lis.append(int(request.POST['Cough']))
        lis.append(int(request.POST['Joint_Pain']))
        lis.append(int(request.POST['Vomiting']))
        lis.append(int(request.POST['Fatigue']))
        lis.append(int(request.POST['Weight_Loss']))
        lis.append(int(request.POST['Anxiety']))
        lis.append(int(request.POST['High_Fever']))
        lis.append(int(request.POST['Dehydration']))
        lis.append(int(request.POST['Indigestion']))
        lis.append(int(request.POST['Headache']))
        lis.append(int(request.POST['Nausea']))
        lis.append(int(request.POST['Back_pain']))
        lis.append(int(request.POST['Constipation']))
        lis.append(int(request.POST['Chest_Pain']))
        lis.append(int(request.POST['FastHeartRate']))
        lis.append(int(request.POST['Dizziness']))
        lis.append(int(request.POST['Cramps']))
        lis.append(int(request.POST['Obesity']))
        lis.append(int(request.POST['KneePain']))
        lis.append(int(request.POST['MuscleWeakness']))
        lis.append(int(request.POST['Coma']))
        lis.append(int(request.POST['LackofConcentration']))

        # newlis = lis
        
        lis.extend(lis2)

        lis = np.array(lis)

        lis = lis.reshape(1,-1)

        ans = cls.predict(lis)

        output = encoder.inverse_transform(ans)

        out={"output": output,
             }

        return render(request, 'result.html', out)

    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password doesnt match!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def result(request):
    return render(request, 'result.html')