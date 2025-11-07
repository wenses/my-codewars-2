def what_list_am_i_on(actions):
    na,ni=0,0
    for action.lower() in actions:
        if action.startswith('b') or action.startswith('k') or action.startswith('f'):
            na+=1
        elif action.startswith('g') or action.startswith('s') or action.startswith('n'):
            ni+=1
    if na>ni:
        ans="naughty
    elif na==ni:
        ans="naughty"
    else:
        ans="nice"
        
    

bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']


print(what_list_am_i_on(bad_actions))
