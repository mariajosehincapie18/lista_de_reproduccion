class DNode:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

  def __repr__(self):
    return f"{self.value}"

class DoubleLinkedList:
  def __init__(self, head = None, tail = None):
    self.__head = head
    self.__tail = tail
    self.__size = 0

  #Agregar al final de la lista
  def append(self, value):
    new_node = DNode(value) #creo el nuevo nodo
    if(self.__size == 0): #está vacía?
      self.__head = new_node
      self.__tail = new_node
      self.__head.prev = self.__tail #circular
      self.__tail.next = self.__head
    else:
      new_node.prev = self.__tail #el previo del nuevo será el tail actual
      self.__tail.next = new_node #el next del tail actual será el nuevo
      self.__tail = new_node
      self.__head.prev = self.__tail #circular
      self.__tail.next = self.__head
    self.__size += 1 #actualizo el size

  def insert(self, pos, value):
    current_node = self.__head #nodo inicial
    if(pos > self.__size-1):
      raise IndexError("índice inválido")

    new_node = DNode(value)
    #insertar al principio
    if(pos == 0):
      new_node.next = self.__head
      new_node.prev = self.__tail
      self.__head.prev = new_node
      self.__tail.next = new_node
      self.__head = new_node

    elif(pos == self.__size - 1): #insertar al final
      new_node.prev = self.__tail
      new_node.next = self.__head
      self.__tail.next = new_node
      self.__head.prev = new_node
      self.__tail = new_node


    else: #insertar en cualquier parte del medio
        current_node = self.__head
        for _ in range(pos): #recorrremos hasta la posicion deseada
          current_node = current_node.next
        
        #ahora "current_node" esta en la posicion deseada
        prev_node = current_node.prev #Nodo anterior al nodo actual

        #creamos el nuevo nodo
        new_node = DNode(value)
        # conectamos el nuevo nodo entre el nodo previo y el nodo actual
        new_node.prev = prev_node
        new_node.next = current_node
        #atualizamos los punteros  de los nodos adyacentes
        prev_node.next = new_node
        current_node.prev = new_node
    self.__size +=1
        
  def delete_at(self, pos):
    if(pos > self.__size-1) or (self.__size == 0):
      raise IndexError("índice inválido")
    
    if  (self.__size == 1):
      self.__head = None
      self.__tail = None

#eliminar en la posicion 0 head
    elif (pos == 0):
      self.__head =self.__head.next
      self.__head.prev = self.__tail
      self.__tail.next = self.__head
      
 #ultimo nodo
    elif (pos == self.__size -1):
      self.__tail = self.__tail.prev
      self.__tail.next = self.__head
      self.__head.prev = self.__tail
      
    else:
      current_node = self.__head
      for _ in range(pos):
        current_node = current_node.next
      current_node.prev.next = current_node.next
      current_node.next.prev = current_node.prev

    self.__size -=1

      

  def traverse(self):
    current_node = self.__head #punto de partida
    for _ in range(self.__size):
      yield current_node
      current_node = current_node.next
    

  def invtraverse(self):
    current_node = self.__tail #punto de partida
    for _ in range(self.__size):
      yield current_node
      current_node = current_node.prev
  @property
  def size(self):
    return self.__size
    

  def __repr__(self):
    if self.__head is None:
      return "Lista vacia"
    current = self.__head
    values = []
    for _ in range(self.__size):
      values.append(str(current))
      current= current.next
    return "<->".join(values)
  



  


  


  






