import os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from main import TaskManager, TaskStorage


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.tmp.close()
        os.remove(self.tmp.name)
        self.m = TaskManager(TaskStorage(self.tmp.name))

    def tearDown(self):
        if os.path.exists(self.tmp.name):
            os.remove(self.tmp.name)

    def test_add(self):
        t = self.m.add("A")
        self.assertEqual(t.id, 1)
        self.assertEqual(len(self.m.list()), 1)

    def test_done(self):
        self.m.add("A")
        self.assertTrue(self.m.done(1))
        self.assertTrue(self.m.list()[0].done)

    def test_delete(self):
        self.m.add("A")
        self.assertTrue(self.m.delete(1))
        self.assertFalse(self.m.delete(1))


if __name__ == "__main__":
    unittest.main()
