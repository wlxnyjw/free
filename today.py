from flask import Flask,render_template
from os import walk
app=Flask(__name__,static_folder="Z:\电影\三体-广播剧",static_url_path="/yjw")
@app.route("/")
def wlx():
    s=[]
    for root,dirs,files in walk("Z:\电影\三体-广播剧"):
        for file in files:
            b=root+"\\"+file
            b=b.replace("\\","/")
            b=b.replace("Z:/电影/三体-广播剧/","")
            print(b)
            s.append(b)
    return render_template("mood.html",s=s)
if __name__ == '__main__':
    app.run()
# fixed
