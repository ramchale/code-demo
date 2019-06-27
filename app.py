from flask import Flask, request, render_template

app = Flask(__name__)

properties = {
    '0': {'large': True, 'legs': 2, 'color': 'green'}, # Hulk
    '1': {'large': False, 'legs': 4, 'color': 'grey'}, # Fox
    '2': {'large': True, 'legs': 4, 'color': 'brown'}, # Elephant
    '3': {'large': False, 'legs': 0, 'color': 'purple'}, # Ekans
    '4': {'large': True, 'legs': 2, 'color': 'grey'} # Totoro
}

# TODO - Get some images and replace these and the tag in the HTML with actual images
images = ['Hulk', 'Fox', 'Elephant', 'Ekans', 'Totoro']


def pick_images(large, legs, color):
    selected_images = []

    # TODO - (For the kids not us) Add more logic here to select the right image based on the three properties
    if large:
        selected_images = [images[0]]

    return selected_images


@app.route('/')
def default():
    return render_template('index.j2.html')


@app.route('/pick-a-thing/', methods=['GET', 'POST','DELETE', 'PATCH'])
def pick_a_thing():
    if request.method == 'GET':
        return render_template('pick-a-thing.j2.html', images=images)

    if request.method == 'POST':
        selected_item = request.form.get('selection')

        item = properties[selected_item]

        selected_images = pick_images(item['large'], item['legs'], item['color'])

        return render_template('pick-a-thing.j2.html', images=selected_images)


if __name__ == '__main__':
    app.run()
