import unittest
from stacks import Stack
from custom_exceptions import EmptyStackException, FullStackException

class StackTestCase(unittest.TestCase):
    stack = Stack(5)

    def setUp(self):
        self.stack = Stack(5)
        for x in range(1,6):
            self.stack.push('item_{}'.format(x))

    def test_can_push_to_stack(self):
        stack = Stack(5)

        stack.push('item_1')
        self.assertEquals(1, len(stack))

        stack.push('item_2')
        self.assertEquals(2, len(stack))

    def test_can_get_stacks(self):
        stack = self.stack
        expected_initialization = [
                'item_1', 'item_2', 'item_3',
                'item_4', 'item_5'
        ]
        self.assertEquals(expected_initialization, stack.getitems())

    def test_can_pop_stacks(self):
        stack = self.stack
        expected_initialization = [
                'item_1', 'item_2', 'item_3',
                'item_4', 'item_5'
        ]

        for x in reversed(expected_initialization):
            self.assertEquals(x, stack.pop())

        with self.assertRaises(EmptyStackException):
            stack.pop()

    def test_set_stack_limit(self):
        stack = self.stack
        self.assertEquals(5, len(stack.getitems()))
        with self.assertRaises(FullStackException):
            stack.push('item_6')

if __name__ == '__main__':
    unittest.main()
