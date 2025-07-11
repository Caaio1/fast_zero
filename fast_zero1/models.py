from datetime import datetime
from sqlalchemy.orm import Mapped, registry, mapped_column
from sqlalchemy import func

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init = False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init = False, default=func.now()) #mapear o dia e criação do usuário


@table_registry.mapped_as_dataclass
class update_user:
    __tablename__ = 'update_users'

    id: Mapped[int] = mapped_column(init = False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init = False, default=func.now()) #mapear o dia e criação do usuário
    uptaded_at: Mapped[datetime] = mapped_column(init = False, default=func.now(), onupdate=func.now()) #mapear o dia e atualização do usuário