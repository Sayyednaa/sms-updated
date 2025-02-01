from django.shortcuts import render
from .models import Test
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
def home(request):
    try:
        all_data = Test.objects.filter(user=request.user).all()
        botany_marks = Test.objects.filter(user=request.user).values_list('date', 'Botany')
        Zoology_marks = Test.objects.filter(user=request.user).values_list('date', 'Zoology')
        Inorganic_marks = Test.objects.filter(user=request.user).values_list('date', 'Inorganic')
        Organic_marks = Test.objects.filter(user=request.user).values_list('date', 'Organic')
        Physical_marks = Test.objects.filter(user=request.user).values_list('date', 'Physical')
        Physics_marks = Test.objects.filter(user=request.user).values_list('date', 'Physics')
        dates = Test.objects.filter(user=request.user).values_list('date', flat=True).distinct()

        total_marks_by_date = []
        # Fetching data for each date
        for date in dates:
            data = Test.objects.filter(date=date,user=request.user).first()
            total_marks = sum([data.Botany, data.Zoology, data.Physical, data.Inorganic, data.Organic, data.Physics])
            total_marks_by_date.append({'date': date, 'total_marks': total_marks})
        

        return render(request, 'test/index.html', {'all_data': all_data,'total_marks_by_date': total_marks_by_date,'botany_marks': botany_marks,'zoology_marks':Zoology_marks,'inorganic_marks':Inorganic_marks,'organic_marks':Organic_marks,'physical_marks':Physical_marks,'physics_marks':Physics_marks})
    except Exception as e:
        
        return render(request, 'test/index.html', {'error': 'No data found'})



@login_required
def add(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        Botany = request.POST.get('botany')
        Zoology = request.POST.get('zoology')
        Inorganic = request.POST.get('inorganic')
        Organic = request.POST.get('organic')
        Physical = request.POST.get('physical')
        Physics = request.POST.get('physics')
        Test.objects.create(date=date, Botany=Botany, Zoology=Zoology, Inorganic=Inorganic, Organic=Organic, Physical=Physical, Physics=Physics, user=request.user)
        return redirect('/test/')
    return render(request, 'test/add.html')

@login_required
def update(request, pk):
    data = Test.objects.get(id=pk)
    if request.method == 'POST':
        data.date = request.POST.get('date')
        data.Botany = request.POST.get('botany')
        data.Zoology = request.POST.get('zoology')
        data.Inorganic = request.POST.get('inorganic')
        data.Organic = request.POST.get('organic')
        data.Physical = request.POST.get('physical')
        data.Physics = request.POST.get('physics')
        data.save()

        return redirect('/test/')
    date=data.date = data.date.strftime('%Y-%m-%d')
    return render(request, 'test/update.html', {'data': data,'date':date})
@login_required
def delete(request, pk):
    data = Test.objects.get(id=pk)
    data.delete()
    return redirect('/test/')