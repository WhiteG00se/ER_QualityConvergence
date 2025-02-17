# -*- coding: utf-8 -*-
def t000002100_1():
    """State 0,1"""
    SetUpdateDistance(170)
    while Loop('mainloop'):
        """State 4"""
        call = t000002100_x0()
        # eventflag:60110:shop:101802:Spirit Calling Bell
        assert not GetEventFlag(GetBuddyStoneSummonedEventFlag()) and (GetEventFlag(2002) or GetEventFlag(60110))
        while True:
            """State 3"""
            call = t000002100_x3()
            if call.Done():
                """State 2"""
                call = t000002100_x2()
                if call.Done():
                    pass
                # eventflag:60110:shop:101802:Spirit Calling Bell
                elif GetEventFlag(GetBuddyStoneSummonedEventFlag()) or not (GetEventFlag(2002) or GetEventFlag(60110)):
                    Continue('mainloop')
            # eventflag:60110:shop:101802:Spirit Calling Bell
            elif GetEventFlag(GetBuddyStoneSummonedEventFlag()) or not (GetEventFlag(2002) or GetEventFlag(60110)):
                Continue('mainloop')

def t000002100_x0():
    """State 0,1"""
    Quit()
    """Unused"""
    """State 2"""
    return 0

def t000002100_x1(mode1=_):
    """State 0,1"""
    if AreaExists(GetBuddyStoneOverwriteActivateRegion()):
        """State 2"""
        assert IsEntityInArea(True, 10000, GetBuddyStoneOverwriteActivateRegion()) == mode1
    else:
        """State 3"""
        assert (GetDistanceToPlayer() < GetBuddyStoneActivateRange()) == mode1
    """State 4"""
    return 0

def t000002100_x2():
    """State 0,1"""
    def WhilePaused():
        GiveSpEffectToPlayer(9530)
        GiveSpEffectToPlayer(84)
        SetBuddySpawnPoint()
    assert t000002100_x1(mode1=0)
    """State 2"""
    return 0

def t000002100_x3():
    """State 0,1"""
    assert t000002100_x1(mode1=1)
    """State 2"""
    return 0

