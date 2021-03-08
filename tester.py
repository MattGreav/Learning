

def bar():
    try:
        import mod 
        from mod import James
        return James.name, James.job
    except ImportError:
        print('Module not found')

import mod 
from mod import James, Foo

print(bar())
print(dir())