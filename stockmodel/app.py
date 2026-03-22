from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# ==============================
# MongoDB Atlas Config
# ==============================
client = MongoClient("mongodb+srv://vijaysuryawanshi7224_db_user:vijay%402005@cluster0.ckvnjfm.mongodb.net/collegedb?retryWrites=true&w=majority") 

db = client["student_db"]
collection = db["documents"]
# ==============================
# Home Page
# ==============================
@app.route('/')
def index():
    files = list(collection.find())
    return render_template('index.html', files=files)

# ==============================
# Add File (Google Drive link)
# ==============================
@app.route('/add', methods=['POST'])
def add():
    filename = request.form.get('filename')
    drive_link = request.form.get('link')
    file_type = request.form.get('type')

    try:
        file_id = drive_link.split('/d/')[1].split('/')[0]
    except:
        return "❌ Invalid Google Drive link"

    view_url = f"https://drive.google.com/uc?export=view&id={file_id}"
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    collection.insert_one({
        "filename": filename,
        "file_id": file_id,
        "view_url": view_url,
        "download_url": download_url,
        "type": file_type
    })

    return redirect(url_for('index'))

# ==============================
# View File
# ==============================
@app.route('/view/<id>')
def view_file(id):
    file = collection.find_one({"_id": ObjectId(id)})
    if not file:
        return "File not found"
    return render_template("view.html", file=file)

# ==============================
# Delete File
# ==============================
@app.route('/delete/<id>')
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('index'))

# ==============================
# Run
# ==============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)