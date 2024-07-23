import os
import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [
    {
        'name': 'RESEARCH UPLOADING',
        'description': 'Выгрузка результатов исследований.',
    }
]

origin_endpoint = ['https://iomqt-vo.edu.rosminzdrav.ru']

app = FastAPI(
    root_path="/api",
    title='API for RESEARCH UPLOADING',
    description='API для выгрузки результатов исследований',
    version='0.1.0',
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin_endpoint,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/test')
async def test(
        quest: str = None
):
    this_folder = os.getcwd()
    beg_beg = 0
    if quest:
        true_answers_list = []
        with open(f'{this_folder}/myans.txt', 'r', encoding="utf-8") as f:
            text = f.read()
        for c in range(text.count(quest)):
            begin = text.find(quest, beg_beg)
            beg_beg = begin + len(quest)
            if begin != -1:
                num_quest = text[text.rfind('\n', 0, begin):begin-2].strip()
                end1 = text.find('\n\n', begin+len(quest))
                end2 = text.find(f'{int(num_quest) + 1}. ', begin+len(quest))
                end = min(filter(lambda val: val > 0, [end1, end2]))
                answers = text[begin+len(quest):end].strip()
                answers_list = answers.split('\n')
                for i in answers_list:
                    if i[0] == '~' or i[-1] == '+':
                        if i[-1] == '+':
                            cleaned_i = i[0:-1]
                            cleaned_i = cleaned_i[0:-1] if cleaned_i[-1] == ';' else cleaned_i
                            cleaned_i = cleaned_i[0:-1] if cleaned_i[-1] == '.' else cleaned_i
                            cleaned_i = cleaned_i[3:].strip()
                            true_answers_list.append(cleaned_i)
            else:
                raise HTTPException(status_code=404, detail='Нет такого вопроса')
        return true_answers_list
    else:
        raise HTTPException(status_code=404, detail='Нет такого вопроса')


# if __name__ == "__main__":
#     uvicorn.run(
#         'quest_ans:app',
#         host="0.0.0.0",
#         port=8000,
#         reload=True
#     )
