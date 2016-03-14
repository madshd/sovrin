def txn(txnType,
        targetId,
        sponsor=None,
        agent=None,
        data=None):
    return {
            'txnType': txnType,
            'targetId': targetId,
            'origin': sponsor,
            'agent': agent,
            'data': data}


# client transaction types
ADD_NYM = "ADD_NYM"
ADD_ATTR = "ADD_ATTR"
IDPROOF = "IDPROOF"
ADD_SPONSOR = "ADD_SPONSOR"
ADD_AGENT = "ADD_AGENT"
ASSIGN_AGENT = "ASSIGN_AGENT"

# TODO: Move them to a separate file
# ROLE types
STEWARD = "STEWARD"


def storedTxn(txnTyp, nym, txnId, role=None, data=None):
    return {
        "type": txnTyp,
        "nym": nym,
        "role": role,
        "data": data,
        "txnId": txnId
    }


def getGenesisTxns():
    return [storedTxn(ADD_NYM,
                    "a3716a7674d089456c603adb5575800bc2d4988e00bc297be7e595de2de61150",
                    "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
                    role=STEWARD),
            ]