# A constraint system consists of a set of constraints imposing on a sequence of decision variables x1, x2, ..., xN.
# Each values of (v1, v2, . . ., vN) of (x1, x2, ..., xN) give a candidate solution to the constraint system. Each candidate solution s may have a specified number of violations of a given constraint c, denoted by v(s,c).
# AllDifferent(x1, x2, ..., xN): the number of violations of AllDifferent is defined to the number of pairs of 2 variables xi, and xj which have the same value.
# IsEqual(x1, x2): the number of violations of IsEqual(x1, x2) is defined to be |x1-x2|
# LessThanEqual(x1, x2): the number of violations of LessThanEqual(x1, x2) is defined to be max(0, x1 - x2)
#
# For example, with 4 decision variables (x1, x2, x3, x4), the current candidate solution s = (1, 3, 3, 1).
# violations of AllDifferent(x1, x2, x3, x4) = v(s,AllDifferent(x1,x2,x3,x4)) = 2
# violations of IsEqual(x1, x2) = v(s,IsEqual(x1, x2)) = 2
# violations of IsEqual(x1, x4) = v(s,IsEqual(x1, x4)) = 0
# violations of LessThanEqual(x1, x3) = v(s,LessThanEqual(x1, x3) = 0
# violations of LessThanEqual(x2, x4) = v(s,LessThanEqual(x2, x4) = max(0,3-1) = 2
#
# The violations of the constraint system is defined to be the sum of the violations of contraints posted to the constraint system.
# During the resolution of the contraint system, the values of decision variables change, hence, the violations of the constraint system changes.
#
# Given a current candidate solution (v1, v2, . . ., vN) to a contraint system, perform a sequence of action including posting a new contraint to the constraint system, updating the value of a decision variable.

import numpy as np


N = int(input())
arr = [int(i) for i in input().split()]
constraints = []
total_violations = 0
violation_calls = []
def update(inp, index, value):
    inp[index - 1] = value
def all_different(inp):
    violations = 0
    entries = list(set(arr))
    for entry in entries:
        count = inp.count(entry)
        if count == 2:
            violations += 1
        if count > 2:
            violations += int(((count)*(count-1))/2)
    return violations
def is_equal(inp, i1, i2):
    return abs(inp[i1-1] - inp[i2-1])
def less_than_equal(inp, i1, i2):
    return max(0, inp[i1-1] - inp[i2-1])
def constraint_check(inp, stem, arg1, arg2):
    if stem == 'AllDifferent':
        return all_different(inp)

    elif stem == 'IsEqual':
        return is_equal(inp, arg1, arg2)

    elif stem == 'LessThanEqual':
        return less_than_equal(inp, arg1, arg2)
def rerun_constraints(inp, constraints_queue):
    new_violations = 0
    for i in constraints_queue:
        if i[1] == 'AllDifferent':
            new_violations += constraint_check(inp, i[1], 0, 0)
        else:
            new_violations += constraint_check(inp, i[1], int(i[2]), int(i[3]))
    return new_violations
while True:
    command = input().split()

    if command[0] == 'post':
        constraints.append(command)
        if command[1] == 'AllDifferent':
            total_violations += constraint_check(arr, command[1], 0, 0)
        else:
            total_violations += constraint_check(arr, command[1], int(command[2]), int(command[3]))

    elif command[0] == 'update':
        update(arr, int(command[1]), int(command[2]))
        total_violations = rerun_constraints(arr, constraints)

    elif command[0] == 'violations':
        violation_calls.append(total_violations)

    elif command[0] == '#':
        for i in violation_calls:
            print(i)



