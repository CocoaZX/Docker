from  flask import Flask,send_from_directory,render_template,send_file
from flask_bootstrap import Bootstrap

app = Flask(__name__,static_folder= "/Users/zhangxin/Desktop/Docker-/app/static")
bootstrap = Bootstrap(app)

@app.route('/docker')
def docker_mehtod():
    return send_file("static/html/docker.html")

@app.route('/base')
def base_mehtod():
    return send_file("static/html/404.html")

@app.route('/')
def navi_mehtod():
    return render_template('He.html')
    # return send_file("static/html/He.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    # return send_file('templates/404.html'),404



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)


