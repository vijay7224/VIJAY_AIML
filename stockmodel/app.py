from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Temporary storage (use DB later if needed)
files = []

# Home page
@app.route('/')
def index():
    return render_template('index.html', files=files)

# Add file (Google Drive link)
@app.route('/add', methods=['POST'])
def add():
    filename = request.form.get('filename')
    drive_link = request.form.get('link')
    file_type = request.form.get('type')

    # Extract FILE ID from Google Drive link
    try:
        file_id = drive_link.split('/d/')[1].split('/')[0]
    except:
        return "❌ Invalid Google Drive link"

    # Convert links
    view_url = f"https://drive.google.com/uc?export=view&id={file_id}"
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    files.append({
        "id": len(files),
        "filename": filename,
        "file_id": file_id,
        "view_url": view_url,
        "download_url": download_url,
        "type": file_type
    })

    return redirect(url_for('index'))

# View page
@app.route('/view/<int:id>')
def view_file(id):
    file = next((f for f in files if f["id"] == id), None)
    if not file:
        return "File not found"
    return render_template("view.html", file=file)

# Delete file
@app.route('/delete/<int:id>')
def delete(id):
    global files
    files = [f for f in files if f["id"] != id]
    return redirect(url_for('index'))

# Run app (Render compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)