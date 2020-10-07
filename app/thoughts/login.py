from django.shortcuts import render, redirect
from .models import UserModel, SessionModel
import logging


def login(request):
    context = {}
    if request.method == 'POST':
        # Get the data and try to log
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        logging.debug('trying Usermodel query')
        try:
            logging.debug('RETRIEVE SESSION MODEL')
            user = UserModel.objects.get(username=username)
            logging.debug('USER MODE PASSED -- 100CHARS')
            logging.debug('Printing user {}'.format(user))
            session = user.login_user(password)
            logging.debug('USER MODE PASSED -- 50CHARS')

            # Set session
            response = redirect('index')
            response.set_cookie('session', session)
            logging.debug('RESPONSE PASSED')
            return response

        except (UserModel.DoesNotExist, UserModel.IncorrectPassword):
            logging.debug('Exception Happened USER MODEL')
            context = {
                'no_log': True,
            }
            return render(request, 'search.html', context)

    return render(request, 'login.html', context)


def logout(request):
    # Delete the session
    cookie_session = request.COOKIES.get('session')
    if cookie_session:
        # Delete it from the DB
        try:
            session = SessionModel.objects.get(session=cookie_session)
            session.delete()
        except SessionModel.DoesNotExist:
            pass

    # Delete session cookie
    response = redirect('login')
    response.delete_cookie('session')
    return response
