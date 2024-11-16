from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.schemas.schema import CreateUserSchema, UserSchema
from flaskr.controllers.user_controller import UserController

bp = Blueprint("users", __name__)


@bp.route("/users")
class Users(MethodView):
    @bp.response(200, UserSchema(many=True))
    def get(self):
        return UserController.get_all()

    @bp.arguments(CreateUserSchema)
    @bp.response(201)
    def post(self, data):
        return UserController.create(data)


@bp.route("/users/<user_id>")
class UserById(MethodView):
    @bp.response(200, UserSchema)
    def get(self, user_id):
        return UserController.get_by_id(user_id)

    @bp.response(204)
    def delete(self, user_id):
        return UserController.delete(user_id)
