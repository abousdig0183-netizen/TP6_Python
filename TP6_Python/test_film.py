
import unittest
from film import Film


class TestFilm(unittest.TestCase):

    def setUp(self):
        self.film = Film("Titanic", "James Cameron", 1997, 9.5)

    def test_creation(self):
        self.assertEqual(self.film.titre, "Titanic")
        self.assertEqual(self.film.note, 9.5)

    def test_film_classique(self):
        self.assertTrue(self.film.est_classique())

    def test_film_non_classique(self):
        film = Film("Inception", "Christopher Nolan", 2010, 8.8)
        self.assertFalse(film.est_classique())

    def test_immutabilite(self):
        with self.assertRaises(AttributeError):
            self.film.note = 8.0

    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            Film("Film", "Auteur", 2020, 11)

    def test_note_negative(self):
        with self.assertRaises(ValueError):
            Film("Film", "Auteur", 2020, -1)

    def test_note_type_invalide(self):
        with self.assertRaises(TypeError):
            Film("Film", "Auteur", 2020, "excellent")

    def test_titre_vide(self):
        with self.assertRaises(ValueError):
            Film("", "Auteur", 2020, 8.0)

    def test_annee_invalide(self):
        with self.assertRaises(TypeError):
            Film("Film", "Auteur", "2020", 8.0)

    def test_from_json(self):
        texte = self.film.to_json()
        nouveau_film = Film.from_json(texte)
        self.assertEqual(nouveau_film, self.film)

    def test_tri_par_note(self):
        film1 = Film("A", "Auteur A", 2020, 9.0)
        film2 = Film("B", "Auteur B", 2021, 7.0)

        resultats = sorted([film1, film2])

        self.assertEqual(resultats[0].note, 7.0)
        self.assertEqual(resultats[1].note, 9.0)


if __name__ == "__main__":
    unittest.main()
