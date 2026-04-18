# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Triplet:
    def __init__(self, node, x, y):
        self.node = node
        self.x = x
        self.y = y

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = {}
        q = [Triplet(root, 0, 0)]
        while q:
            sz = len(q)
            temp = {}
            for i in range(sz):
                node = q[0].node
                x = q[0].x
                y = q[0].y
                q.pop(0)
                if y not in temp:
                    temp[y] = []
                temp[y].append(node.val)
                if node.left :
                    q.append(Triplet(node.left, x+1, y-1))
                if node.right :
                    q.append(Triplet(node.right, x+1, y+1))
            # iterate over temp, uski saari keys k corresponding
            # list ko sort krke ans m daaldo
            for k,v in temp.items():
                v = sorted(v)
                if k not in ans:
                    ans[k] = []
                ans[k].append(v)
        print(ans)

        # iterate over ans, put all the values in a 2d list
        # sorted according to their keys

        res = []
        for i in sorted(ans.keys()):
            res.append(ans[i])

        return res
    