
from dataclasses import dataclass, field, asdict
import json


@dataclass(frozen=True, slots=True, order=True)
class Film:
    titre: str = field(compare=False)
    realisateur: str = field(compare=False)
    annee: int = field(compare=False)
    note: float

    def __post_init__(self):
        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Le titre est obligatoire.")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Le réalisateur est obligatoire.")

        if not isinstance(self.annee, int) or isinstance(self.annee, bool):
            raise TypeError("L'année doit être un entier.")

        if not isinstance(self.note, (int, float)) or isinstance(self.note, bool):
            raise TypeError("La note doit être numérique.")

        if not 0 <= self.note <= 10:
            raise ValueError("La note doit être entre 0 et 10.")

        object.__setattr__(self, "note", float(self.note))

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    @classmethod
    def from_json(cls, chaine):
        donnees = json.loads(chaine)
        return cls(**donnees)


def favoris_to_json(favoris):
    donnees = [asdict(film) for film in favoris]
    return json.dumps(donnees, ensure_ascii=False)


def favoris_from_json(chaine):
    donnees = json.loads(chaine)
    return [Film(**film) for film in donnees]


if __name__ == "__main__":

    film1 = Film("Titanic", "James Cameron", 1997, 9.5)
    film2 = Film("Inception", "Christopher Nolan", 2010, 8.8)
    film3 = Film("Interstellar", "Christopher Nolan", 2014, 9.2)

    print("=== Film en JSON ===")
    print(film1.to_json())

    print("\n=== Film classique ===")
    print(film1.est_classique())

    print("\n=== Chargement JSON ===")
    film4 = Film.from_json(film1.to_json())
    print(film4)

    print("\n=== Tri par note croissante ===")
    films = [film1, film2, film3]

    for film in sorted(films):
        print(film.note, "-", film.titre)

    print("\n=== Liste des favoris ===")
    texte = favoris_to_json(films)
    print(texte)

    nouveaux_favoris = favoris_from_json(texte)
    print("Nombre de favoris :", len(nouveaux_favoris))
