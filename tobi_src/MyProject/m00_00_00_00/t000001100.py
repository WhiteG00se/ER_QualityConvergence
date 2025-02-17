# -*- coding: utf-8 -*-
def t000001100_1():
    """State 0,1"""
    t000001100_x1()
    Quit()

def t000001100_x0(actionbutton1=6100, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert GetEventFlag(flag1) or GetEventFlag(flag2) or GetEventFlag(flag3) or GetEventFlag(flag4) or GetEventFlag(flag5)
        """State 4"""
        assert not GetEventFlag(flag6)
        """State 2"""
        if (GetEventFlag(flag6) or not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead()
            and not IsCharacterDisabled()) or (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3)
            and not GetEventFlag(flag4) and not GetEventFlag(flag5))):
            pass
        # actionbutton:6100:"Touch grace"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t000001100_x1():
    """State 0"""
    while True:
        """State 3"""
        # actionbutton:6100:"Touch grace"
        assert t000001100_x0(actionbutton1=6100, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000)
        """State 1"""
        UpdatePlayerRespawnPoint()
        assert GetCurrentStateElapsedTime() > 2
        """State 2"""
    """Unused"""
    """State 4"""
    return 0

