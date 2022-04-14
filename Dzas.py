for _ in dir(__builtins__):
    print(_)




import sys

print(sys.executable)
print(sys.version)
print(sys.platform)




import inspect
import colorama

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))




list=[]
for method in dir(list):
        print(method)