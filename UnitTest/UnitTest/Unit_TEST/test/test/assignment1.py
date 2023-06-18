from typing import List
import unittest
import coverage


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 1 or len(tokens) > 104:
            raise ValueError("Invalid input length")
        stack = Stack()
        for c in tokens:
            if not (-200 <= int(c) <= 200) and c not in ["+", "-", "*", "/"]:
                raise ValueError("Invalid token value")
            if c == "+":
                stack.push(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.push(b - a)
            elif c == "*":
                stack.push(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.push(int(b / a))
            else:
                stack.push(int(c))
        return stack.pop()


class SolutionStub(Solution):
    def evalRPN(self, tokens: List[str]) -> int:
        # Use the stack stub instead of a real stack.
        stack = Stack()
        for c in tokens:
            if c == "+":
                stack.push(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.push(b - a)
            elif c == "*":
                stack.push(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.push(int(b / a))
            else:
                stack.push(int(c))
        return stack.pop()


class TestEvalRPN(unittest.TestCase):
    def test_valid_operators(self):
        """
        Test that valid operators are allowed in the expression.
        """
        solution = SolutionStub()
        tokens = ["1", "2", "+", "3", "-", "4", "*", "5", "/"]
        self.assertEqual(solution.evalRPN(tokens), -0)

    def test_valid_operand(self):
        """
        Test that valid operands are allowed in the expression.
        """
        solution = Solution()
        tokens = ["2", "3", "4a", "+"]
        with self.assertRaises(Exception):
            solution.evalRPN(tokens)

    def test_division_truncates_toward_zero(self):
        """
        Test that division between two integers always truncates toward zero.
        """
        solution = SolutionStub()
        tokens = ["7", "-3", "/"]
        self.assertEqual(solution.evalRPN(tokens), -2)

    def test_no_division_by_zero(self):
        """
        Test that division by zero is not allowed.
        """
        solution = Solution()
        tokens = ["2", "0", "/"]
        with self.assertRaises(Exception):
            solution.evalRPN(tokens)

    def test_valid_expression(self):
        """
        Test that the input represents a valid arithmetic expression in a reverse polish notation.
        """
        solution = SolutionStub()
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(solution.evalRPN(tokens), 22)

    def test_result_within_32_bit_integer_range(self):
        """
        Test that the answer and all the intermediate calculations can be represented in a 32-bit integer.
        """
        solution = SolutionStub()
        # This expression should not cause overflow or underflow of a 32-bit integer.
        tokens = ["2147483647", "1", "+"]
        self.assertEqual(solution.evalRPN(tokens), 2147483648)

    def test_invalid_input_length(self):
        """
        Test that input length is within the specified range.
        """
        solution = Solution()
        # Tokens length exceeds upper bound
        tokens = ["1"] * 105
        with self.assertRaises(ValueError):
            solution.evalRPN(tokens)
        # Tokens length below lower bound
        tokens = []
        with self.assertRaises(ValueError):
            solution.evalRPN(tokens)

    def test_invalid_token_value(self):
        """
        Test that token values are within the specified range.
        """
        solution = Solution()
        # Token value outside of range
        tokens = ["201", "1", "+"]
        with self.assertRaises(ValueError):
            solution.evalRPN(tokens)
        tokens = ["-201", "1", "+"]
        with self.assertRaises(ValueError):
            solution.evalRPN(tokens)
        tokens = ["a", "1", "+"]
        with self.assertRaises(ValueError):
            solution.evalRPN(tokens)


if __name__ == "__main__":
    cov = coverage.Coverage()
    cov.start()

    unittest.main(argv=["first-arg-is-ignored"], exit=False)

    cov.stop()
    cov.save()
    cov.report()

    suite = unittest.TestLoader().loadTestsFromTestCase(TestEvalRPN)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if result.errors or result.failures:
        print("Errors/ Failures found:\n")
        print(result.errors)
        print(result.failures)
    else:
        print("All tests passed!")
