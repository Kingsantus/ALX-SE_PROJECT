from flask import Blueprint, render_template, request
from app.models import Post, Review, Expirence
from flask_login import login_required

# Create a blueprint named 'main'
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/index")
def index():
    """
    Route for the home page.
    Displays a list of recent posts and experiences.
    """
    # Query the database for the 10 most recent posts
    posts = Post.query.order_by(Post.date_posted.desc()).limit(10).all()
    # Query the database for the 10 highest-rated experiences
    experiences = Expirence.query.filter(Expirence.star_rating >= 4).order_by(Expirence.star_rating.desc()).limit(10).all()
    # Render the index.html template with the posts and experiences
    return render_template('index.html', posts=posts, experiences=experiences)

@main.route("/about")
def about():
    """
    Route for the about page.
    """
    # Render the about.html template
    return render_template('about.html', title='About Us')


@main.route("/home")
@login_required
def home():
    """
    Route for the user's home page.
    Displays the user's posts, reviews, and review counts.
    """
    # Get the current page number from the request arguments
    page = request.args.get('page', 1, type=int)
    # Query the database for paginated posts
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5)
    # Query the database for all reviews
    reviews = Review.query.all()
    # Dictionary to store review counts for each post
    post_review_counts = {}
    # Calculate the number of reviews for each post
    for post in posts:
        review_count = Review.query.filter_by(author_id=post.author.id).count()
        post_review_counts[post.id] = review_count
    # Render the home.html template with posts, reviews, and review counts
    return render_template('home.html', posts=posts, reviews=reviews, post_review_counts=post_review_counts, page=page)
