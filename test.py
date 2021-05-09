import unittest
from unittest import TestCase

from flatonacci import flatonacci


class FlatonacciTest(TestCase):

    def test_flatonacci_returns_empty_list_when_n_is_zero(self):
        signature = [1, 1, 1]
        n = 0
        result = flatonacci(signature=signature, n=n)
        self.assertListEqual(
            list1=list(),
            list2=result,
        )

    def test_flatonacci_returns_correct_list_when_n_is_8(self):
        signature = [1, 1, 1]
        n = 8
        result = flatonacci(signature=signature, n=n)
        self.assertListEqual(
            list1=[1, 1, 1, 3, 5, 9, 17, 31],
            list2=result,
        )

    def test_flatonacci_returns_correct_list_when_n_is_9(self):
        signature = [0, 0, 1]
        n = 9
        result = flatonacci(signature=signature, n=n)
        self.assertListEqual(
            list1=[0, 0, 1, 1, 2, 4, 7, 13, 24],
            list2=result,
        )


if __name__ == '__main__':
    unittest.main()
