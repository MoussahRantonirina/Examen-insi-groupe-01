import web
import nav 
from database import Db
web.config.debug = True

urls = (
    '/rank','rank',
)
class rank:
    def GET(self):
        d = Db()
        db = d.getDb()
        albums = db.select('Album', limit=10)
        artists = db.select('Artist', limit=10)
        result = '<html><head><meta charset="UTF-8"><title>iMusic - Classement</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '</head>'
        result += '<body>'
        result += nav.navbar()
        result += '<div class="container">'
        result += '<h4 class="text-center my-5">Notre top 10 des meilleures musiques du mois</h4>'
        result += '<table class="table table-striped table-bordered mx-auto">'
        result += '<tr class="table-bordered thead-dark text-center"><th class="p-3 table-dark">ID</th><th class="p-3 table-dark">Artist</th><th class="p-3 table-dark">Album Title</th></tr>'
        for artist in artists: 
            result += '<tr class="table table-striped table-bordered">'
            result += '<td class="table-primary p-2 ">'+ str(artist.ArtistId) +'</td>'
            for album in albums:
                result += '<td>' + artist.Name + '</td>'
                result += '<td>' + album.Title + '</td>'
                break
            result += '</tr>'
        result += '</table>'
        result += '</div>'
        result += '</body></html>'
        return result

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()    