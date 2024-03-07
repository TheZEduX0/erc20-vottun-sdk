import requests

class ERC20SDK:
    def __init__(self):
        self.deploy_url = "https://api.vottun.tech/erc/v1/erc20/deploy"
        self.transfer_url = "https://api.vottun.tech/erc/v1/erc20/transfer"
        self.transfer_from_url = "https://api.vottun.tech/erc/v1/erc20/transferFrom"
        self.increase_allowance_url = "https://api.vottun.tech/erc/v1/erc20/increaseAllowance"
        self.decrease_allowance_url = "https://api.vottun.tech/erc/v1/erc20/decreaseAllowance"
        self.allowance_url = "https://api.vottun.tech/erc/v1/erc20/allowance"
        self.name_url = "https://api.vottun.tech/erc/v1/erc20/name"
        self.symbol_url = "https://api.vottun.tech/erc/v1/erc20/symbol"
        self.total_supply_url = "https://api.vottun.tech/erc/v1/erc20/totalSupply"
        self.decimals_url = "https://api.vottun.tech/erc/v1/erc20/decimals"
        self.balance_of_url = "https://api.vottun.tech/erc/v1/erc20/balanceOf"
    
    def deploy_contract(self, name, symbol, alias, initial_supply, network, gas_limit=None):
        payload = {
            "name": name,
            "symbol": symbol,
            "alias": alias,
            "initialSupply": initial_supply,
            "network": network,
            "gasLimit": gas_limit
        }
        response = requests.post(self.deploy_url, json=payload)
        return response.json()

    def transfer_tokens(self, contract_address, recipient, network, amount, gas_limit=None):
        payload = {
            "contractAddress": contract_address,
            "recipient": recipient,
            "network": network,
            "amount": amount,
            "gasLimit": gas_limit
        }
        response = requests.post(self.transfer_url, json=payload)
        return response.json()

    def transfer_from(self, contract_address, sender, recipient, network, amount, gas_limit=None):
        payload = {
            "contractAddress": contract_address,
            "sender": sender,
            "recipient": recipient,
            "network": network,
            "amount": amount,
            "gasLimit": gas_limit
        }
        response = requests.post(self.transfer_from_url, json=payload)
        return response.json()

    def increase_allowance(self, contract_address, spender, network, added_value, gas_limit=None):
        payload = {
            "contractAddress": contract_address,
            "spender": spender,
            "network": network,
            "addedValue": added_value,
            "gasLimit": gas_limit
        }
        response = requests.post(self.increase_allowance_url, json=payload)
        return response.json()

    def decrease_allowance(self, contract_address, spender, network, subtracted_value, gas_limit=None):
        payload = {
            "contractAddress": contract_address,
            "spender": spender,
            "network": network,
            "subtractedValue": subtracted_value,
            "gasLimit": gas_limit
        }
        response = requests.post(self.decrease_allowance_url, json=payload)
        return response.json()

    def get_allowance(self, contract_address, owner, spender, network):
        payload = {
            "contractAddress": contract_address,
            "owner": owner,
            "spender": spender,
            "network": network
        }
        response = requests.post(self.allowance_url, json=payload)
        return response.json()

    def get_name(self, contract_address, network):
        payload = {
            "contractAddress": contract_address,
            "network": network
        }
        response = requests.post(self.name_url, json=payload)
        return response.json()

    def get_symbol(self, contract_address, network):
        payload = {
            "contractAddress": contract_address,
            "network": network
        }
        response = requests.post(self.symbol_url, json=payload)
        return response.json()

    def get_total_supply(self, contract_address, network):
        payload = {
            "contractAddress": contract_address,
            "network": network
        }
        response = requests.post(self.total_supply_url, json=payload)
        return response.json()

    def get_decimals(self, contract_address, network):
        payload = {
            "contractAddress": contract_address,
            "network": network
        }
        response = requests.post(self.decimals_url, json=payload)
        return response.json()

    def get_balance_of(self, contract_address, network, address):
        payload = {
            "contractAddress": contract_address,
            "network": network,
            "address": address
        }
        response = requests.post(self.balance_of_url, json=payload)
        return response.json()


# Ejemplo de uso:
if __name__ == "__main__":
    sdk = ERC20SDK()
    response = sdk.deploy_contract(
        name="VottunToken",
        symbol="TKN",
        alias="My First Token",
        initial_supply=1000000000000000000000000000,
        network=43113,
        gas_limit=6000000
    )
    print(response)
