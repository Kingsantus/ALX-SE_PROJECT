import secrets, os
from time import localtime, strftime
from datetime import datetime, timedelta
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from app import app, db, bcrypt, socketio, mail
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, ExpirenceForm, ReviewForm, RequestResetForm, ResetPasswordForm
from sqlalchemy import or_
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User, Post, Review, Agreement, Expirence, Chat, Message
from flask_socketio import send, emit, join_room, leave_room
from flask_mail import Message














