from flask import Flask, jsonify, request
from flask_management_endpoints import z_blueprint
from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__)
app.register_blueprint(z_blueprint, url_prefix="/")
metrics = PrometheusMetrics(app)

@app.route('/', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "Hello World"}
        return jsonify(data)

@app.route('/metrics')
def simple_get():
    pass
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

if __name__ == "__main__":
    app.run()