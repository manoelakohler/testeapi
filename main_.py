
from inference import preprocessing_csv
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, Response, StreamingResponse
import pandas as pd
import numpy as np
import joblib
import io
app = FastAPI()


@app.post("/inference_complete/")
async def inference_complete(dataset: UploadFile = File(...), model: str = 'mlp'):
    
    if model:

        df = pd.read_csv(dataset.file)
        print(df.head())
        X = np.array(df.iloc[:, :])

        # TODO o modelo sera selecionado a partir da variavel model
        # Acessando o bano de dados. Provisorio/Teste
        filename = 'MLP16/model_mlp_16.sav'
        loaded_model = joblib.load(filename)
        result = loaded_model.predict(X)
        df_inf = pd.DataFrame({'Result': result})

    stream = io.StringIO()
    df_inf.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]),
                                 media_type="text/csv"
                                 )
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    
    return response


@app.get("/inference_coord/")
async def inference_coord(coord_E: float = 390000.01, model: str = 'mlp', coord_N: float = 7390000.01):

    if model:
        print(coord_E)
        print(coord_N)
        print(model)

        # TODO Load Model
        # Load Dataset ligado ao modelo

        # filename='MLP16/model_mlp_16.sav'
        # loaded_model = joblib.load(filename)
        # result=loaded_model.predict(X)

    return {"Coord_E": coord_E, "coord_N": coord_N, "Co2": 50}
