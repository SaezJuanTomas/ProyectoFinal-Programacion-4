from decimal import Decimal

from sqlmodel import Session, select

from app.core.repository import BaseRepository
from app.models import Producto


class ProductoRepository(BaseRepository[Producto]):
    """
    Repository específico para Producto.
    Hereda CRUD genérico de BaseRepository[Producto].
    Incluye queries personalizadas para filtrados comunes.
    """

    def __init__(self, session: Session):
        super().__init__(session, Producto)

    def get_by_nombre(self, nombre: str) -> Producto | None:
        """Buscar producto por nombre exacto."""
        statement = select(Producto).where(Producto.nombre == nombre)
        return self.session.exec(statement).first()

    def get_disponibles(self, offset: int = 0, limit: int = 100) -> list[Producto]:
        """Obtener todos los productos disponibles."""
        statement = (
            select(Producto)
            .where(Producto.disponible == True)
            .offset(offset)
            .limit(limit)
        )
        return self.session.exec(statement).all()

    def get_by_precio_range(
        self, min_precio: Decimal, max_precio: Decimal
    ) -> list[Producto]:
        """Obtener productos dentro de un rango de precio."""
        statement = select(Producto).where(
            Producto.precio_base >= min_precio, Producto.precio_base <= max_precio
        )
        return self.session.exec(statement).all()
