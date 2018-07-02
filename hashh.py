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
    self.keys = []
    
  def insert (self, nombre, apellido, telefono, mail):
    pos = hashstr(apellido,self.size)
    self.keys.append(apellido)
    if self.list[pos] is not None:
      ok = False
      for t in self.list[pos]:
        if t[0] is apellido:
           t[1] = node(nombre, apellido, telefono, mail)
           ok = True
      if not ok:
        self.list[pos].append(node (nombre, apellido, telefono, mail))
    else: 
      self.list[pos] = []
      self.list[pos].append(apellido, node(nombre, apellido, telefono, mail))
    
  def get(self,apellido):
    for e in self.list[hashstr(apellido,self.size)]:
      if e[0] is apellido:
        return e[1]
  
  def eliminar(self,apellido):
    pos = hashstr(apellido,self.size)
    if self.list[pos] is None:
      return False
    else: 
      for i in self.list[pos]:
        if i[0] is apellido:
          i[0] = None
          i[1] = None
  def imprimir (self):
    datos = []
    for i in range (0,len(self.keys),+1):
      x = None
      x = get(self.keys[i])
      datos.append(x)
    menor = datos[0]
    while true:
      for i in range (0,len(datos),+1):
        if menor.apellido[0] >= datos[i].apellido[0]:
          nro = None
          menor = datos[i]
          nro = i
      print ("datos:", menor.nombre, menor.apellido, menor.telefono, menor.mail)
      datos[nro].remove
      if len(datos) == 0:
        false

