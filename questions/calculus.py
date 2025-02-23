import questions.question_scripts as question_scripts
import maths_scripts.calculus
import random
import sympy


def simpsons_rule(difficulty: int) -> [question_scripts.Question, str, float, float]:
    type_id = 3
    number_of_strips = random.choice([4, 6, 8])
    limits_and_function: list = generate_polynomials_check_range(difficulty)
    upper_limit: float = limits_and_function[0]
    lower_limit: float = limits_and_function[1]
    function = limits_and_function[2]
    simpsons_rule_instance = maths_scripts.calculus.SimpsonsRule(number_of_strips, upper_limit, lower_limit, function)
    question_text = "Approximate ∫ {} dx using Simpson's Rule with {} strips " \
                    "between x = {} and x = {}".format(function, number_of_strips, lower_limit, upper_limit)
    correct_answer = round(simpsons_rule_instance.integral(), 2)
    question = question_scripts.Question("Simpson's Rule", type_id, difficulty, question_text, correct_answer)
    upper_limit: float = upper_limit * (random.uniform(1.1, 1.5))
    lower_limit: float = lower_limit * (random.uniform(1.1, 1.5))
    return question, function, lower_limit, upper_limit


def trapezium_rule(difficulty: int) -> [question_scripts.Question, str, float, float]:
    type_id = 4
    number_of_strips = random.randint(4, 8)
    limits_and_function: list = generate_polynomials_check_range(difficulty)
    upper_limit: float = limits_and_function[0]
    lower_limit: float = limits_and_function[1]
    function = limits_and_function[2]
    trapezium_rule_instance = maths_scripts.calculus.TrapeziumRule(number_of_strips, upper_limit, lower_limit, function)
    question_text = "Approximate ∫ {} dx using the Trapezium Rule with {} strips " \
                    "between x = {} and x = {}".format(function, number_of_strips, lower_limit, upper_limit)
    correct_answer = round(trapezium_rule_instance.integral(), 2)
    question = question_scripts.Question("Trapezium Rule", type_id, difficulty, question_text, correct_answer)
    upper_limit: float = upper_limit * (random.uniform(1.1, 1.5))
    lower_limit: float = lower_limit * (random.uniform(1.1, 1.5))
    return question, function, lower_limit, upper_limit


def definite_integral(difficulty: int) -> [question_scripts.Question, str, float, float]:
    type_id = 5
    limits_and_function: list = generate_polynomials_check_range(difficulty)
    upper_limit: float = limits_and_function[0]
    lower_limit: float = limits_and_function[1]
    function = limits_and_function[2]
    integral_instance = maths_scripts.calculus.DefiniteIntegral(upper_limit, lower_limit, function)
    question_text = "Find ∫ {} dx between x = {} and x = {}".format(function, lower_limit, upper_limit)
    correct_answer = round(integral_instance.integral(), 2)
    question = question_scripts.Question("Definite Integral", type_id, difficulty, question_text, correct_answer)
    upper_limit: float = upper_limit * (random.uniform(1.1, 1.5))
    lower_limit: float = lower_limit * (random.uniform(1.1, 1.5))
    return question, function, lower_limit, upper_limit


def generate_polynomials_check_range(difficulty: int) -> list:
    x = sympy.symbols('x')
    while True:
        function_type = random.choice([1, 2])
        if function_type == 1 or difficulty < 3:
            upper_limit = random.randint(3, 10)
            lower_limit = random.randint(1, upper_limit - 1)
            function = maths_scripts.generate_polynomial(random.randint(1, difficulty))
            if not maths_scripts.check_divergent(upper_limit, lower_limit, function):
                return [upper_limit, lower_limit, function]
        elif function_type == 2 and difficulty >= 3:
            function = maths_scripts.generate_compound_trig_function(random.randint(1, difficulty))
            if str(sympy.tan(x)) in str(function) or str(sympy.sec(x)) in str(function):
                upper_limit = round(random.uniform(-1.01, 1), 2)
                lower_limit = round(random.uniform(-1, upper_limit - 0.01), 2)
            elif str(sympy.cot(x)) in str(function) or str(sympy.csc(x)) in str(function):
                upper_limit = round(random.uniform(0.01, 2), 2)
                lower_limit = round(random.uniform(0, upper_limit - 0.01), 2)
            else:
                upper_limit = random.randint(1, 4)
                lower_limit = random.randint(0, upper_limit - 1)
            offset: int = random.randint(-5, 5) * 2
            upper_limit = (upper_limit + offset) * (sympy.pi / 2)
            lower_limit = (lower_limit + offset) * (sympy.pi / 2)
            if not maths_scripts.check_divergent(upper_limit, lower_limit, function):
                return [upper_limit, lower_limit, function]
        else:
            raise ValueError
