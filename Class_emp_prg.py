class Employee :
 def __init__(self,no=0,name="",sal=0.0):   #to allocate memory
  self.__empno=no
  self.__empname=name
  self.__sal=sal
 def getEmpname(self):  # getter method
  return self.__empname
 def setEmpname(self,name): # setter method
  self.__empname=name
 def getEmpno(self):
  return self.__empno
 def setEmpno(self,no):
  self.__empno=no
 def getEmpsal(self):
  return self.__empsal
 def setEmpsal(self,sal):
  self.__Empsal=sal
  
 def display(self):

   print("NO:",self.__empno)
   print("Name: ",self.__empname)
   print("Sal:",self.__sal)
