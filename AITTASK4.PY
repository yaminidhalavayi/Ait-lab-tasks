

def minimax(node, depth, alpha, beta, max_player):
    if depth == 0:
        return node

    if max_player:
        best = -999
        for x in node:
            val = minimax(x, depth-1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if alpha >= beta: # pruning
                break
        return best
    else:
        best = 999
        for x in node:
            val = minimax(x, depth-1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if alpha >= beta: # pruning
                break
        return best

# Your tree from note
tree = [ [ [3, 5], [6, 9] ],
         [ [1, 2], [0, -1] ] ]

print("Optimal value:", minimax(tree, 3, -999, 999, True))
