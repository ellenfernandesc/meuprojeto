import unittest
from src.main import StudyManager

class TestStudyManager(unittest.TestCase):
    def setUp(self):
        self.manager = StudyManager()

    def test_add_task_success(self): # Caminho feliz [cite: 207]
        result = self.manager.add_task("Matemática", 60)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertIn("adicionada", result)

    def test_add_task_invalid_time(self): # Entrada inválida [cite: 208]
        result = self.manager.add_task("Física", -10)
        self.assertIn("Erro", result)

    def test_add_task_empty_name(self): # Caso limite [cite: 209]
        result = self.manager.add_task("", 30)
        self.assertIn("Erro", result)

if __name__ == "__main__":
    unittest.main()
