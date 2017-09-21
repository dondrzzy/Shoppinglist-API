from flask import request
from flask import jsonify
from flask import abort
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

# import configurations file
from instance.config import configurations

# initialize sql-alchemy
db = SQLAlchemy()


def create_instance_of_flask_api(config_mode):
    from app.models import Shoppinglists
    """
    Instantiates Flask and sets configurations for the flask api

    Args:
        config_mode (str): Name of the preferred configuration for this instance

    Returns:
        FlaskAPI: instance of API

    """
    flask_api = FlaskAPI(__name__, instance_relative_config=True)
    flask_api.config.from_object(configurations[config_mode])
    flask_api.config.from_pyfile('config.py')
    flask_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(flask_api)

    @flask_api.route('/shoppinglist/', methods=['POST', 'GET'])
    def shoppinglists():

        if request.method == 'POST':
            # Create a shoppinglist with title provided
            title = str(request.data.get('title', ''))
            if title:
                shopping_list = Shoppinglists(title=title)
                shopping_list.save()
                response = jsonify(
                    {
                      'id': shopping_list.id,
                      'title': shopping_list.title
                    }
                )
                response.status_code = 201
        else:
            shopping_lists = Shoppinglists.get_all()
            results = []

            for shopping_list in shopping_lists:
                list_details = {
                    'id': shopping_list.id,
                    'title': shopping_list.title
                }
                results.append(list_details)
            response = jsonify(results)
            response.status_code = 200

        return response

    @flask_api.route('/shoppinglist/<int:list_id>',
                     methods=['PUT', 'GET', 'DELETE'])
    def shoppinglist(list_id):

        shopping_list = Shoppinglists.query.filter_by(id=list_id).first()
        if not shopping_list:
            abort(404)

        if request.method == 'PUT':
            pass

        if request.method == 'GET':
            pass

        if request.method == 'DELETE':
            pass

    return flask_api


