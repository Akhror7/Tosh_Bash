from pyexpat import model
from unittest import result
from django.shortcuts import render

import pickle

model = pickle.load(open('model/RF_model.pkl', 'rb'))

def predictor(request):
    return render(request,'main.html')


def formInfo(request):
    Term =  request.GET['Term']
    ProsperScore = request.GET['ProsperScore']
    Occupation = request.GET['Occupation']
    EmploymentStatusDuration = request.GET['EmploymentStatusDuration']
    employment = request.GET['Joylashuv']

    if employment=="Бектемирский":
        Бектемирский = 1
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0

    elif employment=="Мирабадский":
        Бектемирский = 0
        Мирабадский = 1
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0
    elif employment=="Мирзо-Улугбекский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 1
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0
    elif employment=="Олмазорский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 1
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0
    elif employment=="Сергелийский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 1
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0

    elif employment=="Учтепинский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 1
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0
    elif employment=="Чиланзарский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 1
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0
    elif employment=="Шайхантахурский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 1
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0
    elif employment=="Юнусабадский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 1
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 0
    elif employment=="Яккасарайский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 1
        Янгихаётский = 0
        Яшнободский = 0

    elif employment=="Янгихаётский":
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 1
        Яшнободский = 0

    else :
        Бектемирский = 0
        Мирабадский = 0
        Мирзо_Улугбекский = 0
        Олмазорский = 0
        Сергелийский = 0
        Учтепинский = 0
        Чиланзарский = 0
        Шайхантахурский = 0
        Юнусабадский = 0
        Яккасарайский = 0
        Янгихаётский = 0
        Яшнободский = 1



    y_pred = model.predict([[Term,
    ProsperScore,
    Occupation,
    EmploymentStatusDuration,
    Бектемирский,
    Мирабадский,
    Мирзо_Улугбекский,
    Олмазорский,
    Сергелийский,
    Учтепинский,
    Чиланзарский,
    Шайхантахурский,
    Юнусабадский,
    Яккасарайский,
    Янгихаётский,
    Яшнободский
    ]])

    res = int((y_pred[0])/1000)*1000
    return render(request,'results.html',{'result':res})