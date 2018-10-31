from  flask import Flask,send_from_directory,render_template,send_file
import os

app = Flask(__name__,static_folder= "/Users/zhangxin/Desktop/Docker-/app/static")
print( os.getcwd() + "/static")

@app.route('/')
def docker_mehtod():
    return send_file("static/html/docker.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=12333)


