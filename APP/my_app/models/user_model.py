from my_app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), nullable=False)
    # age = db.Column(db.Integer, nullable=False)
    # gender = db.Column(db.Integer, nullable=False)
    # job = db.Column(db.Integer, nullable=False)
    # marital = db.Column(db.Integer, nullable=False)
    infos = db.relationship('Info', backref='user', cascade='all, delete')

    def __repr__(self):
        return f"User {self.id}"

class Info(db.Model):
    __tablename__ = 'info'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    job = db.Column(db.Integer, nullable=False)
    marital = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Info {self.id}"

def add_user(raw_user):
    new_user = User(
        id = int(raw_user['id']),
        nickname = raw_user['nickname'],
    )
        
    new_info = Info(
        id = len(Info.query.all()),
        age = int(raw_user['age']),
        gender = int(raw_user['gender']),
        job = int(raw_user['job']),
        marital = int(raw_user['marital']),
        user_id = int(raw_user['id'])
    )

    if User.query.filter(User.id == new_user.id).first() == None:
        db.session.add(new_user)
        db.session.add(new_info)
        db.session.commit()
        return 1
    else:
        return "이미 중복된 ID가 있습니다."

def get_users(raw_user):
    if User.query.filter(User.id == raw_user['id']).first() == None:
        return "해당 ID가 없습니다.", 0
    if User.query.filter(User.nickname == raw_user['nickname']).first() == None:
        return 0, "해당 별명이 없습니다."
        
    user = [
            int(Info.query.filter(Info.user_id==raw_user['id']).first().gender),
            int(Info.query.filter(Info.user_id==raw_user['id']).first().job),
            int(Info.query.filter(Info.user_id==raw_user['id']).first().marital)
    ]
    return Info.query.filter(Info.user_id==raw_user['id']).first().age, user

def delete_user(raw_user):
    if User.query.filter(User.id == raw_user['id']).first() == None:
        return 2
    if User.query.filter(User.nickname == raw_user['nickname']).first() == None:
        return 3
    user = User.query.filter((User.nickname == raw_user['nickname'] and
                             User.id == raw_user['id'])).first()
    db.session.delete(user)
    db.session.commit()
    return 1