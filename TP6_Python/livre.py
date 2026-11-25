
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True, order=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def promo(self, prix_reduit):
        if prix_reduit <= 0 or prix_reduit >= self.prix:
            raise ValueError("Prix réduit invalide.")

        return Livre(
            self.titre,
            self.auteur,
            self.annee,
            prix_reduit
        )

    @classmethod
    def from_json(cls, chaine_json):
        donnees = json.loads(chaine_json)
        return cls(**donnees)


if __name__ == "__main__":

    livre1 = Livre("1984", "George Orwell", 1949, 9.90)

    print("=== Livre original ===")
    print(livre1.to_json())

    print("\n=== Promotion ===")
    livre2 = livre1.promo(7.50)
    print(livre2.to_json())

    print("\n=== Livre original après promotion ===")
    print(livre1.prix)

    print("\n=== Chargement JSON ===")
    texte = livre1.to_json()
    livre3 = Livre.from_json(texte)
    print(livre3)

    print("\n=== Comparaison ===")
    livres = [
        Livre("Livre A", "Auteur A", 2020, 15.0),
        Livre("Livre B", "Auteur B", 2021, 8.0),
        Livre("Livre C", "Auteur C", 2019, 12.0)
    ]

    livres_tries = sorted(livres)

    for livre in livres_tries:
        print(livre.prix, "€ -", livre.titre)
