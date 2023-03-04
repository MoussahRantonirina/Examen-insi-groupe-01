import web
import nav 
from details import details
from database import Db
web.config.debug = True

urls = (
    '/index', 'index',
    '/liste','liste',
    '/details','details'
)
class index:
    def GET(self):
        return '''<html>
        <head>
            <meta charset="UTF-8">
            <title>iMusic - Accueil</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            <style>
                body{
                    background-image: url('https://w.wallhaven.cc/full/4l/wallhaven-4lrojy.jpg');
                    background-size: cover;
                }
                #msg{
                    text-align: center;
                    position: absolute;
                    top: 40%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    color: white;
                }
            </style>
        </head>
        <body>
            ''' + nav.navbar() + '''
            <div id="msg">
                <h1>Bienvenue sur iMusic</h1>
                <p>Découvrez notre top 10 des meilleures musiques du moment</p>
            </div>
        </body>
        </html>
        '''  

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

