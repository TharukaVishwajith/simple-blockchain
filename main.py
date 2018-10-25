import Blockchain as bc
import Block as b

#initialize blockchain
blockchain = bc.Blockchain()

#mine 10 blocks
for n in range(10):
    blockchain.mine(b.Block("Block " + str(n+1)))
    
#print out each block in the blockchain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next