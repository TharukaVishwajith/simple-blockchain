import Block

#defining the blockchain datastructure
#consists of 'blocks' linked together
#to form a 'chain'. Thats why its called
#'blockchain'
class Blockchain:
    
    #mining difficulty
    diff = 20
    #2^32. This is the maximum number
    #we can store in a 32-bit number
    maxNonce = 2**32
    #target hash, for mining
    target = 2 ** (256-diff)

    #generates the first block in the blockchain
    #this is called the 'genesis block'
    block = Block.Block("Genesis")
    #sets it as the head of our blockchain
    head = block

    #adds a given block to the chain of blocks
    #the block to be added is the only parameter
    def add(self, block):
        
        #set the hash of a given block
        #as our new block's previous hash
        block.previous_hash = self.block.hashFun()
        #set the block # of our new block
        #as the given block's # + 1, since
        #its next in the chain
        block.blockNo = self.block.blockNo + 1

        #set the next block equal to 
        #itself. This is the new head 
        #of the blockchain
        self.block.next = block
        self.block = self.block.next

    #Determines whether or not we can add a given block to
    #the blockchain
    def mine(self, block):
        #from 0 to 2^32 
        for n in range(self.maxNonce):
            #is the value of the given block's hash less than our target value?
            if int(block.hashFun(), 16) <= self.target:
                #if it is,
                #add the block to the chain
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
   
