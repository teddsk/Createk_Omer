from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from listings.forms import SingForm, LogForm, Chifoumi
from listings.models import Sign
import random
# Create your views here.

def sign(request):
    if request.method == 'POST':
        form_sing = SingForm(request.POST)
        if form_sing.is_valid():
            password = form_sing.cleaned_data['password']
            confirmation = form_sing.cleaned_data['confirmation']
            if password != confirmation:
                error_message = "Les mots de passe ne correspondent pas."
            else:
                form_sing.save()
                return redirect('login')
    else:
        form_sing = SingForm()
    context = {'form': form_sing, 'error_message': error_message if 'error_message' in locals() else ''}
    return render(request, 'listings/sign.html', context)

def login(request):
    error_message = ""
    if request.method == 'POST':
        form_log = LogForm(request.POST)
        if form_log.is_valid():
            email = form_log.cleaned_data['email']
            password = form_log.cleaned_data['password']
            for object in Sign.objects.all():
                if object.email == email and object.password == password:
                    prenom = object.prenom
                    choix = "choix"
                    return redirect('game', prenom=prenom, choix=choix)
                else:
                    error_message = "L'email ou le mot de passe est incorrecte."
            request.session['my_score'] = 0
            request.session['cp_score'] = 0
            request.session.modified = True
    else:
        form_log = LogForm()
    context = {'form': form_log, 'error_message': error_message if 'error_message' in locals() else ''}
    return render(request, 'listings/login.html', context)


def choose(request, choix):
     prenom = request.GET.get('prenom', '')
     return redirect('game', prenom=prenom, choix=choix)

def game(request, prenom, choix):
    lists = ['pierre', 'feuille', 'ciseau']
    cp_choice = "rien"; my_choice = "rien"; res = ""
    nb_game = request.session.get('nb_game', 0)
    my_score = request.session.get('my_score', 0)
    cp_score = request.session.get('cp_score', 0)
    null_score = request.session.get('null_score', 0)

    list_my_score = request.session.get('list_my_score', [])
    if not isinstance(list_my_score, list):
        list_my_score = []

    list_cp_score = request.session.get('list_cp_score', [])
    if not isinstance(list_cp_score, list):
        list_cp_score = []
    
    list_nb_game = request.session.get('list_nb_game', [])
    if not isinstance(list_cp_score, list):
        list_nb_game = []
    
    my_choice = choix
    if choix != 'choix':
        cp_choice = random.choice(lists)
        if my_choice == "pierre" and cp_choice == "ciseau":
            my_score += 1; nb_game += 1; list_nb_game.append(nb_game)
            res = "Vous avez gagné"
            list_cp_score.append(0); list_my_score.append(1)
        elif my_choice == "ciseau" and cp_choice == "feuille":
            my_score += 1; nb_game += 1; list_nb_game.append(nb_game)
            res = "Vous avez gagné"
            list_cp_score.append(0); list_my_score.append(1)
        elif my_choice == "feuille" and cp_choice == "pierre":
            my_score += 1; nb_game += 1; list_nb_game.append(nb_game)
            res = "Vous avez gagné"
            list_cp_score.append(0); list_my_score.append(1)
        elif my_choice == cp_choice:
            res = "Match null"; nb_game += 1; list_nb_game.append(nb_game); null_score += 1
            list_cp_score.append(0); list_my_score.append(0)
        else:
            cp_score += 1; nb_game += 1; list_nb_game.append(nb_game)
            res = "Vous avez perdu"
            list_cp_score.append(1); list_my_score.append(0)
        request.session['my_score'] = my_score
    request.session['cp_score'] = cp_score
    request.session['null_score'] = null_score
    request.session['nb_game'] = nb_game
    request.session['list_nb_game'] = list_nb_game
    request.session['list_my_score'] = list_my_score
    request.session['list_cp_score'] = list_cp_score
    request.session.modified = True
    
    context = {'form': game, 'prenom': prenom, 
        'list_nb_game': list_nb_game, 'my_choice': my_choice, 
        'cp_choice': cp_choice, 'res': res, 
        'my_score': my_score, 'cp_score': cp_score, 
        'null_score': null_score, 'nb_game': nb_game,
        'list_cp_score': list_cp_score, 'list_my_score': list_my_score}
    return render(request, 'listings/game.html',
                   context)

def reset_scores(request):
    request.session['my_score'] = 0
    request.session['cp_score'] = 0
    request.session['null_score'] = 0
    request.session['nb_game'] = 0
    request.session['list_nb_game'] = []
    request.session['list_my_score'] = []
    request.session['list_cp_score'] = []
    prenom = request.GET.get('prenom', '')
    choix = "choix"
    return redirect('game', prenom=prenom, choix=choix)