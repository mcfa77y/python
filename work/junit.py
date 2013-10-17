# Copyright 2011 Bricsnet FM
# Author: Ryan Skonnord

"""Utilities for parsing and reporting on XML data output by JUnit.

The XML files that this script works on are output into bc/test/report when
a command such as 'ant test.cactus' is run.
"""

# Uses Python 3
# May not work with Python 2.*

import os
import re
import xml.etree.ElementTree
import xml.parsers.expat


class TestCaseResult:
    """The result from one test case (i.e., method call) in a test class."""

    def __init__(self, class_name, case_name, failed):
        self.class_name = class_name
        self.case_name = case_name
        self.failed = failed

    def key(self):
        """Hashable identifier for the test case."""
        return (self.class_name, self.case_name)

    def failure_message(self):
        """The first line of the saved failure trace.

        Usually this is the string provided as an error message to a JUnit
        assertion or Java exception object, but if that message contains a
        newline it can get cut off.
        """
        try:
            t = self.failure_trace
            if '\n' in t:
                return t[ : t.index('\n')]
            else:
                return t
        except AttributeError:
            return ''

    def exceptions(self):
        """A tuple of the exception chain that caused the failure.

        If the test passed, the tuple is empty. If the test failed by
        assertion, the tuple contains just that failure. If the test was
        caused by an exception being thrown, the tuple contains that
        exception followed recursively by its causes.
        """
        if not self.failure_trace:
            return ()
        excs = [self.failure_message()]
        for m in re.finditer(r'Caused by:\s*(.*)', self.failure_trace):
            excs.append(m.groups()[0])
        return tuple(excs)

    @staticmethod
    def parse_element(xml_element):
        """Parse a <testcase> element from an XML ElementTree."""
        fails = xml_element.findall('failure') + xml_element.findall('error')
        obj = TestCaseResult(xml_element.attrib['classname'],
                             xml_element.attrib['name'],
                             len(fails) > 0)
        if len(fails) == 1:
            f = fails[0]
            obj.failure_tag = f.tag
            obj.failure_trace = f.text
        elif len(fails) > 1:
            print('Multiple failure elements:', obj.key())
        else:
            obj.failure_tag = ''
            obj.failure_trace = ''
        return obj


def parse_junit_xml(file):
    """Parse all test cases in an XML report file.

    The XML report file represents one JUnit test class. The return value
    is a list of TestCaseResult objects, one for each test method in the
    test class.
    """
    try:
        t = xml.etree.ElementTree.parse(file)
    except xml.parsers.expat.ExpatError:
        # This usually happens because an empty file is left behind when a
        # test is interrupted with Ctrl-C. Log and ignore it.
        print('Could not read:', file)
        return []
    except xml.etree.ElementTree.ParseError:
        print('ParseError in:', file)
        return []
    return [TestCaseResult.parse_element(c) for c in t.findall('testcase')]


def parse_report_dir(dirname):
    """Parse a set of XML files in a report directory into a list.

    The directory represents a collection of JUnit test classes. The return
    value is a dictionary of TestCaseResult objects, keyed by (class,
    method) pairs. (To get just a collection of TestCaseResult objects,
    call .values() on the returned object.)
    """
    xml_files = []
    for root, dirs, files in os.walk(dirname):
        xml_files += [root + '/' + file for file in files
                      if file.endswith('.xml')]
    cases = dict()
    for xml in xml_files:
        for case in parse_junit_xml(xml):
            cases[case.key()] = case
    return cases


def measure_regression(before, after):
    """Find new failing cases.

    Each argument should be a dictionary of TestCaseResults, like those
    returned from parse_report_dir. The return value is a list of keys that
    have a failing case in 'after' but a passing case in 'before' (or that
    fail with an error in 'after' and merely violate an assertion in
    'before').

    This method is useful not only for sequential test runs; the trunk can
    be 'before' and a branch can be 'after' to measure bugs introduced in
    the branch.
    """
    regressions = []
    for a in after.values():
        try:
            b = before[a.key()]
        except KeyError:
            print('Unmatched key:', a.key())
            continue
        if ( (a.failed and not b.failed)
             or
             (a.failure_tag == 'error' and b.failure_tag == 'failure') ):
            regressions.append(a.key())
    return regressions


def list_regressions(before_dir, after_dir):
    """Print a human-readable list of new failures.

    Both arguments are paths to report directories.
    """
    before = parse_report_dir(before_dir)
    after = parse_report_dir(after_dir)
    r = measure_regression(before, after)
    for class_name, case_name in sorted(r):
        print(class_name + '.' + case_name)


def group_failures_by_message(reports):
    """Produce a human-readable list of failing cases, grouped by message."""
    d = dict()
    for r in reports:
        if (not r.failed) or (not r.failure_message):
            continue
        m = r.failure_message()
        if m in d:
            d[m].add(r)
        else:
            d[m] = set([r])
    # Sort by size, descending
    report_groups = sorted(d.items(), key=(lambda t: (-len(t[1]), t[0])))
    for m, group in report_groups:
        if len(group) <= 1:
            break
        print('{0} case{1}: {2!r}'.format(len(group),
                                          '' if len(group) == 1 else 's',
                                          m))
        for r in sorted(group, key=TestCaseResult.key):
            print('    ', r.key(), sep='')


def compare_cases(trunk, branch):
    """Find cases that fail in a different way than expected.

    Each argument should be a dictionary of TestCaseResults, like those
    returned from parse_report_dir.  Returns a sorted list of all 'branch'
    cases that fail, except those that also fail in the trunk with an
    identical failure message. Since failure messages often contain unique
    information (such as object IDs or timestamps), this is prone to false
    positives. Alternatively, measure_regressions is more conservative.
    """
    novel_failures = []
    for k, bc in branch.items():
        if not bc.failed:
            continue
        try:
            tc = trunk[k]
        except KeyError:
            print('Could not find:', k)
        if (not tc.failed) or (bc.failure_message() != tc.failure_message()):
            novel_failures.append(bc)
    return sorted(novel_failures, key=TestCaseResult.key)


ENDS_OF_INTERESTING_PARTS = (
    'java.security.AccessControlException: Rule [canCreate] returned an authorization level of NONE on',
    'com.bricsnet.core.util.model.ServiceException: Summary account is missing FC.',
    'com.bricsnet.core.util.model.ServiceException: a different object with the same identifier value was already associated with the session: [com.bricsnet.core.dal.workflow.WorkflowRefObjectDTO#WorkflowRefObjectPK@',
    'Transition Activate (1 to 2) is not allowed on',
    'java.security.AccessControlException: Rule [canUpdate] returned an authorization level of NONE on',
    'org.jbpm.graph.def.DelegationException: Illegal transition from 1 to 4 for',
    'org.jbpm.graph.def.DelegationException: Illegal transition from 1 to 5 for',
    'org.jbpm.graph.def.DelegationException: Transition Approve (1 to 8) is not allowed on',
    'java.security.AccessControlException: Transition PutOnHold (1 to 7) is not allowed on',
    'org.jbpm.graph.def.DelegationException: Illegal transition from 2 to 4 for',
    'org.jbpm.graph.def.DelegationException: Transition Submit (1 to 2) is not allowed on',
    'org.jbpm.graph.def.DelegationException: Transition Decline (1 to 5) is not allowed on',
    'org.jbpm.graph.def.DelegationException: Transition OnHold (1 to 3)',
    'org.jbpm.graph.def.DelegationException: Illegal transition from 1 to 7 for',
    'org.jbpm.graph.def.DelegationException: Illegal transition from 1 to 8 for',
    'junit.framework.AssertionFailedError: rowCount for Property',
    'javax.ejb.EJBException: java.lang.Exception: Problem adding custom Attribute column Attr',
    'Status should be success, was <Status: ERROR',
    'Status should be success, was <Status: SEVERE',
    'javax.ejb.EJBException: com.bricsnet.core.util.model.ServiceException: Cyclic document references',
    'com.bricsnet.core.util.model.ServiceException: Illegal transition from 2 to 4 for ',
    'org.jbpm.graph.def.DelegationException: Transition Invoice (1 to 4) is not allowed on ',
    'org.jbpm.graph.def.DelegationException: Transition Receive (1 to 5) is not allowed on ',
    'javax.ejb.EJBException: org.hibernate.NonUniqueObjectException: a different object with the same identifier value was already associated with the session: ',
    'org.jbpm.graph.def.DelegationException: Transition Close (2 to 4) is not allowed on ',
    'org.jbpm.graph.def.DelegationException: Transition Cancel (2 to 6) is not allowed on ',
    'com.bricsnet.core.util.model.ServiceException: Cyclic document references',
    'com.bricsnet.core.util.publisher.PublishingException: Missing required content for element',
    'java.lang.IllegalArgumentException: Invalid uri',
    'statement conflicted with',
    )
"""Strings that immediately precede unwanted unique information in a trace.

See merge_trace docstring. Each string here should be the *last
interesting* part of the trace; everything immediately after, but not in,
the matched substring is discarded.

This list needs maintenance to stay relevant! See the
print_cases_as_todo_list docstring.
"""


def merge_trace(exception_seq):
    """Remove unnecessarily unique parts of the exception trace.

    Some common error types contain unique information, such as object IDs,
    in their exception traces. This causes the traces to look like distinct
    errors when we want to consider them in the same error category. If one
    of the strings in the argument contains a snippet from
    ENDS_OF_INTERESTING_PARTS, everything following it, including other
    elements of the sequence, is discarded. (The last string has '...'
    appended to mark the change.)

    The argument is a sequence of strings; each string is the error message
    from a chained exception.
    """
    for i, e in enumerate(exception_seq):
        for u in ENDS_OF_INTERESTING_PARTS:
            if u in e:
                interesting_part = list(exception_seq[ : i])
                last_string = e[ : e.index(u) + len(u)] + '...'
                interesting_part.append(last_string)
                return tuple(interesting_part)
    return exception_seq


def print_cases_as_todo_list(cases, output):
    """Write a human-readable list of failures, grouped by message.

    The output requires some massaging to keep it from being broken up into
    too-small chunks. As said in the merge_trace docstring, cases can get
    separated because they contain meaninglessly unique information. If
    this method produces a lot of one-case groups with similar error
    messages, identify the last substring that is common to all of them,
    copy it into ENDS_OF_INTERESTING_PARTS, and run the script again.

    The first argument is a dictionary of TestCaseResults, like those
    returned from parse_report_dir. The second argument is a writable file
    object.
    """

    def total_cases(class_to_cases_dict):
        """Number of test methods among the values."""
        return sum([len(v) for v in class_to_cases_dict.values()])

    # Build a nested-dict structure:
    #   dict( keys:   shared failure messages
    #         values: dict( keys:   test classes
    #                       values: set( test methods with that message )
    #        )             )
    struct = dict()
    for c in cases:
        excs = merge_trace(c.exceptions())
        if excs not in struct:
            struct[excs] = dict()
        if c.class_name not in struct[excs]:
            struct[excs][c.class_name] = set()
        struct[excs][c.class_name].add(c.case_name)

    # Sort in descending order by failure count
    todo = sorted(struct.items(), key=(lambda t: (-total_cases(t[1]), t[0])))

    print('Total unique failure type groups:', len(todo), file=output)
    print(file=output)  # Blank line
    for (exception_tuple, cases_dict) in todo:
        print('-' * 72, file=output)  # Separator bar
        total = total_cases(cases_dict)
        print('{0} test method{1} with failure type:\n'.format(
                total, ('' if total == 1 else 's') ),
              file=output)
        for exception_line in exception_tuple:
            print(exception_line, file=output)
        print(file=output)  # Blank line
        for (class_name, cases_set) in sorted(cases_dict.items()):
            print(' ' * 4, class_name, sep='', file=output)
            for case_name in sorted(cases_set):
                print(' ' * 8, case_name, sep='', file=output)
        print(file=output)  # Blank line
    return todo


LOCATION = 'C:/logs/{0}/'
def make_reports(target, compare_to, location=LOCATION, regression_compare=None):
    """Write a set of report files on a test run.
    """
    report_loc = location + 'report'
    target_cases = parse_report_dir(report_loc.format(target))
    for (compare, report_name) in [(compare_to, 'ReportByErrorMessage'),
                                   (regression_compare, 'Regression')]:
        if compare:
            compare_cases = parse_report_dir(report_loc.format(compare))
            keys_to_fix = measure_regression(compare_cases, target_cases)
            to_fix = [target_cases[k] for k in keys_to_fix]
        else:
            to_fix = target_cases.values()
        filename = (location + '{1}.txt').format(target, report_name)
        with open(filename, mode='w') as f:
            print_cases_as_todo_list(to_fix, f)

# Fill in most recent cases here
make_reports('HibernateCactus20110919B',
             'TrunkCactus20110916',
             regression_compare='HibernateCactus20110919A'
             )
