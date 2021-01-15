from flask import Flask, request, render_template
from models import Storage, BlogPostModel
from forms import BlogPostForm
import logging
import config

logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

@app.route('/', methods=['GET', 'POST'])
def home():
    storage = Storage()
    all_items = storage.items

    

    if request.method == 'POST':
        form = BlogPostForm(request.form)
        if form.validate():
            model = BlogPostModel(form.data)
            all_items.append(model)
            print('valid', 200)
        else:
            logger.error('Wrong form!')
            print('invalid', 400)
    # elif request.method == 'GET':
    #     return 'hello world!', 200
    else: 
        form = BlogPostForm()
        
    return render_template(
        'home.html',
        form=form,
        items=all_items,
    )



    

if __name__ == '__main__':
    app.run()