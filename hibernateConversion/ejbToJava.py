#!/usr/bin/python
import re

FINDER_PATTERN = re.compile(r'''
\@ejb\.finder .*? signature \s* = \s* "
(.*?) # The return type
\s+
(.*?) # The method name and arguments
" .*? query \s* = \s* "
select \s+ object \( (.*?) \)  # The object name
\s+ from \s+ (.*?)  # The table name, which implies the DTO name
as \s+ .*? \s+      # Ignore the second instance of the object name
where \s+ (.*?)     # The where clause and trailing clauses (e.g., order by)
"  # This might hit an escaped \'"\' in the where clause
''', flags=(re.VERBOSE | re.DOTALL | re.IGNORECASE))

PARAMETER_PATTERN = re.compile(r'''
([^\s\(]+)  # Type
\s+
([^\s]+)  # Name
\s* (,|\))
''', flags=re.VERBOSE)

COMMENT_FIX_PATTERN = re.compile(r'\n\s*\*\s*')

TYPE_SIMPLIFY_PATTERN = re.compile(r'java\.(lang|util|math)\.')

PARAMETER_COUNT_WARNING = '''
// TODO: Query contains repeated parameters; put them in method call.
'''.strip()

UNUSED_PARAMETER_WARNING = '''
// TODO: Argument(s) not used as parameters?
'''.strip()

PARAMETER_ORDER_WARNING = '''
// TODO: Check that parameter order matches query, then delete this.
'''.strip()

HIBERNATE_PARAM_TYPES = set(['String', 'Integer', 'Boolean', 'Long', 'Short',
                             'Byte', 'Double', 'Float', 'Character',
                             'BigInteger', 'BigDecimal', 'Date', 'Calendar',
                             'Locale', 'int'])

def get_all_finders(text):
    """Parse the fields from a string containing @ejb.finder tags."""
    return [match.groups() for match in FINDER_PATTERN.finditer(text)]

def finder_to_java(groups):
    """Given the fields from get_all_finders, generate Java code."""
    INDENT = ' ' * 4
    groups = [COMMENT_FIX_PATTERN.sub('', g.strip()) for g in groups]
    returntype, method, objectname, table, where = groups
    returntype = TYPE_SIMPLIFY_PATTERN.sub('', returntype)

    # Infer the Java return type
    dtotype = table + 'DTO'
    is_collection = (returntype in ('Collection', 'List'))
    javareturn = ('Collection<{0}>'.format(dtotype) if is_collection else dtotype)

    method = TYPE_SIMPLIFY_PATTERN.sub('', method)
    output = [INDENT, 'public static ', javareturn, ' ', method, '{\n']

    # Build the query
    where = re.sub(objectname + r'\s*\.', '', where)
    where = re.sub(r'\?[0-9]+', '?', where)
    query = ['from ', dtotype, ' where ', where]
    output += [INDENT * 2, 'String hql = "'] + query + ['";\n']

    # Build the method call
    method_call = ('queryForList' if is_collection else 'queryForSingleResult')
    parameters = [m.groups() for m in PARAMETER_PATTERN.finditer(method)]
    for p in parameters:
        param_type = p[0]
        if param_type not in HIBERNATE_PARAM_TYPES:
            raise ValueError('Parameter type not recognized for Hibernate: '+str(param_type))
    method_args = [p[1] for p in parameters]

    # Some error-checking on query parameters
    if len(parameters) == 0:
        if '?' in where:
            raise ValueError('Query needs parameters: '+where)
    else:
        qmark_count = len(list(re.finditer(r'\?', where)))
        if (qmark_count > len(parameters)):
            output += [INDENT * 2, PARAMETER_COUNT_WARNING, '\n']
        elif (qmark_count < len(parameters)):
            output += [INDENT * 2, UNUSED_PARAMETER_WARNING, '\n']
        elif qmark_count != 1:
            output += [INDENT * 2, PARAMETER_ORDER_WARNING, '\n']

    output += [INDENT * 2, 'return (', javareturn, ') HibernateUtil.',
               method_call, '(hql',]
    output += [', ' + a for a in method_args]
    output += [');\n']

    output += [INDENT, '}\n']
    return ''.join(output)

def parse_finders(text):
    """Parse all finders from a comment and print equivalent Java code."""
    out = open("outputEJB2Java.java",'w')
    for findermatch in get_all_finders(text):
    	out.write(finder_to_java(findermatch))
        print(finder_to_java(findermatch))

pf = parse_finders

def main():
	text = '''
    * @ejb.finder signature="Account findByAlphaId(java.lang.String alphaId,
 *             java.lang.Integer parentId)" query="select object(c) from Account
 *             as c where c.alphaId = ?1 and c.coaId = ?2 and c.deleteStatus =
 *             0"
 '''
	parse_finders(text)
main()


