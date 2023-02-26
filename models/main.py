#!/usr/bin/python3



BaseModel = __import__('base_model').BaseModel
my = BaseModel()
nee = repr(my)
print(my.to_dict())

yours = BaseModel(**my.to_dict())
print(yours)

mine = repr(yours)
print (mine)
his = eval(mine)
print(his.id)