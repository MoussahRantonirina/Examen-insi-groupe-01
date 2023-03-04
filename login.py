import web
from index import index
web.config.debug = True

urls = (
    '/login','login',
     '/index', 'index',
)


class login:
    def GET(self):
        return '''<html>
        <head>
            <meta charset="UTF-8">
            <title>Connexion</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
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

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
