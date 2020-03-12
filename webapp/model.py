from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=True)
    tracks = db.relationship('Tracks', backref=db.backref('artists', lazy='dynamic'))


def __repr__(self):
        return f'<Artist: {self.name}, Date of Birth: {self.date_of_birth}>'


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='CASCADE'), index=True, nullable=False)
    artist = db.relationship('Artist', backref=db.backref('tracks', lazy='dynamic'))

    note_duration = db.Column(db.String, nullable=False)
    speed = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Track: {self.name}, duration: {self.note_duration}, speed: {self.speed}>'


class Line(db.Model):
    __tablename__ = 'lines'
    id = db.Column(db.Integer, primary_key=True)

    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id', ondelete='CASCADE'), index=True, nullable=False)
    bars = db.relationship('Bars', backref=db.backref('bars', lazy='dynamic'))

    sequence = db.Column(db.Integer, nullable=False)
    position_1 = db.Column(db.Integer, db.ForeignKey('bars.id', ondelete='CASCADE'), index=True, nullable=False)
    position_2 = db.Column(db.Integer, db.ForeignKey('bars.id', ondelete='CASCADE'), index=True, nullable=False)
    position_3 = db.Column(db.Integer, db.ForeignKey('bars.id', ondelete='CASCADE'), index=True, nullable=False)
    position_4 = db.Column(db.Integer, db.ForeignKey('bars.id', ondelete='CASCADE'), index=True, nullable=False)
    position_5 = db.Column(db.Integer, db.ForeignKey('bars.id', ondelete='CASCADE'), index=True, nullable=False)
    position_6 = db.Column(db.Integer, db.ForeignKey('bars.id', ondelete='CASCADE'), index=True, nullable=False)
    position_7 = db.Column(db.Integer, db.ForeignKey('bars.id', ondelete='CASCADE'), index=True, nullable=False)
    position_8 = db.Column(db.Integer, db.ForeignKey('bars.id', ondelete='CASCADE'), index=True, nullable=False)
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

    def __repr__(self):
        return f'Line sequence: {self.sequence}'
    #  Нужно ли тут перечислять все элементы?


class Bar(db.Model):
    __tablename__ = 'bars'
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    empty = db.Column(db.Boolean, nullable=False)
    half = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'Bar number: {self.number}, empty={self.empty}, half={self.half}, notes: {self.notes}'
