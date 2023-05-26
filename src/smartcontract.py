from web3 import Web3

def connect_to_ethereum(network_url):
    w3 = Web3(Web3.HTTPProvider(network_url))
    return w3

# Cargar el contrato inteligente
def load_contract(w3, contract_address):
    contract_abi = [
        {
            "constant": False,
            "inputs": [
                {
                    "name": "data",
                    "type": "string"
                }
            ],
            "name": "sendData",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "getData",
            "outputs": [
                {
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
    ]

    return w3.eth.contract(address=contract_address, abi=contract_abi)

# Enviar texto al contrato inteligente
def send_text(w3, contract, text_to_send, sender_address, private_keyETH):
    transaction = contract.functions.sendData(text_to_send).buildTransaction({
        'from': sender_address,
        'gas': 100000,
        'gasPrice': w3.toWei('1', 'gwei'),
        'nonce': w3.eth.getTransactionCount(sender_address)
    })
    signed_transaction = w3.eth.account.signTransaction(transaction, private_key=private_keyETH)
    tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    return tx_hash

# Obtener texto almacenado en el contrato inteligente
def get_stored_text(w3, contract):
    stored_text = contract.functions.getData().call()
    return stored_text
