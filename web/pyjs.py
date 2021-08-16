'''
Re-use the python implementation of the normalization routine.
'''
from browser import window
import snark

def doNormalizeARK(src):
    res, infl = snark.normalizeARK(src)
    return {"result":res, "inflection": infl.name}

# Add methods to window namespace for calling from javascript
window.jsNormalizeARK = doNormalizeARK
window.jsPiecesOfARK = snark.piecesOfARK

