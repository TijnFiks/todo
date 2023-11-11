from django.shortcuts import render

# Create your views here.

from .models import ToDoList, ToDoItem


from django.shortcuts import redirect, render
from django.http import HttpResponse

def index(request):
    lists = ToDoList.objects.all()
    return render(
        request,
        'index.html',
        {
            'lists': lists,
        }
    )

def list(request):
    list_id = request.GET['id']
    list = ToDoList.objects.get(id=list_id)
    items = ToDoItem.objects.filter(todo_list_id=list_id).order_by('completed')
    return render(
        request,
        'list.html',
        {
            'items': items,
            'list': list
        }
    )

def new_item(request):
    title = request.POST['item_title']
    due_date = request.POST['due_date']
    todo_list_id = int(request.POST['list_id'])
    item = ToDoItem(title=title, due_date=due_date, todo_list_id=todo_list_id)
    item.save()
    return redirect(f'/list?id={todo_list_id}')

def item(request):
    id = request.GET['id']
    employee = Employee.objects.get(id=id)
    departments = Department.objects.all()
    return render(
        request,
        'employee.html',
        {
            'employee': employee,
            'departments': departments
        }
    )

def delete_item(request):
    id = int(request.POST['id'])
    item = ToDoItem.objects.get(id=id)
    item.delete()
    return redirect(f'/list?id={item.todo_list_id}')


def new_list(request):
    title = request.POST['list_title']
    list = ToDoList(title=title)
    list.save()
    return redirect(index)

def delete_list(request):
    id = int(request.POST['id'])
    ToDoList.objects.get(id=id).delete()
    return redirect(index)


