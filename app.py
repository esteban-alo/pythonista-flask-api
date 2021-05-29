from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{
	"name": "My wonderful store",
	"items": [{
		"name": "My Item",
		"price": 15.99
	}]
}]


@app.route('/store', methods=['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {"name": request_data["name"], "items": []}
	stores.append(new_store)
	return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
	for store_item in stores:
		if store_item["name"] == name:
			return jsonify(store_item)
	return jsonify({"message": "store not found"})


@app.route('/store')
def get_stores():
	return jsonify({"stores": stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	for store_item in stores:
		if store_item["name"] == name:
			new_item = {
					"name": request_data["name"],
					"price": request_data["price"]
			}
			store_item["items"].append(new_item)
			return jsonify(new_item)
	return jsonify({"message": "store not found"})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for store_item in stores:
		if store_item["name"] == name:
			return jsonify({"items": store_item["items"]})
	return jsonify({"message": "store not found"})


app.run(port=5000, host="0.0.0.0")

