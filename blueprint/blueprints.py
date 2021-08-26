from flask import Blueprint

healthcheck_blueprint = Blueprint('/', __name__)
author_blueprint = Blueprint('author', __name__)
recipe_blueprint = Blueprint('recipe', __name__)
search_blueprint = Blueprint('search', __name__)
