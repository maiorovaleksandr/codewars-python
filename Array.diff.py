#here I would like to share 2 full and 1 partial solution

Full Solutions:
======1======
def array_diff(a, b):
    return [l for l in a if l not in b]
    
======2======
def array_diff(a, b):
    for i in b:
      if i in a:
        for j in range(a.count(i)):
          a.remove(i)
    return a

Partial Solution: This test will pass first 18 tests but fail other tests.
def array_diff(a, b):
    return (list(set(a) - set(b)))
