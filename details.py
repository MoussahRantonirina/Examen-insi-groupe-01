import web
import nav 
from database import Db

web.config.debug = True

urls = (
    '/details','details',
)

class details:
    def GET(self):
        d = Db()
        db = d.getDb()
        albums=db.select('Album', limit=10)
        artists=db.select('Artist', limit=10)
        genres=db.select('Genre', limit=10)
        mdtype=db.select('MediaType', limit=10)
        plist=db.select('Playlist', limit=10)
        cstm=db.select('Customer', limit=10)
        country=db.select('Customer', limit=10)

        result = '<html><head><meta charset="UTF-8"><title> iMusic - Album details</title>'
        result += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">'
        result += '<style>'
        result += '.carousel-control-prev-icon, .carousel-control-next-icon{background-color: black; border-radius: 20%;}'
        result += '.carousel-control-prev, .carousel-control-next{ height: 20px; margin-top: 250px;}'
        result += '</style>'
        result += '</head>'
        result += '<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>'
        result += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>'
        result += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>'
        result += '<body>'
        result += nav.navbar()
        result += '<div class="container">'
        result += '<h4 class="text-center my-5">Informations supplémentaire sur le classement</h4>'

        result += '<div id="myCarousel" class="carousel slide" data-ride="carousel">'
        result += '<ol class="carousel-indicators">'
        for i in range(len(artists)):
            if i == 0:
                result += '<li data-target="#myCarousel" data-slide-to="'+str(i)+'" class="active"></li>'
            else:
                result += '<li data-target="#myCarousel" data-slide-to="'+str(i)+'"></li>'
        result += '</ol>'
        result += '<div class="carousel-inner">'
        for i, artist in enumerate(artists):
            result += '<div class="carousel-item '
            if i == 0:
                result += 'active'
            result += '">'
            result += '<table class="table table-striped table-bordered mx-auto">'
            result += '<tr class="table-bordered thead-dark text-center"><th class="p-3 table-dark">ID</th><th class="p-3 table-dark">Title</th><th class="p-3 table-dark">Artist</th><th class="p-3 table-dark">Genre</th><th class="p-3 table-dark">Country</th><th class="p-3 table-dark">Mediatype</th><th class="p-3 table-dark">Company Name</th><th class="p-3 table-dark">Playlist</th></tr>'
            result += '<tr class="table table-striped table-bordered">'
            result += '<td class="table-primary p-2 ">'+ str(artist.ArtistId) +'</td>'
            for album in albums:
                result += '<td class="p-3">' + album.Title + '</td>'
                result += '<td class="p-3">' + artist.Name + '</td>'
                break
            for genre in genres:
                result += '<td class="p-3">' + genre.Name + '</td>'
                break
            for customer in country:
                result += '<td class="p-3">'+ customer.Country+'</td>'  
                break
            for mediatype in mdtype:
                result += '<td class="p-3">' + mediatype.Name + '</td>'
                break
            for customer in cstm:
                result += '<td class="p-3">'+str(customer.Company)+'</td>' 
                break
            for playlist in plist:
                result += '<td class="p-3">' + playlist.Name + '</td>'
                break 
            result += '</tr>'
            result += '</table>'
            result += '</div>'
        result += '</div>'
        result += '</div>'
        result += '<a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev" style="left: 0">'
        result += '<span class="carousel-control-prev-icon" aria-hidden="true"></span>'
        result += '<span class="sr-only">Previous</span>'
        result += '</a>'
        result += '<a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next" style="right: 0">'
        result += '<span class="carousel-control-next-icon" aria-hidden="true"></span>'
        result += '<span class="sr-only">Next</span>'
        result += '</a>'
        result += '</div>'
        result += '</body></html>'
        return result
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
