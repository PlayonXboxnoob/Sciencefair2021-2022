
def verify(unsortedarr, verifylist):

    unsortedarr.sort()

    for i in range(len(verifylist)):
        if verifylist[i] != unsortedarr[i]:
            return False
    return True