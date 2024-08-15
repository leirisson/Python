from fastapi import FastAPI
from configs.configs import settings
from api.V1.api import api_router

app = FastAPI()
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":

    import uvicorn
    uvicorn.run(app, host="0.0.0.", port=8000, log_level='info', reload=True, debug=True)

