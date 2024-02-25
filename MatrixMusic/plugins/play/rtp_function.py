from database import get_db_constractors, get_db_manager, get_db_admin, get_db_special, get_db_general_rtb
from config import developer


def sudo(m):
    leader = False
    try:
        for per in sudoers:
            if m.from_user.id == per:
                leader = True
    except Exception as e:
        print("sudo " + str(e))

    return leader


def secsudo(m):
    leader = False
    lang = get_db_general_rtb("secdeveloper")
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[0]:
                    leader = True
        except Exception as e:
            print("genspecial " + str(e))
    if leader or sudo(m):
        leader = True
    else:
        leader = False
    return leader


def sudo2(m):
    leader = False
    if developer is None:
        leader = False
    else:
        try:
            for per in developer:
                if m.from_user.id == per:
                    leader = True
        except Exception as e:
            print("sudo2 " + str(e))

    if leader or sudo(m) or secsudo(m):
        leader = True
    else:
        leader = False
    return leader


def genspecial(m):
    leader = False
    lang = get_db_general_rtb("genspecial")
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[0]:
                    leader = True
        except Exception as e:
            print("genspecial " + str(e))

    return leader


def manager(m):
    leader = False
    lang = get_db_manager(m.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("manager " + str(e))
    if leader or sudo(m) or secsudo(m) or sudo2(m):
        leader = True
    else:
        leader = False
    return leader


def constractors(m):
    leader = False
    lang = get_db_constractors(m.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("constractors " + str(e))
    if leader or sudo(m) or secsudo(m) or sudo2(m) or manager(m):
        leader = True
    else:
        leader = False
    return leader


def admin(m):
    leader = False
    lang = get_db_admin(m.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("admin " + str(e))
    if leader or sudo(m) or secsudo(m) or sudo2(m) or manager(m) or constractors(m):
        leader = True
    else:
        leader = False
    return leader


def special(m):
    leader = False
    lang = get_db_special(m.chat.id)
    if lang is None:
        leader = False
    else:
        try:
            for per in lang:
                if m.from_user.id == per[1]:
                    leader = True
        except Exception as e:
            print("special " + str(e))
    if leader or sudo(m) or secsudo(m) or sudo2(m) or manager(m) or constractors(m) or admin(m):
        leader = True
    else:
        leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def get_Rank(m):
    leader = "عضو"
    if m.from_user.id == 6373798952:
        leader = "Dev 🎖"
    else:
        if m.from_user.id == 6516751434:
            leader = "Dev² 🎖"
        else:
            if sudo(m):
                leader = "مطور اساسي"
            else:
                if secsudo(m):
                    leader = "مطور ثانوي"
                else:
                    if sudo2(m):
                        leader = "مطور"
                    else:
                        if genspecial(m):
                            leader = "مميز عام"
                        else:
                            if manager(m):
                                leader = "oWnEr 🎖"
                            else:
                                if constractors(m):
                                    leader = "منشئ"
                                else:
                                    if admin(m):
                                        leader = "ادمن"
                                    else:
                                        if special(m):
                                            leader = "مميز"

    return leader


########################################################################################################################
########################################################################################################################

def sudooo(u):
    leader = False
    for per in sudoers:
        if u == per:
            leader = True
    return leader


def secsudooo(u):
    leader = False
    lang = get_db_general_rtb("secdeveloper")
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[0]:
                leader = True
    if leader or sudooo(u):
        leader = True
    else:
        leader = False
    return leader


def sudooo2(u):
    leader = False
    if developer is None:
        leader = False
    else:
        for per in developer:
            if u == per:
                leader = True
    if leader or sudooo(u) or secsudooo(u):
        leader = True
    else:
        leader = False
    return leader


def genspecialll(u):
    leader = False
    lang = get_db_general_rtb("genspecial")
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[0]:
                leader = True
    return leader


def managerrr(u, m):
    leader = False
    lang = get_db_manager(m.chat.id)
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[1]:
                leader = True
    if leader or sudooo(u) or secsudooo(u) or sudooo2(u):
        leader = True
    else:
        leader = False
    return leader


def constractorsss(u, m):
    leader = False
    lang = get_db_constractors(m.chat.id)
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[1]:
                leader = True
    if leader or sudooo(u) or secsudooo(u) or sudooo2(u) or managerrr(u, m):
        leader = True
    else:
        leader = False
    return leader


def adminnn(u, m):
    leader = False
    lang = get_db_admin(m.chat.id)
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[1]:
                leader = True
    if leader or sudooo(u) or secsudooo(u) or sudooo2(u) or managerrr(u, m) or constractorsss(u, m):
        leader = True
    else:
        leader = False
    return leader


def specialll(u, m):
    leader = False
    lang = get_db_special(m.chat.id)
    if lang is None:
        leader = False
    else:
        for per in lang:
            if u == per[1]:
                leader = True
    if leader or sudooo(u) or secsudooo(u) or sudooo2(u) or managerrr(u, m) or constractorsss(u, m) or adminnn(u, m):
        leader = True
    else:
        leader = False
    return leader


########################################################################################################################
########################################################################################################################

async def get_Rankkk(u, m):
    leader = "عضو"
    if u == 6373798952:
        leader = "Dev 🎖"
    else:
        if u == 6516751434:
            leader = "Dev² 🎖"
        else:
            if sudooo(u):
                leader = "مطور اساسي"
            else:
                if secsudooo(u):
                    leader = "مطور ثانوي"
                else:
                    if sudooo2(u):
                        leader = "مطور"
                    else:
                        if genspecialll(u):
                            leader = "مميز عام"
                        else:
                            if managerrr(u, m):
                                leader = "oWnEr 🎖"
                            else:
                                if constractorsss(u, m):
                                    leader = "منشئ"
                                else:
                                    if adminnn(u, m):
                                        leader = "ادمن"
                                    else:
                                        if specialll(u, m):
                                            leader = "مميز"

    return leader


########################################################################################################################
########################################################################################################################

async def get_Rank_ana_meen(m):
    leader = "عضو"
    if m.from_user.id == 6373798952:
        leader = "Dev 🎖"
    else:
        if m.from_user.id == 6516751434:
            leader = "Dev² 🎖"
        else:
            if sudo(m):
                leader = "مطور اساسي"
            else:
                if secsudo(m):
                    leader = "مطور ثانوي"
                else:
                    if sudo2(m):
                        leader = "مطور"
                    else:
                        if genspecialll(m):
                            leader = "مميز عام"
                        else:
                            if manager(m):
                                leader = "oWnEr 🎖"
                            else:
                                if constractors(m):
                                    leader = "منشئ"
                                else:
                                    if admin(m):
                                        leader = "ادمن"
                                    else:
                                        if special(m):
                                            leader = "مميز"

    return leader


########################################################################################################################
########################################################################################################################

async def get_available_creator(c, m):
    creatorcheck = False
    creatorname = "لايوجد"
    creatorid = 0
    async for creator in c.iter_chat_members(m.chat.id, filter="Administrators"):
        if creator.status == "creator":
            creatorname = creator.user.first_name
            creatorid = creator.user.id
            if m.from_user.id == creator.user.id:
                creatorcheck = True

    return creatorcheck, creatorname, creatorid

########################################################################################################################
########################################################################################################################
