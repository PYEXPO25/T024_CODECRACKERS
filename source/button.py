from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('button.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    selected_slot = request.form.get("selected_slot")
    # Get slot from form
    if selected_slot:
        return f"Slot {selected_slot} reserved successfully!"
    return "No slot selected.", 400

if __name__ == '__main__':
    app.run(debug=True)
