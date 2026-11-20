from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"error": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not Found"}), 404

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)