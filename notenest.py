from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:  # Ensure note is not empty
            notes.append(note)
    return render_template("home.html", notes=notes)

@app.route('/update_note', methods=["POST"])
def update_note():
    note_index_str = request.form.get("note_index")
    updated_note = request.form.get("updated_note")

    try:
        if note_index_str is not None:
            note_index = int(note_index_str)
            if 0 <= note_index < len(notes):
                notes[note_index] = updated_note
            else:
                raise IndexError
        else:
            raise ValueError("Note index is None")
    except (ValueError, IndexError) as e:
        return f"Error updating note: {e}"

    return render_template("home.html", notes=notes)

@app.route('/delete_note', methods=["POST"])
def delete_note():
    note_index_str = request.form.get("note_index")

    try:
        if note_index_str is not None:
            note_index = int(note_index_str)
            if 0 <= note_index < len(notes):
                del notes[note_index]
            else:
                raise IndexError
        else:
            raise ValueError("Note index is None")
    except (ValueError, IndexError) as e:
        return f"Error deleting note: {e}"

    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
