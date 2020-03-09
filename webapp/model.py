from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Artist(db.Model):
    __tablename__ = 'artists'  #  Надо ли прописывать для каждрй таблицы?
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f'<Artist: {self.name}, Date of Birth: {self.date_of_birth}>'

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    #  Пока до конца не понял, правильно ли сделал Foreign Key?
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist = db.relationship('Artist', backref=db.backref('artist', lazy='dynamic'))

    note_duration = db.Column(db.String, nullable=False)
    speed = db.Column(db.Integer, nullable=False)

    def __init__(self, name, artist, note_duration, speed):
        self.name = name
        self.artist = artist  #  Тут верно? Или надо указывать artist_id?
        self.note_duration = note_duration
        self. speed = speed

    def __repr__(self):
        return f'<Track: {self.name}, duration: {self.note_duration}, speed: {self.speed}>'

class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    #  Или подойдет вот такая записть Foreign Key
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)

    sequence = db.Column(db.Integer, nullable=False)

    # Тут не понятно пока как записывать Foreign Key.
    position_1 =
    position_2 =
    position_3 =
    position_4 =
    position_5 =
    position_6 =
    position_7 =
    position_8 =
    accent_1 = db.Column(db.Boolean, nullable=False)
    accent_2 = db.Column(db.Boolean, nullable=False)
    accent_3 = db.Column(db.Boolean, nullable=False)
    accent_4 = db.Column(db.Boolean, nullable=False)
    accent_5 = db.Column(db.Boolean, nullable=False)
    accent_6 = db.Column(db.Boolean, nullable=False)
    accent_7 = db.Column(db.Boolean, nullable=False)
    accent_8 = db.Column(db.Boolean, nullable=False)
    intro = db.Column(db.Boolean, nullable=False)
    couplet = db.Column(db.Boolean, nullable=False)
    chorus = db.Column(db.Boolean, nullable=False)
    pre_chorus = db.Column(db.Boolean, nullable=False)
    bridge = db.Column(db.Boolean, nullable=False)
    solo = db.Column(db.Boolean, nullable=False)
    coda = db.Column(db.Boolean, nullable=False)

    def __init__(self, sequence, accent_1=False, accent_2=False, accent_3=False, accent_4=False, accent_5=False,
                 accent_6=False, accent_7=False, accent_8=False, intro=False, couplet=False, chorus=False,
                 pre_chorus=False, bridge=False, solo=False, coda=False):
        self.sequence = sequence
        self.accent_1 = accent_1
        self.accent_2 = accent_2
        self.accent_3 = accent_3
        self.accent_4 = accent_4
        self.accent_5 = accent_5
        self.accent_6 = accent_6
        self.accent_7 = accent_7
        self.accent_8 = accent_8
        self.intro = intro
        self.couplet = couplet
        self.chorus = chorus
        self.pre_chorus = pre_chorus
        self.bridge = bridge
        self.solo = solo
        self.coda = coda

    def __repr__(self):
        return f'Line sequence: {self.sequence}'
    #  Нужно ли тут перечислять все элементы?

class Bar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    empty = db.Column(db.Boolean, nullable=False)
    half = db.Column(db.Boolean, nullable=False)

    def __init__(self, notes, number, empty=False, half=False):
        self.notes = notes
        self.number = number
        self.empty = empty
        self.half = half

    def __repr__(self):
        return f'Bar number: {self.number}, empty={self.empty}, half={self.half}, notes: {self.notes}'
