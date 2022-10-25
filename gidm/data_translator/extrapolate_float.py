# file based on https://github.com/frzyc/genshin-optimizer/blob/master/pipeline/extrapolateFloat.ts

"""
 # Extrapolate the single-precision number `float` to a double-precision number
 # by assuming that the *actual* value has the fewest number of digits amongst
 # numbers that are rounded to `float`. In case of ambiguity (multiple values
 # with the same number of digits round to `float`), returns the original value.
 #
 # REF: This is inspired by
 # Section 3.1 in Printing Floating-Point Numbers: An Always Correct Method
 # (https://cseweb.ucsd.edu/~lerner/papers/fp-printing-popl16.pdf)
 """
import math

# TODO: extrapolate float
def extrapolate_float(float):
    if not math.isfinite(float):
        return float
    else:
        return float

# TODO: round in range
def round_in_range():
    pass


print(extrapolate_float(1.08224545578))
