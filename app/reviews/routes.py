from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Expirence, Review
from app import db
from .forms import ExpirenceForm, ReviewForm
from app.models import User

reviews = Blueprint('reviews', __name__)

@reviews.route('/expirence/new', methods=['GET', 'POST'])
@login_required
def expirence():
    """
    Route to create a new experience post.
    Users can create new experience posts by submitting the experience form.
    """
    # Create an instance of the ExperienceForm
    form = ExpirenceForm()
    # If the form is submitted and validated
    if form.validate_on_submit():
        # Create a new Experience object with the form data and the current user as the author
        expirence = Expirence(
            star_rating=form.rating.data,
            content=form.content.data,
            author6=current_user
        )
        # Add the review to the database and commit the session
        db.session.add(expirence)
        db.session.commit()
        # Flash a success message and redirect the user to the home page
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    # Render the expirence.html template with the form
    return render_template('expirence.html', title='New Post', form=form, legend='New Post')

@reviews.route('/review/<int:author_id>', methods=['GET', 'POST'])
@login_required
def review(author_id):
    """
    Route to review a user.
    Users can submit reviews for other users by filling out the review form.
    """
    author = User.query.get_or_404(author_id)
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(
            star_rating=form.rating.data,
            user_id=current_user.id,
            author_id=author.id,
            content=form.content.data
        )
        
        db.session.add(review)
        db.session.commit()

        flash('Your review has been submitted!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('review.html', title='Review User', form=form, legend='New Review')