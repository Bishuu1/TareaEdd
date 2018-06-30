def str2num(apellido):
  return sum([ord(c) for c in apellido])

 def hashstr(apellido,size):
    return str2num(apellido)%size

class node:
  def __init__(self, nombre, apellido, telefono, mail):
      self.nombre = nombre
      self.apellido = apellido
      self.telefono = telefono
      self.mail = mail

class hash:
  def __init__(self,size):
    self.list = [None]*size
    self.size = size
    
  def insert (self, nombre, apellido , telefono, mail):
    pos = hashstr(apellido,self.size)
    if self.list[pos] is not None:
      ok = False
      for t in self.list[pos]:
        if t[0] is apellido:
           t[1] =  nombre , telefono, mail
          ok = True
      if not ok:
        self.list[pos].append([ apellido, nombre , telefono, mail])
    else:
      self.list[pos] =[]
      self.list[pos].append([ nombre, apellido , telefono, mail])
    
  def get(self,apellido):
    for e in self.list[hashstr(apellido,self.size)]:
      if e[0] is apellido:
        return e[1]