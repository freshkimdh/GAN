
class Base(object):
    def __init__(self):
        print("Base created")
        print("안녕하세요") 

# __init__ 상속 방법 1
class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

# __init__ 상속 방법 2, 3
class ChildB(Base):
    def __init__(self):
        super().__init__() # 2
        super(ChildB, self).__init__() # 3

ChildA() 
ChildB()