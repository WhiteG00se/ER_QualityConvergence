# -*- coding: utf-8 -*-
def t910000000_1():
    """State 0,1"""
    t910000000_x0()
    Quit()

def t910000000_x0():
    """State 0"""
    if not IsClientPlayer():
        """State 1"""
        Label('L0')
        call = t910000000_x1()
        assert IsClientPlayer()
    else:
        pass
    """State 2"""
    call = t910000000_x2()
    assert not IsClientPlayer()
    Goto('L0')
    """Unused"""
    """State 3"""
    return 0

def t910000000_x1():
    """State 0"""
    while True:
        """State 2"""
        assert t910000000_x4(actionbutton1=6581, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000)
        """State 1"""
        TurnCharacterToFaceEntity(-1, 10000, -1, -1)
        assert t910000000_x3() or GetDistanceToPlayer() > 3
        """State 4"""
        assert t910000000_x5()
    """Unused"""
    """State 5"""
    return 0

def t910000000_x2():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t910000000_x3():
    """State 0"""
    SetEventFlag(1099000106, 1)
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000040, -1)
        AddTalkListData(2, 910000041, -1)
        AddTalkListData(3, 910000042, -1)
        AddTalkListData(4, 910000043, -1)
        AddTalkListData(5, 910000044, -1)
        AddTalkListData(6, 910000045, -1)
        AddTalkListData(7, 910000046, -1)
        AddTalkListDataIf(GetEventFlag(6951) == 1, 8, 910000047, -1)
        # action:20000009:"Leave"
        AddTalkListData(21, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 9"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 5,7"""
            assert t910000000_x6()
        elif GetTalkListEntryResult() == 2:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            assert t910000000_x7()
        elif GetTalkListEntryResult() == 3:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            assert t910000000_x8()
        elif GetTalkListEntryResult() == 4:
            """State 14"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            assert t910000000_x9()
        elif GetTalkListEntryResult() == 5:
            """State 16"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 17"""
            assert t910000000_x10()
        elif GetTalkListEntryResult() == 6:
            """State 18"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 19"""
            assert t910000000_x11()
        elif GetTalkListEntryResult() == 7:
            """State 20"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 21"""
            assert t910000000_x12()
        elif GetTalkListEntryResult() == 8:
            """State 22"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 23"""
            assert t910000000_x13()
        elif GetEventFlag(1099000105):
            """State 24"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x1()
            """State 46"""
            return 0

def t910000000_x4(actionbutton1=6581, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
                and not DoesSelfHaveSpEffect(1400))
        """State 3"""
        assert GetEventFlag(flag1) or GetEventFlag(flag2) or GetEventFlag(flag3) or GetEventFlag(flag4) or GetEventFlag(flag5)
        """State 4"""
        assert not GetEventFlag(flag6)
        """State 2"""
        if (GetEventFlag(flag6) or not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead()
            and not IsCharacterDisabled()) or (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3)
            and not GetEventFlag(flag4) and not GetEventFlag(flag5))):
            pass
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t910000000_x5():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t910000000_x6():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000000, -1)
        AddTalkListData(2, 910000001, -1)
        AddTalkListData(3, 910000019, -1)
        # action:15000372:"Cancel"
        AddTalkListData(20, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            SetEventFlag(97000, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 2:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            SetEventFlag(97001, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 3:
            """State 14"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            SetEventFlag(97019, 1)
            assert t910000000_x5()
        elif GetEventFlag(1099000105):
            """State 5"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x3()
            """State 46"""
            return 0

def t910000000_x7():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000005, -1)
        AddTalkListData(2, 910000006, -1)
        AddTalkListData(3, 910000007, -1)
        # action:15000372:"Cancel"
        AddTalkListData(20, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            SetEventFlag(97005, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 2:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            SetEventFlag(97006, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 3:
            """State 14"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            SetEventFlag(97007, 1)
            assert t910000000_x5()
        elif GetEventFlag(1099000105):
            """State 5"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x3()
            """State 46"""
            return 0

def t910000000_x8():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000002, -1)
        AddTalkListData(2, 910000004, -1)
        AddTalkListData(3, 910000003, -1)
        # action:15000372:"Cancel"
        AddTalkListData(20, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            SetEventFlag(97002, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 2:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            SetEventFlag(97004, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 3:
            """State 14"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            SetEventFlag(97003, 1)
            assert t910000000_x5()
        elif GetEventFlag(1099000105):
            """State 5"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x3()
            """State 46"""
            return 0

def t910000000_x9():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000008, -1)
        AddTalkListData(2, 910000009, -1)
        # action:15000372:"Cancel"
        AddTalkListData(20, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            SetEventFlag(97008, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 2:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            SetEventFlag(97009, 1)
            assert t910000000_x5()
        elif GetEventFlag(1099000105):
            """State 5"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x3()
            """State 46"""
            return 0

def t910000000_x10():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000011, -1)
        AddTalkListData(2, 910000010, -1)
        AddTalkListData(3, 910000012, -1)
        # action:15000372:"Cancel"
        AddTalkListData(20, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            SetEventFlag(97011, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 2:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            SetEventFlag(97010, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 3:
            """State 14"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            SetEventFlag(97012, 1)
            assert t910000000_x5()
        elif GetEventFlag(1099000105):
            """State 5"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x3()
            """State 46"""
            return 0

def t910000000_x11():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000020, -1)
        AddTalkListData(2, 910000013, -1)
        AddTalkListData(3, 910000014, -1)
        AddTalkListData(4, 910000015, -1)
        # action:15000372:"Cancel"
        AddTalkListData(20, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            SetEventFlag(97020, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 2:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            SetEventFlag(97013, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 3:
            """State 14"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            SetEventFlag(97014, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 4:
            """State 16"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 17"""
            SetEventFlag(97015, 1)
            assert t910000000_x5()
        elif GetEventFlag(1099000105):
            """State 5"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x3()
            """State 46"""
            return 0

def t910000000_x12():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000017, -1)
        AddTalkListData(2, 910000016, -1)
        AddTalkListData(3, 910000018, -1)
        # action:15000372:"Cancel"
        AddTalkListData(20, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            SetEventFlag(97017, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 2:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            SetEventFlag(97016, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 3:
            """State 14"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            SetEventFlag(97018, 1)
            assert t910000000_x5()
        elif GetEventFlag(1099000105):
            """State 5"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x3()
            """State 46"""
            return 0

def t910000000_x13():
    """State 0"""
    while True:
        """State 1"""
        ClearTalkListData()
        ClearPreviousMenuSelection()
        """State 2"""
        AddTalkListData(1, 910000021, -1)
        AddTalkListData(2, 910000022, -1)
        AddTalkListData(3, 910000023, -1)
        AddTalkListData(4, 910000024, -1)
        AddTalkListData(5, 910000025, -1)
        AddTalkListData(6, 910000026, -1)
        AddTalkListData(7, 910000027, -1)
        # action:15000372:"Cancel"
        AddTalkListData(20, 15000372, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 4"""
        if GetTalkListEntryResult() == 1:
            """State 10"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 11"""
            SetEventFlag(97021, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 2:
            """State 12"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 13"""
            SetEventFlag(97022, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 3:
            """State 14"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 15"""
            SetEventFlag(97023, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 4:
            """State 16"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 17"""
            SetEventFlag(97024, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 5:
            """State 18"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 19"""
            SetEventFlag(97025, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 6:
            """State 20"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 21"""
            SetEventFlag(97026, 1)
            assert t910000000_x5()
        elif GetTalkListEntryResult() == 7:
            """State 22"""
            assert not (CheckSpecificPersonMenuIsOpen(22, 0) and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 23"""
            SetEventFlag(97027, 1)
            assert t910000000_x5()
        elif GetEventFlag(1099000105):
            """State 5"""
            assert t910000000_x5()
        else:
            """State 6,8"""
            assert t910000000_x3()
            """State 46"""
            return 0

