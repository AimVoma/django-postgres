from django.shortcuts import render, redirect
from .models import ThoughtModel, SessionModel
import os
from django.conf import settings
# import dill as pickle, joblib
from django.db import transaction

def get_username_from_session(request):
    cookie_session = request.COOKIES.get('session')
    try:
        session = SessionModel.objects.get(session=cookie_session)
    except SessionModel.DoesNotExist:
        return None

    return session.username


def list_thoughts(request):
    '''
    List the user's thoughts
    '''
    username = get_username_from_session(request)
    if not username:
        return redirect('login')

    user_thoughts = (ThoughtModel.objects
                     .filter(username=username)
                     .order_by('-timestamp'))

    context = {
        'thoughts': user_thoughts,
        'username': username,
    }
    return render(request, 'list_thoughts.html', context)


def new_thought(request):
    '''
    Create a new thought for the user
    '''
    username = get_username_from_session(request)
    if not username:
        return redirect('login')

    text = request.POST.get('text')

    if text:
        # Only store the thought if there's text in it
        new_thought = ThoughtModel(text=text, username=username)
        new_thought.save()

    return redirect('list-thoughts')

# def analyze_thought(request):
#     '''
#     Create a new thought for the user
#     '''
#
#     print('---- Printing Req')
#     print(request)
#
#     username = get_username_from_session(request)
#     if not username:
#         return redirect('login')
#
#     thought_ids = request.POST.getlist('checks')
#
#     for thought_id in thought_ids:
#         thought_model = ThoughtModel.objects.get(pk=thought_id)
#         sentiment = settings.SENTIMENT_MODEL.predict([thought_model.text])[0]
#         thought_model.sentiment = sentiment
#         thought_model.save()
#
#     context = {
#         'thoughts': ThoughtModel.objects.filter(pk__in=thought_ids),
#         'username': username
#     }
#
#     # q_set = ThoughtModel.objects.all().values()
#     # print(type(q_set))
#     # print(q_set)
#
#     return render(request, 'list_sentiment_thoughts.html', context)
#     # return redirect('list-thoughts')

