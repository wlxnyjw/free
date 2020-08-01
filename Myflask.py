import flask
from os import walk
app = flask.Flask(__name__, static_folder="Z:\电影\三体-广播剧", static_url_path="/assets")
@app.route("/")
def wlx():
    s = []
    for root, dirs, files in walk("Z:\电影\三体-广播剧"):
        for file in files:
            b = root + "\\" + file
            b = b.replace("\\", "/")
            b = b.replace("Z:/电影/三体-广播剧/", "")
            print(b)
            s.append(b)
    return flask.render_template("film.html", s=s)
if __name__ == '__main__':
    app.run()