from typing import Optional
from pydantic import BaseModel, ConfigDict


class SCatAdd(BaseModel):    # создаем класс наследованием от Basemodel - прификс S - схема Pydantic
    name: str
    description: Optional[str] = None  #  Поле необязательное с дефолтным значением в новых версиях можно str | None - а тут надо импортировать optional


class SCat(SCatAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)
    # При преобразовании SQLAlchemy модели в схему  - обязательно добавить конфигурацию from_attributes=True (тк это не словарь а экземпляр класса) - распарсь объект не только как словарик, а еще как экземпляр класса, и из его атрибутов достань все свойства
