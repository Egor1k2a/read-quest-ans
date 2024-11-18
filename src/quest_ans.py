import os
import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [
    {
        'name': 'SEARCH ANSWERS',
        'description': 'API для поиска правильных ответов.',
    }
]

origin_endpoint = ['https://iomqt-vo.edu.rosminzdrav.ru', 'https://iomqt-spo.edu.rosminzdrav.ru', 'https://iomqt-nmd.edu.rosminzdrav.ru']

app = FastAPI(
    root_path="/api",
    title='API for SEARCH ANSWERS',
    description='API для поиска правильных ответов',
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
    # quest = quest.replace('a', 'а')
    # quest = quest.replace('o', 'о')
    this_folder = os.getcwd()
    beg_beg = 0
    if quest:
        quest += '\n'
        true_answers_list = []
        with open(f'{this_folder}/src/myans.txt', 'r', encoding="utf-8") as f:
            text = f.read()
        for c in range(text.count(quest)):
            begin = text.find(quest, beg_beg)
            beg_beg = begin + len(quest)
            if begin != -1:
                num_quest = text[text.rfind('\n', 0, begin):begin-2].strip()
                num_quest = num_quest.replace('.', '') if '.' in num_quest else num_quest
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
                            cleaned_i = cleaned_i[1:] if cleaned_i[0] == '~' else cleaned_i
                            cleaned_i = cleaned_i[2:].strip()
                            # cleaned_i = cleaned_i.replace('а', 'a')
                            # cleaned_i = cleaned_i.replace('о', 'o')
                            true_answers_list.append(cleaned_i)
            else:
                raise HTTPException(status_code=404, detail='Нет такого вопроса')

        if len(true_answers_list) == 0:
            quest = quest.replace('a', 'а')
            quest = quest.replace('o', 'о')
            for c in range(text.count(quest)):
                begin = text.find(quest, beg_beg)
                beg_beg = begin + len(quest)
                if begin != -1:
                    num_quest = text[text.rfind('\n', 0, begin):begin - 2].strip()
                    num_quest = num_quest.replace('.', '') if '.' in num_quest else num_quest
                    end1 = text.find('\n\n', begin + len(quest))
                    end2 = text.find(f'{int(num_quest) + 1}. ', begin + len(quest))
                    end = min(filter(lambda val: val > 0, [end1, end2]))
                    answers = text[begin + len(quest):end].strip()
                    answers_list = answers.split('\n')
                    for i in answers_list:
                        if i[0] == '~' or i[-1] == '+':
                            if i[-1] == '+':
                                cleaned_i = i[0:-1]
                                cleaned_i = cleaned_i[0:-1] if cleaned_i[-1] == ';' else cleaned_i
                                cleaned_i = cleaned_i[0:-1] if cleaned_i[-1] == '.' else cleaned_i
                                cleaned_i = cleaned_i[1:] if cleaned_i[0] == '~' else cleaned_i
                                cleaned_i = cleaned_i[2:].strip()
                                # cleaned_i = cleaned_i.replace('а', 'a')
                                # cleaned_i = cleaned_i.replace('о', 'o')
                                true_answers_list.append(cleaned_i)
                    # return true_answers_list
                else:
                    raise HTTPException(status_code=404, detail='Нет такого вопроса')

        if len(true_answers_list) == 0:
            quest = quest.replace('а', 'a')
            quest = quest.replace('о', 'o')
            for c in range(text.count(quest)):
                begin = text.find(quest, beg_beg)
                beg_beg = begin + len(quest)
                if begin != -1:
                    num_quest = text[text.rfind('\n', 0, begin):begin - 2].strip()
                    num_quest = num_quest.replace('.', '') if '.' in num_quest else num_quest
                    end1 = text.find('\n\n', begin + len(quest))
                    end2 = text.find(f'{int(num_quest) + 1}. ', begin + len(quest))
                    end = min(filter(lambda val: val > 0, [end1, end2]))
                    answers = text[begin + len(quest):end].strip()
                    answers_list = answers.split('\n')
                    for i in answers_list:
                        if i[0] == '~' or i[-1] == '+':
                            if i[-1] == '+':
                                cleaned_i = i[0:-1]
                                cleaned_i = cleaned_i[0:-1] if cleaned_i[-1] == ';' else cleaned_i
                                cleaned_i = cleaned_i[0:-1] if cleaned_i[-1] == '.' else cleaned_i
                                cleaned_i = cleaned_i[1:] if cleaned_i[0] == '~' else cleaned_i
                                cleaned_i = cleaned_i[2:].strip()
                                # cleaned_i = cleaned_i.replace('а', 'a')
                                # cleaned_i = cleaned_i.replace('о', 'o')
                                true_answers_list.append(cleaned_i)
                    # return true_answers_list
                else:
                    raise HTTPException(status_code=404, detail='Нет такого вопроса')

        new_true_answers_list = []
        for i in true_answers_list:
            new_i = i.replace('а', 'a')
            new_i = new_i.replace('о', 'o')
            new_true_answers_list.append(new_i)

            new_i = i.replace('a', 'а')
            new_i = new_i.replace('o', 'о')
            new_true_answers_list.append(new_i)
        return true_answers_list + new_true_answers_list
    else:
        raise HTTPException(status_code=404, detail='Нет такого вопроса')

