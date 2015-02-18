def main():
    class MyClass:
        """A simple example class"""
        i = 12345
        def f(self):
            return 'Howdy'
    print 'The value of i is, ' + str(MyClass.i)
    x = MyClass()
    print x.f()
main()
