from sqlalchemy import select

from database import new_session, CatOrm
from shemes import SCatAdd


class CatRepository:
    @classmethod
    async def add_one(cls, data: SCatAdd) -> int:
        async with new_session() as session:
            cat_dict = data.model_dump()         #превращает в словарик

            cat = CatOrm(**cat_dict)   # cat - Это объект СatOrm  - новая строчка в таблице,
                                        # у которой есть поля  - ID - задает сама база, а поля name И description
                                        # мы не будем задавать явно, а передаем раскрытый словарик и поля передадутся
                                        # как ключевые аргументы (kwargs)
            # чтобы добавить в БД - есть объект сессии session - который работает с транзакцией

            session.add(cat)   # добавляем объект cat в сессию - синхронная операция, обращения в базу пока нет
            await session.flush()    # не завершая транзакцию отправит изменения в базу и получит ID, который база присвоила нашей записи cat и только потом commit - таким образом поле ID в cat будет зафиксировано и можно будет вернуть cat.id
            await session.commit()   # теперь сессия все изменения которые добавили череез .add отправит в БД
            return cat.id



    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(CatOrm)    # импортируем из sqlalchemy!!!
            result = await session.execute(query)  # await - Обратись к БД - через session и исполни запрос query
            cat_models = result.scalars().all()
            return cat_models
