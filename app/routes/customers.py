from flask import Blueprint, jsonify, request

from app import store

bp = Blueprint("customers", __name__, url_prefix="/customers")


@bp.get("")
def list_customers():
    return jsonify(list(store.CUSTOMERS.values())), 200


@bp.get("/<int:customer_id>")
def get_customer(customer_id):
    item = store.CUSTOMERS.get(customer_id)
    if item is None:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify(item), 200


@bp.post("")
def create_customer():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400
    # Customers need a name and a phone number (docs/business-rules.md);
    # without a phone number nothing is saved (400). Phone format is open
    # (docs/business-rules.md, "Open") - stored as typed.
    if not data.get("name") or not data.get("phone_number"):
        return jsonify({"error": "Name and phone number are required"}), 400
    customer_id = max(store.CUSTOMERS, default=0) + 1
    item = {"id": customer_id, **data}
    store.CUSTOMERS[customer_id] = item
    return jsonify(item), 201


@bp.put("/<int:customer_id>")
def update_customer(customer_id):
    item = store.CUSTOMERS.get(customer_id)
    if item is None:
        return jsonify({"error": "Customer not found"}), 404
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400
    # A customer always needs a name and a phone number.
    if "name" in data and not data["name"]:
        return jsonify({"error": "Name is required"}), 400
    if "phone_number" in data and not data["phone_number"]:
        return jsonify({"error": "Phone number is required"}), 400
    item.update(data)
    return jsonify(item), 200
