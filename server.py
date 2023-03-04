import web
import nav 
from index import index
from rank import rank
from details import details
from database import Db
web.config.debug = True

urls = (
    '/', 'login',
    '/index', 'index',
    '/login', 'login',
    '/rank','rank',
    '/details','details',
    '/logout', 'logout'
)
class login:
    def GET(self):
        return '''<html>
<head>
    <meta charset="UTF-8">
    <title>Connexion</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <style>
        body {
            background-image: url('https://w.wallhaven.cc/full/1k/wallhaven-1kzryg.png');
            background-size: cover;
        }
        .login-container {
            background-color: transparent;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            max-width: 300px;
            margin: auto;
            margin-top: 150px;
            backdrop-filter: blur(5px);
        }
        .form-control {
            background-color: rgba(255, 255, 255, 0.8);
            color: #555;
        }
        h1 {
            color: #fff;
            text-align: center;
            font-size: 2em;
            margin-bottom: 30px;
        }
        label {
            color: #fff;
        }
    </style>            
</head>
<body>
    <div class="login-container">
        <h1>Connexion</h1>
        <form method="POST" action="/">
            <div class="form-group">
                <label for="username">Nom d'utilisateur :</label>
                <input type="text" class="form-control" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Mot de passe :</label>
                <input type="password" class="form-control" id="password" name="password" required>
            </div>
            <button type="submit" class="btn btn-primary">Se connecter</button>
        </form>
    </div>
</body>
</html>

        '''

    def POST(self):
        username = web.input().username
        password = web.input().password

        if username == "admin" and password == "admin":
            web.setcookie("username", username)
            return web.seeother("/index")
        else:
            return "Nom d'utilisateur ou mot de passe incorrect."

class logout:
    def GET(self):
        web.setcookie("username", "", expires=-1)
        return web.seeother("/")



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
