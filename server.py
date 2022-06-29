from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    return render_template('list.html', user_stories=user_stories)


@app.route('/story', methods=['GET','POST'])
def story():
    if request.method == 'POST':
        user_story = {}
        user_story['id'] = data_handler.generate_id()
        user_story['title'] = request.form['title']
        user_story['user_story'] = request.form['story']
        user_story['acceptance_criteria'] = request.form['acceptance-criteria']
        user_story['business_value'] = request.form['value']
        user_story['estimation'] = request.form['estimation']
        user_story['status'] = 'planning'

        data_handler.add_user_story(user_story)
        return redirect('/')
    return render_template('story.html')


@app.route('/story/<int:id>', methods=['GET', 'POST'])
def update_story(id):
    if request.method == 'POST':
        user_story = {}
        user_story['id'] = id
        user_story['title'] = request.form['title']
        user_story['user_story'] = request.form['story']
        user_story['acceptance_criteria'] = request.form['acceptance-criteria']
        user_story['business_value'] = request.form['value']
        user_story['estimation'] = request.form['estimation']
        user_story['status'] = request.form['status']

        user_stories = data_handler.get_all_user_story()

        for row in user_stories:
            if row['id'] == user_story['id']:
                user_stories[user_stories.index(row)] = user_story

        data_handler.update_user_story(user_stories)
        return redirect('/')

    user_stories = data_handler.get_all_user_story()
    for row in user_stories:
        if row['id'] == id:
            user_story_to_be_updated = row
    return render_template('update-story.html', user_story=user_story_to_be_updated, status_options=data_handler.STATUSES, id=id)

#TODO ask about status: in progress - only showing in - when clicked to update it's not even selected

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
