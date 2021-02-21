from unittest import TestCase
import training_functions as tf


class TrainingFunctionTests(TestCase):
    def test_calculate_ninety(self):
        ninety = tf.calculate_ninety(100)
        self.assertEqual(ninety, 90.0)
