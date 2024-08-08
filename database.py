from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker    # импортируем создание асинк движка
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column





engine = create_async_engine(
    "sqlite+aiosqlite:///cats.db"
)
# URL или адрес базы занных состоит из названия базы данных и драйвера через +
# - потом двоеточие и три слеша и название файла

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):    # Наш класс модели таблиц который наследуем от класса из Алхимии
    pass            # тут можно делать конфигурацию, но сейчас без нее


class CatOrm(Model):            # Создаем таблицу - суффикс Orm - которая должна наследоваться от класса таблиц
    __tablename__ = "cats"

    id: Mapped[int] = mapped_column(primary_key=True)  # тоже импортируем
    name: Mapped[str]
    description: Mapped[Optional[str]]
    # это мы описали таблицу
# а теперь создаем функцией из документации к алхимии


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
