from enum import Enum


class PermissionsEnum(str, Enum):
    AKTUALNOSCI_DODAWANIE_WATKU = "aktualnosci_dodawanie_watku"
    AKTUALNOSCI_EDYCJA_WATKU = "aktualnosci_edycja_watku"
    AKTUALNOSCI_KOMENTOWANIE = "aktualnosci_komentowanie"
    KALENDARZ_KLUBOWY_OGLADANIE = "kalendarz_klubowy_ogladanie"
    KALENDARZ_KLUBOWY_ZARZADZANIE = "kalendarz_klubowy_zarzadzanie"
    KALENDARZ_ZAJEC_MENU = "kalendarz_zajec_menu"
    KALENDARZ_ZAJEC_ODCZYT = "kalendarz_zajec_odczyt"
    KOMUNIKACJA = "komunikacja"
    PLATNOSCI_ZAJEC_EDYCJA = "platnosci_zajec_edycja"
    PLATNOSCI_ZAJEC_POKAZ = "platnosci_zajec_pokaz"
    REZERWACJE = "rezerwacje"
    STREFA_RODZICA_ODCZYT = "strefa_rodzica_odczyt"
    STREFA_RODZICA_POKAZ_MENU = "strefa_rodzica_pokaz_menu"
    STREFA_RODZICA_ZAPIS = "strefa_rodzica_zapis"
    STREFA_TRENERA_MENU = "strefa_trenera_menu"
    STREFA_TRENERA_ODCZYT = "strefa_trenera_odczyt"
    STREFA_TRENERA_ZAPIS = "strefa_trenera_zapis"
    ZARZADZANIE_KLUBEM = "zarzadzanie_klubem"
    ZARZADZANIE_REZERWACJAMI = "zarzadzanie_rezerwacjami"

    def __str__(self) -> str:
        return str(self.value)
