from flask import (
    Flask,
    jsonify,
    render_template,
    send_from_directory,
    Response,
    request,
    redirect,
)
from bson import ObjectId
from io import BytesIO
import requests
from datetime import datetime
import pyfiglet
from pymongo import MongoClient
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

WAIFUIM = "https://api.waifu.im/search/?excluded_files=3867126be8e260b5&excluded_files=3133&gif=false&excluded_tags=maid"
constant = "&is_nsfw=true"
client = MongoClient("mongodb+srv://shreyash:Galaxy.g05@databasefarmer11.ivwnoas.mongodb.net/?retryWrites=true&w=majority&appName=DatabaseFarmer11")
db = client['test']  # Replace with your actual database name
notes_collection = db.notes

def is_valid_objectid(oid):
    try:
        ObjectId(oid)
        return True
    except:
        return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/notes', methods=['GET'])
def get_notes():
    try:
        # Fetch all notes from the MongoDB collection
        notes = list(notes_collection.find())
        
        # Manually format the response
        formatted_notes = []
        for note in notes:
            formatted_note = {
                "_id": str(note["_id"]),  # Convert ObjectId to string
                "title": note["title"],
                "content": note["content"],
                "createdAt": note.get("createdAt", datetime.utcnow()),  # Default to current UTC time if missing
                "updatedAt": note.get("updatedAt", datetime.utcnow()),  # Default to current UTC time if missing
                "__v": 0  # Adding version field as __v (set to 0 by default)
            }
            formatted_notes.append(formatted_note)
        
        return jsonify(formatted_notes)
    
    except Exception as e:
        return jsonify({"message": "Failed to fetch notes", "error": str(e)}), 500

@app.route('/addNote', methods=['POST'])
def add_note():
    try:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')

        if not title or not content:
            return jsonify({"message": "Title and content are required."}), 400
        
        new_note = {
            "title": title,
            "content": content,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
        result = notes_collection.insert_one(new_note)
        new_note["_id"] = str(result.inserted_id)
        new_note["__v"] = 0  # Adding version field as __v (set to 0 by default)
        return jsonify(new_note), 201
    except Exception as e:
        return jsonify({"message": "Failed to add note", "error": str(e)}), 500
    
@app.route('/deleteNote/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    if not is_valid_objectid(note_id):
        return jsonify({"message": "Invalid note ID"}), 400

    try:
        result = notes_collection.delete_one({"_id": ObjectId(note_id)})
        if result.deleted_count == 0:
            return jsonify({"message": "Note not found"}), 404
        return jsonify({"message": "Note deleted successfully"}), 200
    except Exception as e:
        return jsonify({"message": "Failed to delete note", "error": str(e)}), 500

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


@app.route("/image/ass", methods=["GET"])
def ass():
    url = WAIFUIM + "&included_tags=ass&is_nsfw=false"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        imageUrl = data["images"][0]["url"]
        imageData = requests.get(imageUrl)
        image = BytesIO(imageData.content)
        return Response(image, mimetype="image/png")
    else:
        return jsonify({"API", "Responded with error"})


@app.route("/image/gif", methods=["GET"])
def gif():
    url = "https://api.lunardev.group/nsfw/gif"
    headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2ZDVmN2IzYWExYTNkYjZkYWU1OTY0YyIsImlhdCI6MTcyNTI5ODYxMSwiZXhwIjoxNzU2ODM0NjExfQ.KkQl7GKIzog-LaFP2ohRlAdBNbKofWy9xGrcxed-Mxs"
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        imageUrl = data["url"]
        imageData = requests.get(imageUrl)
        image = BytesIO(imageData.content)
        return Response(image, mimetype="image/png")
    else:
        return jsonify({"API", "Responded with error"})

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify({"message": str(e), "error": str(e.description)}).data
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    print(f"{pyfiglet.figlet_format('Sussy API')}")
    app.run(host="0.0.0.0", port=8000)  # FOR PRODUCTION
    # app.run()
