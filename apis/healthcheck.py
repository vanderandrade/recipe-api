from blueprint.blueprints import healthcheck_blueprint

@healthcheck_blueprint.route('/', methods=['GET'])
def healthcheck():
    return 'OK', 200