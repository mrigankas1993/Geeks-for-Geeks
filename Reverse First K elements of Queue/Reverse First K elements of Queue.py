
def modifyQueue(q,k):
    # code here
    if k == 0:
        return q
    queue = []
    sas = len(q)
    if k > sas:
        return q
    if k == sas:
        q.reverse()
        return q
    for i in range(sas):
        if i == k:
            queue.reverse()
        queue.append(q[i])
    return queue
