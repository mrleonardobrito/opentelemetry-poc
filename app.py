from flask import Flask, jsonify
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import os
from dotenv import load_dotenv

load_dotenv()

trace.set_tracer_provider(TracerProvider())

span_processor = BatchSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

app = Flask(__name__)

FlaskInstrumentor().instrument_app(app)

@app.route('/')
def index():
    return jsonify(message="Hello, World!")

@app.route('/example')
def example():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("example-span"):
        return jsonify(message="This is an example endpoint")

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port)