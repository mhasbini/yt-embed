from flask import Flask, request, send_file, render_template
from io import BytesIO

from .processor import embed_image

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/embed")
def embed():
    video_id = request.args.get("v", None)

    return send_file(BytesIO(embed_image(video_id)), mimetype="image/png")


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
