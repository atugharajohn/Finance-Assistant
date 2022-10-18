import requests
import json
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def PoA():
    rpc_url = 'http://127.0.0.1:7545'
    try:
        response = requests.post(rpc_url, json={"jsonrpc": "2.0", "method": "net_version", "params": [], "id": 1})
        response.raise_for_status()
        result = response.json()

        if 'result' in result:
            network_id = result['result']
            print(f"Connected to Ganache, Network ID: {network_id}")
        else:
            print("Error connecting to Ganache")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Ganache: {e}")

    account = '0xeE09B110FB9013bCbF8bC2F31f4f0f5b3433d5FB'  
    default_account = account.lower()
    print(f"Default account set to: {default_account}")
    contract_source = """
    pragma solidity ^0.8.0;
    contract SimpleStorage {
        uint storedData;

        function set(uint x) public {
            storedData = x;
        }

        function get() public view returns (uint) {
            return storedData;
        }
    }
    """
    contract_data = {"language": "Solidity", "sources": {"SimpleStorage.sol": {"content": contract_source}}, "settings": {"outputSelection": {"*": {"*": ["*"]}}}}
    response = requests.post(rpc_url, json={"jsonrpc": "2.0", "method": "eth_compileSolidity", "params": [contract_data], "id": 1})
    response.raise_for_status()

    compiled_result = response.json()
    if 'result' in compiled_result and 'contracts' in compiled_result['result']:
        contracts = compiled_result['result']['contracts']
        if contracts:
            contract = next(iter(contracts.values()))
            compiled_code = contract['SimpleStorage']['evm']['bytecode']['object']
            compiled_abi = contract['SimpleStorage']['abi']
        else:
            print("Error: No contracts found in the compilation result.")
    else:
        print("Error: Invalid compilation result format.")

    nonce = requests.post(rpc_url, json={"jsonrpc": "2.0", "method": "eth_getTransactionCount", "params": [account, "latest"], "id": 1})
    gas_price = requests.post(rpc_url, json={"jsonrpc": "2.0", "method": "eth_gasPrice", "params": [], "id": 1})
    transaction_params = {
        "from": default_account,
        "gas": hex(3000000),
        "gasPrice": gas_price.json()['result'],
        "nonce": nonce.json()['result'],
    }
    transaction = {
        "jsonrpc": "2.0",
        "method": "eth_sendTransaction",
        "params": [transaction_params],
        "id": 1
    }
    response = requests.post(rpc_url, json=transaction)
    response.raise_for_status()
    tx_hash = 5

    receipt = None
    
