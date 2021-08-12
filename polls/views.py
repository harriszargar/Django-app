from urllib import request

from django.shortcuts import render, HttpResponse, redirect
import mysql.connector
from datetime import datetime


# Create your views here.
def index(request):
    template_name = "index.html"
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Mhz-9797199103",
        database="readingright"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, itemname, CASE itemstatus WHEN 0 THEN 'Pending' when 1 then 'Bought' end as itemstatus, itemquantity, date from grocerylist ; ")
    data = cursor.fetchall()
    #print(data)
    cursor.execute("SELECT itemname, CASE itemstatus WHEN 0 THEN 'Unavaialble' when 1 then 'available' end as itemstatus, itemquantity from grocerylist where id=1;")
    data1 = cursor.fetchall()
    cursor.execute("SELECT itemname, CASE itemstatus WHEN 0 THEN 'Unavaialble' when 1 then 'available' end as itemstatus, itemquantity from grocerylist where id=2;")
    data2 = cursor.fetchall()
    cursor.execute(
        "SELECT itemname, CASE itemstatus WHEN 0 THEN 'Unavaialble' when 1 then 'available' end as itemstatus, itemquantity from grocerylist where id=3;")
    data3 = cursor.fetchall()

    if (request.POST.get('count')):
        mydates = request.POST.get("mydate")
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Mhz-9797199103",
            database="readingright"
        )
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, itemname, CASE itemstatus WHEN 0 THEN 'Pending' when 1 then 'Bought' end as itemstatus, itemquantity, date from grocerylist where date='{}' ;".format(
             str(mydates)))
        data = cursor.fetchall()

    return render(request, template_name, {'data': data, 'data1':data1, 'data2':data2, 'data3':data3})

def add(request):
    template_name = "add.html"
    if (request.GET.get('additem')):
        id = request.GET.get("serialnumber")
        itemName = request.GET.get('itemname')
        print(itemName)
        itemquantity = request.GET.get('itemquantity')
        itemstatus = request.GET.get('itemstatus')
        if itemstatus == 'Bought':
            itemstatus = 1
        else:
            itemstatus = 0

        itemdate = request.GET.get("date")
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Mhz-9797199103",
            database="readingright"
        )
        cursor = conn.cursor()
        cursor.execute(
            "insert into readingright.grocerylist(id, itemname, itemquantity, itemstatus, date) values(%s,%s,%s,%s,%s)",
            (id, itemName, itemquantity, itemstatus, itemdate))
        conn.commit()
        conn.close()
        return redirect("/homepage")
    return render(request, template_name, {'add': add, "template_name":template_name})
def homepage(request):
    template_name = "index.html"
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Mhz-9797199103",
        database="readingright"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, itemname, CASE itemstatus WHEN 0 THEN 'Pending' when 1 then 'Bought' end as itemstatus, itemquantity, date from grocerylist ; ")
    data = cursor.fetchall()
    #print(data)
    cursor.execute("SELECT itemname, CASE itemstatus WHEN 0 THEN 'Unavaialble' when 1 then 'available' end as itemstatus, itemquantity from grocerylist where id=1;")
    data1 = cursor.fetchall()
    cursor.execute("SELECT itemname, CASE itemstatus WHEN 0 THEN 'Unavaialble' when 1 then 'available' end as itemstatus, itemquantity from grocerylist where id=2;")
    data2 = cursor.fetchall()
    cursor.execute(
        "SELECT itemname, CASE itemstatus WHEN 0 THEN 'Unavaialble' when 1 then 'available' end as itemstatus, itemquantity from grocerylist where id=3;")
    data3 = cursor.fetchall()

    return render(request, template_name, {'data': data, 'data1':data1, 'data2':data2, 'data3':data3})

def update(request):
    template_name="update.html"
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Mhz-9797199103",
        database="tm_bot_auotmation"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT concat(id) as id_list from readingright.grocerylist;")
    listd = cursor.fetchall()






    if (request.GET.get('updateitem')):
        itemName = request.GET.get('itemname')
        itemId = request.GET.get('serialnumber')
        itemquantity = request.GET.get('itemquantity')
        itemstatus = request.GET.get('itemstatus')
        print(itemstatus)
        if itemstatus == 'Bought':
            itemstatus = 1
        else:
            itemstatus = 0
        itemdate = request.GET.get("date")
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Mhz-9797199103",
            database="readingright"
        )
        cursor = conn.cursor()
        cursor.execute(
            "Update readingright.grocerylist set itemname=%s, itemquantity=%s, itemstatus=%s, date=%s where Id=%s;",
            (itemName, itemquantity, itemstatus, itemdate, itemId))
        conn.commit()
        conn.close()
        return redirect("/homepage")
    return render(request, template_name, {"listd":listd, "update": update})

def deleteitem(request):
    template_name = "deleteitem.html"
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Mhz-9797199103",
        database="tm_bot_auotmation"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT concat(id) as id_list from readingright.grocerylist;")
    listf = cursor.fetchall()
    if (request.GET.get('deleteitem')):
        itemId = request.GET["serialnumber"]
        print(itemId)
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Mhz-9797199103",
            database="tm_bot_auotmation"
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM readingright.grocerylist where id='{}';".format(itemId))
        conn.commit()
        conn.close()

        return redirect("/homepage")

    return render(request, template_name, {"listf": listf})




