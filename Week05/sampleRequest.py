# sampleRequest.py
# complicated example
# Author: Sharon Curley (lecture)

sampleRequest={
    "Data":{
        "Tags":["debit","checking"],
        "InstructedAmount":{
            "Amount":100,
            "Currency":"GBP"
        },
        "DebtorAccount":{
            "Identification":"320132545645",
            "Name": "DSharon"
        },
        "CreditorAccount":{
            "Identification":"32013254666",
            "Name": "CDes"
        },
        "Risk": "Risk"
    }
}
print(sampleRequest["Data"]["InstructedAmount"]["Amount"])