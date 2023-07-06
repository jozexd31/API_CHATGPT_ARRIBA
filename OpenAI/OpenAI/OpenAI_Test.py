import openai
from pydantic import BaseModel

openai.organization = 'org-DYRwCOZ92Bsf4lIsYceu2SVQ'
openai.api_key = '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'


class Document(BaseModel):
    prompt: str = ''




def inference(prompt: str) -> str:
    print('[----------INGRESO AL PROCESO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres el mayor sistema de conocimiento conocido responde cualquier pregunta o duda que el usuario te pida responder.
        E.G
        Claro, la respuesta a tu pregunta esta basada en...
        """},
            {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    return content