# views.py
from django.shortcuts import render
from django.db.models import Sum,Avg
from django.db.models import Sum
from django.db.models.functions import TruncMonth,TruncDay,ExtractWeek,ExtractYear
from .models import TimeEntry
from datetime import datetime,timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
@login_required
def monthly_summary(request):
    # Fetch monthly summaries
    monthly_summaries = TimeEntry.objects.filter(user=request.user).annotate(
        month=TruncMonth('date')
    ).values('month').annotate(
        total_duration=Sum('duration'),
        avg_duration=Avg('duration')
    ).order_by('month')
   
    return monthly_summaries
@login_required
def home(request):
    try:
        time_entries = TimeEntry.objects.filter(user=request.user).all()
        result = TimeEntry.objects.filter(user=request.user).aggregate(Sum('duration'), Avg('duration'))
        tDays=time_entries.count()
        zeroDay=TimeEntry.objects.filter(duration=0,user=request.user).count()

        # Access the sum and average values
        duration = result['duration__sum']
        average = result['duration__avg']
        # ***Total Monthly avg****
        months=monthly_summary(request)
        # *****Day with Highest Duration*********
        day_with_highest_duration = TimeEntry.objects.filter(user=request.user).annotate(
        day=TruncDay('date')
        ).values('day').annotate(
            total_duration=Sum('duration')
        ).order_by('-total_duration').first()

        if day_with_highest_duration:
            highest_duration_day = day_with_highest_duration['day']
            total_duration = day_with_highest_duration['total_duration']
            HighestDay=f'{highest_duration_day} : {total_duration}'
        # ******Week With Highest Duration ********
            

        

            # Find the week with the highest total duration
            # Fetch the week with the highest total duration
            week_with_highest_duration = TimeEntry.objects.filter(user=request.user).annotate(
                week=ExtractWeek('date'),
                year=ExtractYear('date')
            ).values('year', 'week').annotate(
                total_duration=Sum('duration')
            ).order_by('-total_duration').first()

            if week_with_highest_duration:
                year = week_with_highest_duration['year']
                week_number = week_with_highest_duration['week']

                # Find the start and end dates of the week
                start_of_week = datetime.strptime(f"{year}-W{week_number}-1", "%G-W%V-%u").date()
                end_of_week = start_of_week + timedelta(days=6)
                total_duration_of_highest_week = TimeEntry.objects.filter(user=request.user,
                    date__range=[start_of_week, end_of_week]
                ).aggregate(total_duration=Sum('duration'))['total_duration']

                week=(f" {start_of_week} to {end_of_week} : {total_duration_of_highest_week}")
    
        return render(
            request,
            'daily/index.html',
            {
                'time_entries': time_entries,
                'hours': duration,
                'avg':average,
                'zero':zeroDay,
                'tday':tDays,
                'month':months,
                'highday':HighestDay,
                'week':week,

        })
    except:
        return render(
            request,
            'daily/index.html',{'error':'No data available'}
        
              
        )


@login_required
def add(request):
    if request.method == 'POST':
        date = request.POST['date']
        duration = request.POST['duration']
        data = TimeEntry(date=date, duration=duration,user=request.user)
        data.save()
        return redirect('/time/')
    return render(request, 'daily/add.html')

@login_required
def update(request,pk):
    data=TimeEntry.objects.get(id=pk)
    if request.method == 'POST':
        date = request.POST['date']
        duration = request.POST['duration']
        data = TimeEntry(date=date, duration=duration,user=request.user)
        data.save()
        return redirect('/time/')
    date=data.date=data.date.strftime('%Y-%m-%d')
    return render(request, 'daily/update.html',{'data':data,'date':date})
 # with open('A:\Code\SMS\SMS-main\daily\data.text') as file:
    #     for lines in file:
    #         values = lines.strip().split(',')
    #         date=values[0]
    #         duration=values[1]
    #         data=TimeEntry(date=date,duration=duration)
    #         data.save()
@login_required
def delete(request,pk):
    data=TimeEntry.objects.get(id=pk)
    data.delete()
    return redirect('/time/')
 # with open('A:\Code\SMS\SMS-main\daily\data.text') as file:
    #     for lines in file:
    #         values = lines.strip().split(',')
    #         date=values[0]
    #         duration=values[1]
    #         data=TimeEntry(date=date,duration=duration)
    #         data.save()
