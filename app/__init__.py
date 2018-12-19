from flask import Flask,send_from_directory,render_template,send_file
from flask_bootstrap import Bootstrap
from datetime import  timedelta

app = Flask(__name__,static_folder= "/users/zhangxin/desktop/docker-/app/static")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=2)
bootstrap = Bootstrap(app)#模板


@app.route('/docker')
def docker_mehtod():
    return send_file("static/html/docker.html")

@app.route('/oc')
def oc_mehtod():
    return send_file("static/html/typeOC.html")


@app.route('/typeDocker')
def typeDocker_mehtod():
    return send_file("static/html/typeDocker.html")


@app.route('/base')
def base_mehtod():
    return send_file("static/html/404.html")

@app.route('/')
def navi_mehtod():
    return send_file("static/html/typeOC.html")


@app.route('/objective-c-runtime-1')
def oc_runtime_1():
    return send_file("static/html/Objective-C/objective-c-runtime-1.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    # return send_file('templates/404.html'),404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


