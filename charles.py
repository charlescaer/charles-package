from pyinstruments.pyhardwaredb import instrument

DORMEUR = instrument("dormeur")

SAMPLE = 'S11-1300'
MEMBRANE = 'M5'

def get_finesse(name='no-name',
                tags=['finesse', 
                      'sample',
                      'sample/'+SAMPLE,
                      'sample/' + SAMPLE + '/' + MEMBRANE],
                comment='',
                ch=None):
    """
    petite fonction pour acquerir une courbe de finesse sur l'oscillo dormeur, les parametres
    sont ...
    """
    if ch:
        DORMEUR.ch_idx = ch
    curve = DORMEUR.get_curve()
    curve.name = name
    curve.tags = tags
    curve.params['comment'] = comment
    curve.save()
    
    fit_curve = curve.fit('doublelorentz', autosave=True)
    finesse = (fit_curve.params['x2'] - fit_curve.params['x1'])/fit_curve.params['bandwidth']
    curve.params["finesse"] = finesse
    curve.save()
    print "finesse : " + finesse