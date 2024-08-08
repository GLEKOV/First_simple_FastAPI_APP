from fastapi import FastAPI  # из библиотеки импортируем класс

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as cats_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DataBase is cleared")
    await create_tables()
    print("DataBase is ready")
    yield
    print('Shutting down the DataBase')


app = FastAPI(lifespan=lifespan)   # Создаем экземпляр класса - приложение

app.include_router(cats_router)


