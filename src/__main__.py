import uvicorn


uvicorn.run(
    'scr.quest_ans:app',
    host="0.0.0.0",
    port=8000,
    reload=True
)
