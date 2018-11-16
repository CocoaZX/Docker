from  flask import Flask,send_from_directory,render_template,send_file

app = Flask(__name__,static_folder= "/Users/zhangxin/Desktop/Docker-/app/static")

@app.route('/docker')
def docker_mehtod():
    return send_file("static/html/docker.html")

@app.errorhandler(404)
def page_not_found(e):
    return send_file('templates/404.html'),404



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)


