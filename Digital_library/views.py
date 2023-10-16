
from django.shortcuts import render, redirect
from django.contrib import messages
import pickle
import numpy as np
from .models import Books,user

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

email="hi"
item="hi"

def Landing_page(request):
    return render(request,'Landing_page.html')
def home(request):
    return render(request,'home.html')
def maps(request):
    return render(request,'maps.html')
def home2(request):
    return render(request,'home2.html')
def contacts(request):
    return render(request,'contacts.html')
def about_us(request):
    return render(request,'about_us.html')

def recommend2(request):
    book1=""
    if item == "Dan_Brown" :
        book1 = Books.objects.all()[0:4]
    if item == "Charles_Dickens" :
        book1 = Books.objects.all()[4:8]
    if item == "George_Orwell" :
        book1 = Books.objects.all()[8:12]
    if item == "Walter_Scott" :
        book1 = Books.objects.all()[12:16]

    data = {
        'book': book1
    }
    return render(request,'recommend2.html',data)
def login(request):
    global email
    data1 = user.objects.all()
    l1=list()
    l2=list()
    for a in data1:
        email1=a.Email
        password=a.Password
        l1.append(email1)
        l2.append(password)
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']

        if((email in l1) and (pass1 in l2)) :

            return render(request, "home2.html")
        else:
            messages.error(request, "invalid Email address or password")
            return render(request,'login.html')
    return render(request,"login.html")
def novels(request):
    global email,item
    book1 = Books.objects.all()
    data={
        'book':book1
    }
    if request.method == 'POST':
        item = request.POST.get('save')
        user.objects.filter(Email=email).update(Author_name=item)
    return render(request,'novels.html',data)
def registration(request):
    data1 = user.objects.all()
    l1 = list()
    for a in data1:
        email1 = a.Email
        l1.append(email1)
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if (email in l1):
            messages.success(request, "email already register")
            return render(request, 'registration.html')
        else:
            c_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            l_alpha = "abcdefghijklmnopqrstuvwxyz"
            digits = "0123456789"
            special = "#@$_"
            c, l, d, s = 0, 0, 0, 0
            if (len(pass1) + 1 > 8):
                for i in pass1:
                    if (i in c_alpha):
                        c += 1
                    if (i in l_alpha):
                        l += 1
                    if (i in digits):
                        d += 1
                    if (i in special):
                        s += 1
            else:
                messages.success(request, "password must be atleast of 8 characters")
                return render(request, 'registration.html')
            if (c >= 1 and l >= 1 and d >= 1 and s >= 1):
                if pass1 != pass2:
                    messages.success(request, "password and confirm password does not match")
                    return render(request, 'registration.html')


                else:
                    user1 = user(Name=fname, Email=email, Password=pass1)
                    user1.save()
                    messages.success(request,"Your Account has been created succesfully!")
            else:
                if (c == 0 ):
                    messages.success(request, "Password should contain atleast one Uppercase Character")
                elif l == 0:
                    messages.success(request, "Password should contain atleast one Lowercase Character")
                elif d == 0:
                    messages.success(request, "Password should contain  digits")
                elif s == 0:
                    messages.success(request, "Password should contain special character")
            return redirect('/registration')
    return render(request,'registration.html')
def recommend(request):

    if request.method == "POST":
        user_input = request.POST['user_input']
        index = np.where(pt.index == user_input)[0]
        index = index[0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
        data1 = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data1.append(item)
        sam1 = []
        for i in range (0,4):
            vaish =data1[i][0]
            sam1.append(vaish)
        data={
            'image': sam1
        }
        return render(request, 'recommend.html',data)
    else:
        user_input ="#"
        data="#"
    return render(request,'recommend.html')

def index(request):
    data={
        'image' : list(popular_df['Image-URL-M'].values),
    }
    return render(request,'index.html', data)