from flask import Flask, request, jsonify
import script
from script import Sentiment
import time, json, datetime, os


app = Flask(__name__)
obj = script.Sentiment()

@app.route('/get', methods = ["GET"])
def getApi():
	if request.method == "GET":
		try:
			query = request.args.get('q')
			response = obj.get_response(query)
			timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
			return jsonify({
				'status': 'success',
				'query': query,
				'response': response,
				'dated': timestamp
				});

		except Exception as e:
			return jsonify({
				'status': str(e)
				})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)