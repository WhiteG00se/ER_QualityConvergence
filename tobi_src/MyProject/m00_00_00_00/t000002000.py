# -*- coding: utf-8 -*-
def t000002000_1():
    """State 0,1"""
    SetUpdateDistance(1000)
    while Loop('mainloop'):
        """State 2"""
        call = t000002000_x0()
        # eventflag:60110:shop:101802:Spirit Calling Bell
        assert (not (GetEventFlag(GetBuddyStoneSummonedEventFlag()) or GetIsRealMultiplayer() or GetIsHost() or
                (GetBuddyStoneEliminateTarget() >= 0 and not IsEliminateTargetInBuddyArea()) or DoesSelfHaveSpEffect(9531)
                or (not GetEventFlag(2002) and not GetEventFlag(60110))))
        while True:
            """State 4"""
            call = t000002000_x3()
            if call.Done():
                """State 3"""
                call = t000002000_x2()
                if call.Done():
                    pass
                # eventflag:60110:shop:101802:Spirit Calling Bell
                elif (not not (GetEventFlag(GetBuddyStoneSummonedEventFlag()) or GetIsRealMultiplayer() or GetIsHost()
                      or (GetBuddyStoneEliminateTarget() >= 0 and not IsEliminateTargetInBuddyArea()) or DoesSelfHaveSpEffect(9531)
                      or (not GetEventFlag(2002) and not GetEventFlag(60110)))):
                    Continue('mainloop')
            # eventflag:60110:shop:101802:Spirit Calling Bell
            elif (not not (GetEventFlag(GetBuddyStoneSummonedEventFlag()) or GetIsRealMultiplayer() or GetIsHost()
                  or (GetBuddyStoneEliminateTarget() >= 0 and not IsEliminateTargetInBuddyArea()) or DoesSelfHaveSpEffect(9531)
                  or (not GetEventFlag(2002) and not GetEventFlag(60110)))):
                Continue('mainloop')

def t000002000_x0():
    """State 0,1"""
    Quit()
    """Unused"""
    """State 2"""
    return 0

def t000002000_x1(mode1=_):
    """State 0,1"""
    if AreaExists(GetBuddyStoneOverwriteActivateRegion()):
        """State 2"""
        assert IsEntityInArea(True, 10000, GetBuddyStoneOverwriteActivateRegion()) == mode1
    else:
        """State 3"""
        assert (GetDistanceToPlayer() < GetBuddyStoneActivateRange()) == mode1
    """State 4"""
    return 0

def t000002000_x2():
    """State 0,1"""
    def WhilePaused():
        GiveSpEffectToPlayer(9530)
        GiveSpEffectToPlayer(84)
        SetBuddySpawnPoint()
    assert t000002000_x1(mode1=0)
    """State 2"""
    return 0

def t000002000_x3():
    """State 0,1"""
    assert t000002000_x1(mode1=1)
    """State 2"""
    return 0

