import uvicorn
from src.laudos import Laudo
from src.classifier import Classifier

from fastapi import FastAPI

classifier = Classifier('/app/models/model.pkl')

app = FastAPI()

@app.get("/")
def home():
    return {'Hello': 'World'}

# async def get_prediction(doc, pipeline):
#     dict_result = {}
#     y_pred = pipeline.predict_proba([doc])[0]
#     y_pred_class = pipeline.predict([doc])[0]
#     for target, prob in zip(pipeline.classes_, y_pred):
#         dict_result[target] = prob
#     return y_pred_class, dict_result[y_pred_class]

@app.post('/predict')
async def predict_laudos(laudo: Laudo):
    data = laudo.dict()
    prediction_class, probability = await classifier.get_prediction(data['texto'])

    return{
        'prediction': prediction_class,
        'probability': probability
    }
    

if __name__ == '__main__':
    uvicorn.run('main:app')