def solution(sizes):
    ws = []
    hs = []

    for w, h in sizes:
        if w < h:
            ws.append(h)
            hs.append(w)
        else:
            ws.append(w)
            hs.append(h)

    print(ws)
    print(hs)        
          
    return max(ws) * max(hs)