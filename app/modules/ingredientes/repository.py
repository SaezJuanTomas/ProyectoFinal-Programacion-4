from sqlmodel import Session, select

from app.core.repository import BaseRepository
from app.models import Ingrediente


class IngredienteRepository(BaseRepository[Ingrediente]):
    """
    Repository específico para Ingrediente.
    Hereda CRUD genérico de BaseRepository[Ingrediente].
    """

    def __init__(self, session: Session):
        super().__init__(session, Ingrediente)

    def get_by_nombre(self, nombre: str) -> Ingrediente | None:
        """Buscar ingrediente por nombre exacto."""
        statement = select(Ingrediente).where(Ingrediente.nombre == nombre)
        return self.session.exec(statement).first()

    def get_alergenos(self) -> list[Ingrediente]:
        """Obtener todos los alérgenos."""
        statement = select(Ingrediente).where(Ingrediente.es_alergeno == True)
        return self.session.exec(statement).all()
