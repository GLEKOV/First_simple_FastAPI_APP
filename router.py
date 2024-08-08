from typing import Annotated

from fastapi import APIRouter, Depends

from repository import CatRepository
from shemes import SCatAdd

# Для того чтобы выносить набор ручек в отдельный файл
# и потом перемещать в файлик main одной строчкой кода


router = APIRouter(
    prefix="/cats",
    tags=['Котики'],
)
# Херня с префиксом не сработала приложение ругалось
# убрали "/cats" из аргументов метода пост и ниже метода гет через строчку выше
@router.post("/cats")
async def add_cat(
        cat: Annotated[SCatAdd, Depends()],
 ):                   # импортируем и Annotated и Depends - ДАЕТ КРАСИВЫЕ ПОЛЯ ДЛЯ ВВОДА
    cat_id = await CatRepository.add_one(cat)  # добавляем объект cat в репозиторий
    return {"ok": True, "cat_id": cat_id}


@router.get("/cats")
async def get_cats():
    cats = await CatRepository.find_all()
    return {"cats": cats}    # возвращаем Pydantic кото`рый FastAPI конвертирует в Json(чтобы хорошо передавать по сети)
