import unittest
from task_manager import Task, TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()
        self.task1 = Task("Zadanie 1", 3)
        self.task2 = Task("Zadanie 2", 5)
        self.task3 = Task("Zadanie 3", 1)
        self.task_manager.add_task(self.task1)
        self.task_manager.add_task(self.task2)
        self.task_manager.add_task(self.task3)

    def test_add_task(self):
        self.assertEqual(self.task_manager.get_task_count(), 3)
        self.task_manager.add_task(Task("Zadanie 4", 2))
        self.assertEqual(self.task_manager.get_task_count(), 4)

    def test_remove_task(self):
        self.task_manager.remove_task("Zadanie 2")
        self.assertEqual(self.task_manager.get_task_count(), 2)

    def test_get_highest_priority_task(self):
        self.assertEqual(self.task_manager.get_highest_priority_task(), self.task2)
        self.task_manager.remove_task("Zadanie 2")
        self.assertEqual(self.task_manager.get_highest_priority_task(), self.task1)
        self.task_manager.remove_task("Zadanie 1")
        self.assertEqual(self.task_manager.get_highest_priority_task(), self.task3)
        self.task_manager.remove_task("Zadanie 3")
        self.assertIsNone(self.task_manager.get_highest_priority_task())

    def test_get_task_count(self):
        self.assertEqual(self.task_manager.get_task_count(), 3)
        self.task_manager.remove_task("Zadanie 2")
        self.assertEqual(self.task_manager.get_task_count(), 2)
        self.task_manager.add_task(Task("Zadanie 4", 2))
        self.assertEqual(self.task_manager.get_task_count(), 3)

    def test_add_duplicate_task(self):
        self.assertEqual(self.task_manager.get_task_count(), 3)
        self.task_manager.add_task(Task("Zadanie 1", 2))
        self.assertEqual(self.task_manager.get_task_count(), 3)

    def test_remove_nonexistent_task(self):
        self.assertEqual(self.task_manager.get_task_count(), 3)
        self.task_manager.remove_task("Nieistniejące Zadanie")
        self.assertEqual(self.task_manager.get_task_count(), 3)

    def test_get_highest_priority_task_empty(self):
        self.task_manager.remove_task("Zadanie 1")
        self.task_manager.remove_task("Zadanie 2")
        self.task_manager.remove_task("Zadanie 3")
        self.assertIsNone(self.task_manager.get_highest_priority_task())

    def test_add_task_priority_0(self):
        self.assertEqual(self.task_manager.get_task_count(), 3)
        self.task_manager.add_task(Task("Zadanie 4", 0))
        self.assertEqual(self.task_manager.get_task_count(), 4)

    def test_add_task_negative_priority(self):
        self.assertEqual(self.task_manager.get_task_count(), 3)
        self.task_manager.add_task(Task("Zadanie 4", -1))
        self.assertEqual(self.task_manager.get_task_count(), 4)

    def test_remove_task_not_in_list(self):
        self.assertEqual(self.task_manager.get_task_count(), 3)
        self.task_manager.remove_task("Zadanie 4")
        self.assertEqual(self.task_manager.get_task_count(), 3)

if __name__ == '__main__':
    unittest.main()
