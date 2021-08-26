from flask import Flask

def create_app(app_name='recipe'):
    app = Flask(app_name)

    @app.route('/')
    def healthcheck():
        return 'OK', 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)