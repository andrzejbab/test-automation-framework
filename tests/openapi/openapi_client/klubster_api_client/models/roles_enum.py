from enum import Enum


class RolesEnum(str, Enum):
    ADMINISTRATOR = "administrator"
    GOSC = "gosc"
    PREZES = "prezes"
    RECEPCJA = "recepcja"
    REKREACJA = "rekreacja"
    RODZIC = "rodzic"
    SKARBNIK = "skarbnik"
    TRENER = "trener"
    ZAWODNIK = "zawodnik"

    def __str__(self) -> str:
        return str(self.value)
