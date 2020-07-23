import os
from extensions.gnosis_extension import GnosisExchange

def main():
    if not os.getenv('GN_PRIVATE'):
        print("""
        Usage: 
            place your private key to GN_PRIVATE: 
                export GN_PRIVATE
                
            run example:
                python example.py
        """)
        return 1

    gnosis = GnosisExchange({'secret': os.getenv('GN_PRIVATE'), 'network': 'rinkeby'})

    balance = gnosis.fetch_balance()
    print(balance)
    return 0

if __name__ == "__main__":
    exit(main())
