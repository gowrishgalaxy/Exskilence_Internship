class A:
    def func(self,*args):
        sum=0
        for i in args:
            sum+=i
        print(sum)


obj=A()
obj.func(3,5)