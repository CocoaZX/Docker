from  flask import Flask,send_from_directory,render_template
import os

app = Flask(__name__)

@app.route('/')
def docker_mehtod():
    root_dir = os.path.dirname(os.getcwd())
    return app.send_static_file("html/docker.html")#homepage.html在templates文件夹下


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=12333)


