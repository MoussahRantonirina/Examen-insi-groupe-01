def navbar():
    result = '<nav class="navbar navbar-expand-lg navbar-light bg-primary">'
    result += '<a class="col-3 navbar-brand" href="#">iMusic</a>'
    result += '</button>'
    result += '<div class="col-6 offset-3 collapse navbar-collapse text-center"  id="navbarNav">'
    result += '<ul class="navbar-nav ml-auto">'
    result += '<li class="nav-item">'
    result += '<a class="nav-link text-light" href="/index">Accueil</a>'
    result += '</li>'
    result += '<li class="nav-item">'
    result += '<a class="nav-link text-light" href="/rank">Classement</a>'
    result += '</li>'
    result += '<li class="nav-item">'
    result += '<a class="nav-link text-light" href="/details">Details</a>'
    result += '</li>'
    result += '<li class="nav-item">'
    result += '<a class="nav-link text-light" href="/logout">Déconnexion</a>'
    result += '</li>'
    result += '</ul>'
    result += '</div>'
    result += '</nav>'
    return result
