from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    date_of_birth = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Artist: {self.name}, Date of Birth: {self.date_of_birth}>'


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id', ondelete='CASCADE'), index=True, nullable=False)
    artist = db.relationship('Artist', backref=db.backref('tracks', lazy='dynamic'))

    note_duration = db.Column(db.String, nullable=True)
    speed = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Track_id: {self.id},Track: {self.name}, duration: {self.note_duration}, speed: {self.speed}>'


class Line(db.Model):
    __tablename__ = 'lines'
    id = db.Column(db.Integer, primary_key=True)

    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id', ondelete='CASCADE'), index=True, nullable=False)

    sequence = db.Column(db.Integer, nullable=False)
    position_1 = db.Column(db.Integer, db.ForeignKey('bars.id'), index=True, nullable=False)
    position_2 = db.Column(db.Integer, db.ForeignKey('bars.id'), index=True, nullable=True)
    position_3 = db.Column(db.Integer, db.ForeignKey('bars.id'), index=True, nullable=True)
    position_4 = db.Column(db.Integer, db.ForeignKey('bars.id'), index=True, nullable=True)
    position_5 = db.Column(db.Integer, db.ForeignKey('bars.id'), index=True, nullable=True)
    position_6 = db.Column(db.Integer, db.ForeignKey('bars.id'), index=True, nullable=True)
    position_7 = db.Column(db.Integer, db.ForeignKey('bars.id'), index=True, nullable=True)
    position_8 = db.Column(db.Integer, db.ForeignKey('bars.id'), index=True, nullable=True)
    accent_1 = db.Column(db.Boolean, nullable=True)
    accent_2 = db.Column(db.Boolean, nullable=True)
    accent_3 = db.Column(db.Boolean, nullable=True)
    accent_4 = db.Column(db.Boolean, nullable=True)
    accent_5 = db.Column(db.Boolean, nullable=True)
    accent_6 = db.Column(db.Boolean, nullable=True)
    accent_7 = db.Column(db.Boolean, nullable=True)
    accent_8 = db.Column(db.Boolean, nullable=True)
    intro = db.Column(db.Boolean, nullable=True)
    couplet = db.Column(db.Boolean, nullable=True)
    chorus = db.Column(db.Boolean, nullable=True)
    pre_chorus = db.Column(db.Boolean, nullable=True)
    bridge = db.Column(db.Boolean, nullable=True)
    solo = db.Column(db.Boolean, nullable=True)
    coda = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f'Line: {self.id}, sequence: {self.sequence}'


class Bar(db.Model):
    __tablename__ = 'bars'
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    empty = db.Column(db.Boolean, nullable=True)
    half = db.Column(db.Boolean, nullable=True)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id', ondelete='CASCADE'), index=True, nullable=True)
    track = db.relationship('Track', backref=db.backref('bars', lazy='dynamic'))

    def __repr__(self):
        return f'Bar {self.id}, number: {self.number}, empty={self.empty}, half={self.half}, notes: {self.notes}'
