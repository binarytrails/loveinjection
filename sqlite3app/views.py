from django.shortcuts import HttpResponse, render_to_response, render
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token
from django.db import connection

log = """<i>Username:</i> %s</br>
    <i>Password:</i> %s</br>
    <i>Authentificated:</i> %s</br>
    <i>Rows matched:</i></br>%s</br>
    <i>SQL:</i></br>%s
"""

@csrf_exempt
def level1(request):
    if request.method == "GET":
        return render(request, 'sqlite3app/login.html')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        cursor = connection.cursor()
        sql = """SELECT username, password FROM sqlite3app_user 
            WHERE username='""" + username + "' AND password='" + password + "';"
        
        try:
            query = cursor.execute(sql)
        except Exception, error:
            return render(request, 'sqlite3app/login.html', {"log": error})

        creds = {}
        auth = False 
        for user, pwd in query:
            creds[user] = pwd
            if user: auth = True

        return render(request, 'sqlite3app/login.html', {"log": log %(username, password, str(auth), str(creds), sql)})

