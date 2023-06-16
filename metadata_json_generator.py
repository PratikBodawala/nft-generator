def get_data(number, total):
    return {
        "name": f"Number #{str(number).zfill(4)}",
        "symbol": "NB",
        "description": f"Collection of {total} numbers on the blockchain. This is the number {number}/{total}.",
        "image": f"{number}.png",
        "attributes": [
            {
                "trait_type": "Number",
                "value": f"{number}"
            }
        ],
        "properties": {
            "files": [
                {
                    "uri": f"{number}.png",
                    "type": "image/png"
                }
            ]
        }
    }
