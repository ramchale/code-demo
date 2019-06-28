from flask import Flask, request, render_template

app = Flask(__name__)


properties = {
    '0': {'large': True, 'legs': 2, 'color': 'green'},  # Hulk
    '1': {'large': False, 'legs': 4, 'color': 'orange'},  # Fox
    '2': {'large': True, 'legs': 4, 'color': 'grey'},  # Elephant
    '3': {'large': False, 'legs': 0, 'color': 'purple'},  # Ekans
    '4': {'large': True, 'legs': 2, 'color': 'grey'}  # Totoro
}

images = {
    'hulk': 'hulk.jpg',
    'fox': 'fox.jpg',
    'elephant': 'elephant.jpg',
    'ekans': 'ekans.gif',
    'totoro': 'totoro.jpg'
}


def pick_images(large, legs, color):
    selected_images = []

    # TODO - Add more logic here to select the right image based on the three properties
    if large:
        selected_images = [images['hulk']]

    return selected_images


@app.route('/')
def default():
    return render_template('index.j2.html')


@app.route('/pick-a-thing/', methods=['GET', 'POST','DELETE', 'PATCH'])
def pick_a_thing():
    if request.method == 'GET':
        selected_images=[]
        # selected_images=images # Uncomment to display all
        return render_template('pick-a-thing.j2.html', images=selected_images)

    if request.method == 'POST':
        selected_item = request.form.get('selection')

        item = properties[selected_item]

        selected_images = pick_images(item['large'], item['legs'], item['color'])

        return render_template('pick-a-thing.j2.html', selected=selected_item, images=selected_images)


if __name__ == '__main__':
    app.run()
