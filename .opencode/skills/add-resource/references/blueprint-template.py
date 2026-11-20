from flask import Blueprint, jsonify, request

from app import store

# Replace RESOURCE (singular) and RESOURCES (plural, lowercase) everywhere.
bp = Blueprint("RESOURCES", __name__, url_prefix="/RESOURCES")


@bp.get("")
def list_RESOURCES():
    return jsonify(list(store.RESOURCES.values())), 200


@bp.get("/<int:RESOURCE_id>")
def get_RESOURCE(RESOURCE_id):
    # For repairs: look up by slip number instead of an integer id.
    item = store.RESOURCES.get(RESOURCE_id)
    if item is None:
        return jsonify({"error": "RESOURCE not found"}), 404
    return jsonify(item), 200


@bp.post("")
def create_RESOURCE():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400
    # TODO: validate required fields (see docs/business-rules.md if relevant)
    # TODO: money as whole cents, dates as YYYY-MM-DD, errors as {"error": ...} with 400
    RESOURCE_id = max(store.RESOURCES, default=0) + 1
    item = {"id": RESOURCE_id, **data}
    store.RESOURCES[RESOURCE_id] = item
    return jsonify(item), 201


@bp.put("/<int:RESOURCE_id>")
def update_RESOURCE(RESOURCE_id):
    item = store.RESOURCES.get(RESOURCE_id)
    if item is None:
        return jsonify({"error": "RESOURCE not found"}), 404
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400
    # TODO: validate changed fields and allowed changes (status rules, price rules)
    item.update(data)
    return jsonify(item), 200
