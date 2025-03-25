from collections import defaultdict


class UF:
    def __init__(self, items):
        self.par = [i for i in range(len(items))]
        self.weights = [1] * len(items)

    def find(self, acct):
        """
        find the main account
        """
        if acct != self.par[acct]:
            self.par[acct] = self.find(self.par[acct])
        return self.par[acct]

    def union(self, acct1, acct2):
        aPar = self.find(acct1)
        bPar = self.find(acct2)

        if aPar == bPar:
            return False

        # default to aPar
        # pick larger parent
        if self.weights[aPar] < self.weights[bPar]:
            self.weights[bPar] += self.weights[aPar]
            self.par[aPar] = bPar
        else:
            self.weights[aPar] += self.weights[bPar]
            self.par[bPar] = aPar

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # set up
        uf = UF(accounts)
        email2AcctNum = {}

        # merge
        for acctNum, items in enumerate(accounts):
            for email in items[1:]:
                if email in email2AcctNum:
                    uf.union(acctNum, email2AcctNum[email])
                else:
                    email2AcctNum[email] = acctNum

        # setup account: email[]
        accountDict = defaultdict(list)

        for email, acctNum in email2AcctNum.items():
            # find main account
            mainAcct = uf.find(acctNum)
            accountDict[mainAcct].append(email)

        res = []

        # name + sorted(emails)
        for acct, emailList in accountDict.items():
            name = accounts[acct][0]
            res.append([name] + sorted(emailList))

        return res
