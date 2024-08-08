from typing import Optional
from pydantic import BaseModel

class SCatAdd(BaseModel):    # создаем класс наследованием от Basemodel - прификс S - схема Pydantic
    name: str
    description: Optional[str] = None  #  Поле необязательное с дефолтным значением в новых версиях можно str | None - а тут надо импортировать optional


class SCat(SCatAdd):
    id: int