from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(error):
        # api-conventions.md: errors are JSON {"error": "message"}.
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad request"}), 400

    from app.routes import customers
    app.register_blueprint(customers.bp)

    return app
