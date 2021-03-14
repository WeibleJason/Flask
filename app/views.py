from app import app
from app import jsonify, request, render_template

@app.route('/', methods=['GET', 'POST'])
def index():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON header

    return render_template('public/index.html')

@app.route('/admin')
def admin():
    return render_template('admin/dashboard.html')