class TurnTrackerNode:
# Hint: This class should look just like the LinkNode class (the doubly linked list version)
    ...
    def __init__(self, info , last=None , forward=None):
        self.info=info
        self.last=last
        self.forward=forward


        if last is not None:
            self.last.forward=self
        
        if forward is not None:
            self.forward.last=self
    def __str__(self):
        return f"{self.info}"
    





class TurnTracker:
# Hint: This class shares a lot of functionality/logic with the DoublyLinkedList class from the textbook.
# A good place to start is by looking at that DoublyLinkedList class and examining which methods are going
# to be similar to those needed by the TurnTracker. Then start adjusting those methods to suit your needs here.
    
    ...
    def __init__(self):
        self._head=None
        self._tail=None
        self.length= 0
        self._reversed=False
        self._next_player= None

    def addPlayer(self,Player):
        if self.length==0:
            self._head= self._tail= TurnTrackerNode(Player)

            self._head.forward=self._tail
            self._head.last=self._tail

            self._tail.next=self._head
            self._tail.last=self._tail
        else:
            newNode= TurnTrackerNode(Player,self._tail,self._head)
            self._tail.forward=newNode
            self._tail= newNode
        self.length+=1




    def nextPlayer(self):
        if self._reversed is False:
            if self.length==0:
                raise RuntimeError('No players playing')
            elif self._next_player is None:
                self._next_player = self._head
            else:
                self._next_player= self._next_player.forward
            return self._next_player.info
        if self._reversed is True:
            if self.length==0:
                raise RuntimeError('N/A')
            elif self._next_player is None:
                self._next_player = self._tail
            else:
                self._next_player= self._next_player.last
            return self._next_player.info
    def numberOfPlayers(self):
        return self.length
    def skipNextPlayer(self):
        newnode =None
        if self._reversed is False:
            if self.length==0:
                raise RuntimeError('N/A')
            else:
                newnode=self._next_player.forward 
                self._next_player=newnode
        if self._reversed is True:
            if self.length==0:
                raise RuntimeError('N/A')
            else:
                newnode=self._next_player.last
                self._next_player=newnode
    def reverseTurnOrder (self):
        if self._reversed is False:
            self._reversed = True
        else:
            self._reversed= False
                


