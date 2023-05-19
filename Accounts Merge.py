class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result = []
        
        unique_emails = set()
        
        mail_name_map = dict()

        rep_mail_map = defaultdict(list)

        for account in accounts:
            for i in range(1, len(account)):
                unique_emails.add(account[i])
                mail_name_map[account[i]] = account[0]

        unionFind = UnionFind(unique_emails)

        for account in accounts:
            for i in range(2, len(account)):
                unionFind.union(account[1], account[i])

        for mail in unique_emails:
            rep_mail_map[unionFind.find(mail)].append(mail)

        for rep, mails in rep_mail_map.items():
            temp = [mail_name_map[rep]] + sorted(mails)
            result.append(temp)

        return result


class UnionFind:
    def __init__(self, initializer):
        
        self.root = dict()
        self.size = dict()

        for mail in initializer:
            self.root[mail] = mail
            self.size[mail] = 1



    def find(self, x):
        
        root = self.root[x]

        while root != self.root[root]:
            root = self.root[root]

        while x != root:
            parent = self.root[x]
            self.root[x] = root
            x = parent
        
        return root
    
    def union(self, x, y):
        
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep != y_rep:
            if self.size[x_rep] > self.size[y_rep]:
                self.root[y_rep] = self.root[x_rep]
                self.size[x_rep] += self.size[y_rep]

            else:
                self.root[x_rep] = self.root[y_rep]
                self.size[y_rep] += self.size[x_rep]
