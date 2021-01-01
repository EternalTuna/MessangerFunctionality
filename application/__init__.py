from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')


    with app.app_context():
        # imports
        from .views import view
        from .filters import _slice
        from .database import DataBase

        # register routes
        app.register_blueprint(view, url_prefix="/")

        # register context processor
        @app.context_processor
        def slice():
            return dict(slice=_slice)

        return app
        