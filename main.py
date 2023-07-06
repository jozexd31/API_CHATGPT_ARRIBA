from fastapi import FastAPI

from OpenAI.OpenAI.OpenAI_Test import Document, inference

app = FastAPI()


@app.post("/inference", status_code=200)
def user_inference(doc: Document):
    response = inference(doc.prompt)
    print("Respuesta del prompt:", response)  # Imprime la respuesta completa
    return {
        'inference': response
    }