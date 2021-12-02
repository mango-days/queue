# QUEUE
class Queue :
    def __init__ ( self ): self.array = []
    def push ( self, element ) : self.array.insert( 0 , element )
    def first_out ( self ) : 
        last_index = len( self.array ) - 1
        print ( self.array [ last_index ] )
    def empty ( self ) : self.array = []
    def getMin ( self ) : print ( min ( self.array ) )
    def pop ( self ) : 
        last_index = len( self.array ) - 1
        print ( self.array [ last_index ] )
        self.array.pop ( last_index )
    def printQueue ( self ) : print ( self.array )

a = Queue()
for values in range ( 0 , 5 ): a.push(values)
a.printQueue()
a.pop()
a.pop()
a.getMin()
a.first_out()