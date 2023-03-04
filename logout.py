import web
from login import login

web.config.debug = True

urls = (
    '/','logout',
    '/login','login',
    '/index', 'index',
)

class logout:
    def GET(self):
        web.setcookie("username", "", expires=-1)
        return web.seeother("/login")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
