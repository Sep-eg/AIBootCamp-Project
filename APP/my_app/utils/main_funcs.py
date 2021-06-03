import joblib

def predict_life(age, predict_info):
    modelfile = 'my_app/models/model.pkl'
    model = joblib.load(modelfile)

    life = model.predict([predict_info])

    lifespan = life - age + 25
    result = str(int(lifespan))

    return result