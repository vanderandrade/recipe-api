from flask import Flask
from apis.healthcheck import healthcheck_blueprint

def create_app(app_name='recipe'):
    app = Flask(app_name)

    app.register_blueprint(healthcheck_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)