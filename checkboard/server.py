# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"

app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def home():
    # Return the string 'Hello World!' as a response
    return render_template('index.html', x_num=8, y_num=8)


@app.route('/<int:num>')
def change_y(num):
    # Return the string 'Hello World!' as a response
    return render_template('index.html', x_num=8, y_num=num)


@app.route('/<int:x_num>/<int:y_num>')
def num_of_boxes(x_num, y_num):
    return render_template('index.html', x_num=x_num, y_num=y_num)


@app.route('/<int:x_num>/<int:y_num>/<string:color1>/<string:color2>')
def change_boxes_colors(x_num, y_num, color1, color2):
    return render_template('index.html', x_num=x_num, y_num=y_num, color1=color1, color2=color2)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
