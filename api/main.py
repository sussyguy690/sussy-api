from flask import (
    Flask,
    jsonify,
    render_template,
    send_from_directory,
    Response,
    redirect,
)
from io import BytesIO
import requests
import pyfiglet

app = Flask(__name__)

WAIFUIM = "https://api.waifu.im/search/?excluded_files=3867126be8e260b5&excluded_files=3133&gif=false&excluded_tags=maid"
constant = "&is_nsfw=true"


@app.route("/image/oppai", methods=["GET"])
def oppai():
    url = WAIFUIM + "&included_tags=oppai" + constant
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        imageUrl = data["images"][0]["url"]
        imageData = requests.get(imageUrl)
        image = BytesIO(imageData.content)
        return Response(image, mimetype="image/png")
    else:
        return jsonify({"API", "Responded with error"})
    

@app.route("/image/milf", methods=["GET"])
def milf():
    url = WAIFUIM + "&included_tags=milf" + constant
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        imageUrl = data["images"][0]["url"]
        imageData = requests.get(imageUrl)
        image = BytesIO(imageData.content)
        return Response(image, mimetype="image/png")
    else:
        return jsonify({"API", "Responded with error"})
    
@app.route("/image/ecchi", methods=["GET"])
def ecchi():
    url = WAIFUIM + "&included_tags=ecchi" + constant
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        imageUrl = data["images"][0]["url"]
        imageData = requests.get(imageUrl)
        image = BytesIO(imageData.content)
        return Response(image, mimetype="image/png")
    else:
        return jsonify({"API", "Responded with error"})
    
@app.route("/image/hentai", methods=["GET"])
def hentai():
    url = WAIFUIM + "&included_tags=hentai" + constant
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        imageUrl = data["images"][0]["url"]
        imageData = requests.get(imageUrl)
        image = BytesIO(imageData.content)
        return Response(image, mimetype="image/png")
    else:
        return jsonify({"API", "Responded with error"})
    
@app.route("/image/waifu", methods=["GET"])
def waifu():
    url = WAIFUIM + "&included_tags=waifu&is_nsfw=false"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        imageUrl = data["images"][0]["url"]
        imageData = requests.get(imageUrl)
        image = BytesIO(imageData.content)
        return Response(image, mimetype="image/png")
    else:
        return jsonify({"API", "Responded with error"})
    
@app.route("/image/uniform", methods=["GET"])
def uniform():
    url = WAIFUIM + "&included_tags=uniform&is_nsfw=false"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        imageUrl = data["images"][0]["url"]
        imageData = requests.get(imageUrl)
        image = BytesIO(imageData.content)
        return Response(image, mimetype="image/png")
    else:
        return jsonify({"API", "Responded with error"})


if __name__ == "__main__":
    print(f"{pyfiglet.figlet_format('Sussy API')}")
    app.run(host="0.0.0.0", port=8000)  # FOR PRODUCTION
    # app.run()
