import secrets, os
from time import localtime, strftime
from datetime import datetime, timedelta
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from app import app, db, bcrypt, socketio, ROOMS
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, ExpirenceForm, ChatIDForm
from sqlalchemy import or_
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User, Post, Review, Agreement, Expirence, Chat, Message
from flask_socketio import send, emit, join_room, leave_room

@app.route("/")
@app.route("/index")
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).limit(10).all()
    experiences = Expirence.query.filter(Expirence.star_rating >= 4).order_by(Expirence.star_rating.desc()).limit(10).all()
    return render_template('index.html', posts=posts, experiences=experiences)

@app.route("/about")
def about():
    return render_template('about.html', title='About Us')


@app.route("/signup", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, phone_number=form.phone_number.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form, title='Signup')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form, title='Login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/home")
@login_required
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static\\images\\profile_pic', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.city = form.city.data
        current_user.verification_number = form.verification_number.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.city.data = current_user.city
        form.verification_number.data = current_user.verification_number
    image_file = url_for('static', filename='images/profile_pic/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

def post_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static\\images\\post_pic', picture_fn)
    output_size = (400, 400)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    picture_file = None
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = post_picture(form.picture.data)
            post = Post(
                title=form.title.data,
                description=form.description.data,
                price=form.price.data,
                city=form.city.data,
                category=form.category.data,
                image_file=picture_file,
                author=current_user
            )

        db.session.add(post)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, image_file=picture_file, legend='New Post')

@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route('/post/<int:post_id>/update')
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    picture_file = None
    form.title.data = post.title
    form.description.data = post.description
    return render_template('create_post.html', title='Update Post', form=form, image_file=picture_file, legend='Update Post')

@app.route('/expirence/new', methods=['GET', 'POST'])
@login_required
def expirence():
    form = ExpirenceForm()
    if form.validate_on_submit():
        expirence = Expirence(
            star_rating=form.rating.data,
            content=form.content.data,
            author6=current_user
        )
        
        db.session.add(expirence)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    
    return render_template('expirence.html', title='New Post', form=form, legend='New Post')


@app.route('/create_chat/<int:author_id>', methods=['GET', 'POST'])
@login_required
def create_chat(author_id):
    # Get the current user's ID
    current_user_id = current_user.id
    
    # Ensure the author exists
    author = Post.query.get_or_404(author_id)

    # Sort the IDs to create a unique chat ID
    user1_id, user2_id = sorted([str(current_user_id), str(author_id)])
    chat_id = f"{user1_id}_{user2_id}"

    # Create an initial message
    initial_message_content = f"I am interested in your post: {author.title}, let's chat"
    initial_message = Message(chat_id=chat_id, user_id=current_user_id, content=initial_message_content, timestamp=datetime.utcnow())
    db.session.add(initial_message)
    db.session.commit()
    
    # Check if the chat already exists, if not, create it
    chat = Chat.query.filter_by(id=chat_id).first()
    if not chat:
        chat = Chat(id=chat_id, user1_id=user1_id, user2_id=user2_id)
        db.session.add(chat)
        db.session.commit()

    # Redirect to the chat page
    return redirect(url_for('chats', chat_id=chat_id))

@app.route('/chats', methods=['GET', 'POST'])
@login_required
def chats():
    # Retrieve all chats where the current user is a participant
    chats = Chat.query.filter(or_(Chat.user1_id == current_user.id, Chat.user2_id == current_user.id)).all()

    # Prepare a dictionary to store messages for each chat
    chat_messages = {}
    for chat in chats:
        # Retrieve messages associated with the chat
        messages = Message.query.filter_by(chat_id=chat.id).all()
        # Store messages in the dictionary with chat_id as key
        chat_messages[chat.id] = messages
    
    # Pass the current date and time to the template
    current_datetime = datetime.now()
    timedelta_class = timedelta


    # Render the template with the user's chats and associated messages
    return render_template('message.html', chats=chats, chat_messages=chat_messages, current_datetime=current_datetime, timedelta_class=timedelta_class)

@app.route('/chat/<chat_id>', methods=['GET'])
@login_required
def chat(chat_id):
    # Retrieve the chat based on the chat ID
    chat = Chat.query.get_or_404(chat_id)
    
    # Check if the current user is one of the participants in the chat
    if current_user.id not in [chat.user1_id, chat.user2_id]:
        abort(403)  # Access forbidden
    else:
        # Fetch messages related to the chat
        messages = Message.query.filter_by(chat_id=chat_id).all()
    
    # Render the chat template with messages
    return render_template('message.html', chat=chat, messages=messages)

def get_user_image_file(user_id):
    user = User.query.get(user_id)
    if user:
        return user.image_file
    return None 

# SocketIO event handler for new messages
@socketio.on('send_message')
def handle_message(data):
    content = data['content']
    chat_id = data['chat_id']
    user_id = current_user.id
    timestamp = datetime.utcnow()
    user_image_file = get_user_image_file(user_id)
    timestamp_str = timestamp.strftime('%H:%M') 

    # Save the message to the database
    message = Message(content=content, chat_id=chat_id, user_id=user_id, timestamp=timestamp)
    db.session.add(message)
    db.session.commit()
    # Emit a 'receive_message' event to all clients
    emit('receive_message', {'content': content, 'chat_id': chat_id, 'user_image_file': user_image_file, 'timestamp': timestamp_str}, broadcast=True)



@app.route('/message', methods=['POST'])
@login_required
def message():
    if request.method == 'POST':
        chat_id = request.form['chat_id']
        content = request.form['content']
        
        # Ensure the chat exists and the current user is part of it
        chat = Chat.query.get_or_404(chat_id)
        if current_user.id not in [chat.user1_id, chat.user2_id]:
            abort(403)  # Access forbidden
        
        # Create a new message
        message = Message(chat_id=chat_id, user_id=current_user.id, content=content)
        db.session.add(message)
        db.session.commit()
        
        # Redirect back to the chat page
        return redirect(url_for('chat', chat_id=chat_id))
    else:
        # Handle GET requests to /message if necessary
        pass
