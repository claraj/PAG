# read in the lab's JSON file, run tests, figure out points.
# Remember to edit the grades.json file to assign appropriate points for each assignment.

# Credit to helpful stack overflow.. https://stackoverflow.com/questions/14282783/call-a-python-unittest-from-another-script-and-export-all-the-error-messages

import json
import os
import unittest
import sys
import io
import importlib
import inspect

grade_json_file = 'grades.json'  # Modify this if the filename with points and test files is changed
test_out_file = 'test_report.txt'

# Dump output into text file to not clutter console output.
# test_out.txt is human-readable, may be used for debugging
runner = unittest.TextTestRunner(open(test_out_file, 'w'))


def calc(lab):

    """ Run tests in a lab package (directory) and calculate grade from grades.json
    :param lab: the directory containing the lab materials, e.g. "Lab_1"
    """

    # Read in the grades.json from lab/grades.json
    # This does some verification of the JSON, including that the points per assignment sum sensibly.
    assignment = read_grade_json(lab)

    total_points = assignment.total_points

    print('total points for this assignment:', total_points)

    messages = []

    points_earned = 0

    for question in assignment.questions:

        test_file = question['test_file']
        question_points = question['points']

        print('points available for question ' + question['name'], question_points)

        results = run_test(lab, test_file)

        if not results:
            print('No tests found in test file %s, skipping, no points assigned' % test_file)
            continue

        total_tests_run = 0
        total_fails = 0
        total_errors = 0

        for result in results:

            total_tests_run += result.testsRun
            total_fails += len(result.failures)
            total_errors += len(result.errors)

            for err in result.errors:
                messages.append(err)

            for fail in result.failures:
                messages.append(fail)

            print('result %s: total points %s total tests %s total fails %s total errors %s' % (str(result), total_points, total_tests_run, total_fails, total_errors))

        # Points proportional to number of passing tests
        # So if there are 10 points for the question, and 3 out of 5 tests pass,
        # the assignment receives 6 points.

        passing_tests = total_tests_run - (total_errors + total_fails)

        if passing_tests == 0:
            points_for_question = 0  # Avoid divide by zero errors
        else:
            points_for_question = (passing_tests / total_tests_run) * question_points

        print('points earned for question', points_for_question)
        points_earned += points_for_question


    return points_earned, messages


def run_test(lab, test_file):

    '''
    :param test_file: the test file name, read from JSON. The module/package is assumed
    :return: test results.
    '''

    #test_file = 'Lab_1.tests.q1_test'  # Example, will be read from JSON

    test_file = '%s.tests.%s' % (lab, test_file)
    test_package = importlib.import_module(test_file)

    objects = [m[1] for m in inspect.getmembers(test_package) if inspect.isclass(m[1])]
    print('objects', objects)

    results = []

    for obj in objects:

        # Skip the superclass TestCase
        result = runner.run(unittest.makeSuite(obj))  #
        print('THIS many tests were run', result.testsRun)

        results.append(result)

    return results



class GradeData:
    def __init__(self, gradejson):
        self.__dict__ = json.loads(gradejson)


def read_grade_json(lab):

    filename = os.path.join('..', lab, grade_json_file)

    with open(filename) as f:
        grade_json = f.read()
        assignment = GradeData(grade_json)

    # Verify that the total points == sum of individual assignments

    total_points = assignment.total_points
    question_points = 0

    for question in assignment.questions:
        question_points += question['points']

    assert question_points == total_points, 'Total points for each question in ' + filename + ' must sum to the same value as total_points.'
    assert question_points > 0

    return assignment


# test

pts, msgs = calc('Lab_1')
print('POINTS ', pts)
print('MESSAGES', msgs)

