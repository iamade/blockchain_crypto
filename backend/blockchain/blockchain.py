from backend.blockchain.block import Block

class Blockchain:
    """
    Blockchain: A public ledger of transactions
    Implemented as a list of blocks - data set of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1],data))
        # self.chain.append(Block(data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__:{__name__}')

if __name__ == '__main__':
    main()