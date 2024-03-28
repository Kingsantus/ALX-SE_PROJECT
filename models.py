from app import db
from enum import Enum as PythonEnum
from sqlalchemy import Enum
from datetime import datetime

class Category(PythonEnum):
    KEYBOARDS_SYNTHESIZERS = 'Keyboards & Synthesizers'
    ELECTRIC_GUITARS = 'Electric Guitars'
    ACOUSTIC_GUITARS = 'Acoustic Guitars'
    BASS_GUITARS = 'Bass Guitars'
    DRUM_KITS = 'Drum Kits'
    ELECTRONIC_DRUM_MACHINES = 'Electronic Drum Machines'
    DJ_CONTROLLERS = 'DJ Controllers'
    TURNTABLES = 'Turntables'
    MIXERS_AUDIO = 'Mixers (Audio)'
    MICROPHONES = 'Microphones'
    HEADPHONES = 'Headphones'
    PA_SYSTEMS = 'PA Systems'
    STUDIO_MONITORS = 'Studio Monitors'
    STAGE_LIGHTING = 'Stage Lighting'
    EFFECTS_PEDALS = 'Effects Pedals'
    AUDIO_INTERFACES = 'Audio Interfaces'
    MIDI_CONTROLLERS = 'MIDI Controllers'
    DIGITAL_PIANOS = 'Digital Pianos'
    STAGE_AMPLIFIERS = 'Stage Amplifiers'
    RECORDING_EQUIPMENT = 'Recording Equipment'
    KARAOKE_MACHINES = 'Karaoke Machines'
    CD_PLAYERS_RECORDERS = 'CD Players & Recorders'
    TAPE_DECKS = 'Tape Decks'
    VINYL_RECORDS = 'Vinyl Records'
    CABLES_CONNECTORS = 'Cables & Connectors'
    MUSICAL_INSTRUMENT_CASES_BAGS = 'Musical Instrument Cases & Bags'
    MUSIC_STANDS = 'Music Stands'
    INSTRUMENT_ACCESSORIES = 'Instrument Accessories (e.g., guitar picks, drumsticks)'
    SPEAKER_STANDS = 'Speaker Stands'
    SUBWOOFERS = 'Subwoofers'
    PORTABLE_PA_SYSTEMS = 'Portable PA Systems'
    LIVE_SOUND_MIXERS = 'Live Sound Mixers'
    WIRELESS_MICROPHONE_SYSTEMS = 'Wireless Microphone Systems'
    IN_EAR_MONITORS = 'In-Ear Monitors'
    DIGITAL_AUDIO_WORKSTATIONS = 'Digital Audio Workstations (DAWs)'
    MUSIC_PRODUCTION_SOFTWARE = 'Music Production Software'
    SAMPLE_LIBRARIES_SOUND_PACKS = 'Sample Libraries & Sound Packs'
    SOUND_MODULES = 'Sound Modules'
    MUSIC_PRODUCTION_CONTROLLERS = 'Music Production Controllers'
    ANALOG_SYNTHESIZERS = 'Analog Synthesizers'
    EFFECTS_PROCESSORS = 'Effects Processors'
    SPEAKER_CABINETS = 'Speaker Cabinets'
    SPEAKER_COMPONENTS = 'Speaker Components (e.g., woofers, tweeters)'
    POWER_AMPLIFIERS = 'Power Amplifiers'
    KARAOKE_MICROPHONES = 'Karaoke Microphones'
    KARAOKE_SPEAKERS = 'Karaoke Speakers'
    DJ_LIGHTING = 'DJ Lighting'
    DJ_SOFTWARE = 'DJ Software'
    DJ_MIXERS = 'DJ Mixers'
    DJ_TURNTABLE_CARTRIDGES = 'DJ Turntable Cartridges'
    CHOOSE = 'Choose a Category'

class City(PythonEnum):
    ABIA = 'Abia'
    ADAMAWA = 'Adamawa'
    AKWA_IBOM = 'Akwa Ibom'
    ANAMBRA = 'Anambra'
    BAUCHI = 'Bauchi'
    BAYELSA = 'Bayelsa'
    BENUE = 'Benue'
    BORNO = 'Borno'
    CROSS_RIVER = 'Cross River'
    DELTA = 'Delta'
    EBONYI = 'Ebonyi'
    EDO = 'Edo'
    EKITI = 'Ekiti'
    ENUGU = 'Enugu'
    FCT = 'FCT'
    GOMBE = 'Gombe'
    IMO = 'Imo'
    JIGAWA = 'Jigawa'
    KADUNA = 'Kaduna'
    KANO = 'Kano'
    KATSINA = 'Katsina'
    KEBBI = 'Kebbi'
    KOGI = 'Kogi'
    KWARA = 'Kwara'
    LAGOS = 'Lagos'
    NASARAWA = 'Nasarawa'
    NIGER = 'Niger'
    OGUN = 'Ogun'
    ONDO = 'Ondo'
    OSUN = 'Osun'
    OYO = 'Oyo'
    PLATEAU = 'Plateau'
    RIVERS = 'Rivers'
    SOKOTO = 'Sokoto'
    TARABA = 'Taraba'
    YOBE = 'Yobe'
    ZAMFARA = 'Zamfara'

class Rating(PythonEnum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    verification_number = db.Column(db.Integer)
    verified_user = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)
    reviews = db.relationship('Review', backref='author1', lazy=True)
    rented = db.relationship('Agreement', backref='author4', lazy=True)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(Enum(Category), default=Category.CHOOSE)
    price = db.Column(db.Float, nullable=False)
    city = db.Column(Enum(City), default=City.FCT)
    country = db.Column(db.String(10), nullable=False, default='Nigeria')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_file = db.Column(db.String(50), nullable=False, default='default.jpg')
    availability = db.Column(db.Boolean, nullable=False, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reviews = db.relationship('Review', backref='author2', lazy=True)
    rented = db.relationship('Agreement', backref='author5', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    star_rating = db.Column(Enum(Rating), default=Rating.ZERO)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"Review('{self.content}')"

class Agreement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rented_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    returned_date = db.Column(db.DateTime)
    returned = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Agreement('{self.returned}')"