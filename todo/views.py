# in todo/views.py
 
from django.shortcuts import render, redirect
from .models import Task,syallbuss
 
from django.contrib.auth.decorators import login_required
 
from django.db.models import Count
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})
@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['date']
        task = Task.objects.create(title=title, description=description,user=request.user)
        task.save()
       

        
                
        return redirect('task_list')
    return render(request, 'todo/task_form.html')
@login_required
def task_update(request, pk):
    task = Task.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task.title = title
        task.description = description
        completed= request.POST.get('completed',False)
       
        # completed = request.POST.get('completed')
        # print(completed)
        if completed == 'on':
            task.completed = True
        else:
            task.completed = False

        # task.completed = completed
        task.save()
        return redirect('task_list')
    return render(request, 'todo/task_form.html', {'task': task})
@login_required
def task_delete(request, pk):
    task = Task.objects.filter(user=request.user).get(pk=pk)
    task.delete()
    return redirect('task_list')

@login_required
def syal_delete(request, pk):
    syal = syallbuss.objects.filter(user=request.user).get(pk=pk)
    syal.delete()
    return redirect('/todo/syallbuss')
@login_required
def syal_add(request):
    if request.method == 'POST':
        Subject = request.POST['Subject']
        Chapter = request.POST['Chapter']
        
        task = syallbuss.objects.create(Subject=Subject, Cname=Chapter,user=request.user,completed=False)
        task.save()
        return redirect('/todo/syallbuss')
    return render(request, 'todo/syallbuss_add.html')

@login_required
def syal_update(request,pk):
    syal = syallbuss.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        Subject = request.POST['Subject']
        Chapter = request.POST['Chapter']
        completed=request.POST.get('completed',False)
        syal.Cname = Chapter
        syal.Subject = Subject
        
        if completed == 'on':
            syal.completed = True
        else:
            syal.completed = False
        syal.save()
         
        return redirect('/todo/syallbuss')
    return render(request, 'todo/syallbuss_update.html',{'syal': syal})
@login_required
def syalfun(request):
    # file="N:\\Code\\SMS\\csv\\todo_task.csv"
    # with open(file, mode='r', newline='', encoding='utf-8') as file:
    #     # Create a CSV reader object
    #     csv_reader = csv.reader(file)
        
    #     # Optionally, skip the header row if it exists
    #     header = next(csv_reader)  # Skip header row if there is one, remove this line if not

    #     # Loop through each row in the CSV file
    #     for row in csv_reader:
    #         print(f"Row: {row}")  # Debugging: print the row to verify values

    #         # Check if 'completed' should be True or False based on the value in row[3]
    #         completed = False if row[3] == '0' else True  # Assumes row[3] is a string, update if it's an int

    #         # Debugging: print out the value being assigned to 'completed'
    #         print(f"Completed: {completed}")

    #         try:
    #             # Create a new Task object and save it
    #             Task.objects.create(
    #                 title=row[1],
    #                 description=row[2],
    #                 completed=completed,
    #                 user=request.user
    #             ).save()
    #         except Exception as e:
    #             print(f"Error creating Task: {e}")

    #         # Loop through each row in the CSV file
        
            
        
    bio=syallbuss.objects.filter(Subject='Biology',user=request.user)
    chem=syallbuss.objects.filter(Subject='Chemistry',user=request.user)
    phy=syallbuss.objects.filter(Subject='Physics',user=request.user)
    eng=syallbuss.objects.filter(Subject='English',user=request.user)
    hin=syallbuss.objects.filter(Subject='Hindi',user=request.user)
    bt=syallbuss.objects.filter(Subject='Biology',user=request.user).all().count()
    ct=syallbuss.objects.filter(Subject='Chemistry',user=request.user).all().count()
    pt=syallbuss.objects.filter(Subject='Physics',user=request.user).all().count()
    et=syallbuss.objects.filter(Subject='English',user=request.user).all().count()
    ht=syallbuss.objects.filter(Subject='Hindi',user=request.user).all().count()
    btc=syallbuss.objects.filter(Subject='Biology',user=request.user,completed=True).all().count()
    ctc=syallbuss.objects.filter(Subject='Chemistry',user=request.user,completed=True).all().count()
    ptc=syallbuss.objects.filter(Subject='Physics',user=request.user,completed=True).all().count()
    etc=syallbuss.objects.filter(Subject='English',user=request.user,completed=True).all().count()
    htc=syallbuss.objects.filter(Subject='Hindi',user=request.user,completed=True).all().count()
    tc=syallbuss.objects.filter(user=request.user).all().count()
    data=syallbuss.objects.filter(user=request.user).all()
    subjects=syallbuss.objects.values('Subject').distinct()
    for subject in subjects:
        print(subject['Subject'])
    subjects_with_counts = syallbuss.objects.filter(completed=True, user=request.user).values('Subject').annotate(completed_count=Count('Subject'))
    try:

        bp=format(btc/bt*100,'.0f'),
        cp=format(ctc/ct*100 ,'.0f') ,
        pp=format(ptc/pt*100 ,'.0f') ,
    except :
        bp="error"
        cp="error"
        pp="error"
        
        
    

    return render(request,'todo/syallbuss.html',{'bio':bio,
                                                 'chem':chem,
                                                 'phy':phy,
                                                 'eng':eng,
                                                 'hin':hin,
                                                 'tc':tc,
                                                 'pt':pt,
                                                 'et':et,
                                                 'ct':ct,
                                                 'bt':bt,
                                                 'ht':ht,
                                                 'ptc':ptc,
                                                 'etc':etc,
                                                 'ctc':ctc,
                                                 'btc':btc,
                                                 'htc':htc,
                                                 'bp':bp,
                                                 'cp':cp,
                                                 'pp': pp,
                                                 'data':data,
                                                 'subjects':subjects,
                                                 'subjects_with_counts': subjects_with_counts
                                                  
                                                 })


