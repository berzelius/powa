"""
import os
import webapp
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))
"""


from bottle import Bottle, run, static_file, view
import utils


def main():
    conf = utils.get_conf()

    host = conf["bottle"]["host"]
    port = conf["bottle"]["port"]
    route_statics = conf["bottle"]["route_statics"]
    statics_path = conf["bottle"]["statics_path"]
    video_paths = conf["bottle"]["video_paths"]

    app = Bottle()

    if route_statics is True:
        @app.route('/static/<filepath:path>')
        def server_static(filepath):
            return static_file(filepath, root=statics_path)

    @app.route('/')
    def index():
        return "Hello World!"

    @app.route('/videos')
    @view('views/videos.tpl')
    def videos():
        tpl_vars = dict()
        tpl_vars["video_paths"] = video_paths
        return tpl_vars

    return app, host, port





# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application, host, port = main()
