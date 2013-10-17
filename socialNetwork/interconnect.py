#!/usr/bin/python27
  if len(nodes)==2:
        print('hit base case', nodes)
        return [(nodes[0],nodes[1])]
    else:
        results=[]
        first = nodes[0]
        for n in nodes[1:]:
            results.append((first,n))
        results.extend(create_tour(nodes[1:]))
        print results
        return results