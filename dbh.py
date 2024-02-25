import sqlite3

dbGeneral = sqlite3.connect("leomedo.db")
dbcGeneral = dbGeneral.cursor()

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS groups (chat_id INTEGER PRIMARY KEY,
                                                  welcome,
                                                  welcome_enabled INTEGER,
                                                  rules,
                                                  goodbye,
                                                  goodbye_enabled INTEGER,
                                                  warns_limit INTEGER,
                                                  chat_lang,
                                                  start,
                                                  cached_admins)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY,
                                                 start,
                                                 chat_lang)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS channels (chat_id INTEGER PRIMARY KEY)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS generalban (user_id INTEGER PRIMARY KEY,
                                                 firstname)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS generalmute (user_id INTEGER PRIMARY KEY,
                                                 firstname)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS generalreply (text, reply)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS wait (key,
                                                 user_id INTEGER, chat_id INTEGER)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS waitg (key,
                                                 gamekey, chat_id INTEGER)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS botname (name)""")

##################################################################################
##################################################################################

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS ban (user_id,
                                                 firstname, chat_id INTEGER)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mute (user_id,
                                                 firstname, chat_id INTEGER)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS priban (user_id,
                                                 firstname, chat_id INTEGER)""")

##################################################################################
##################################################################################

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS groupcheck (key, chat_id, name)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS usercheck (key, user_id, name)""")

##################################################################################
##################################################################################

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS developer (user_id INTEGER PRIMARY KEY,
                                                     firstname)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS secdeveloper (user_id INTEGER PRIMARY KEY,
                                                     firstname)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS genspecial (user_id INTEGER PRIMARY KEY,
                                                     firstname)""")

##################################################################################
##################################################################################

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS manager (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS constructor (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS admin (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS special (firstname,
                                                        user_id, chat_id)""")

#################################################################################
#################################################################################

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS replygroup (text, reply, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locktext (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockmnshn (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locklink (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locklinkban (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locklinkmute (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockphoto (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockvideo (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locksticker (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockanimation (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockaudio (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockvoice (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockforward (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockforwardban (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockforwardmute (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockdocument (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockcontact (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockreply (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockfshar (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockfsharban (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockfsharmute (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockzhrafa (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockmusic (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockaflam (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockyoutube (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locktranslate (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS blocktext (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS blocktextban (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS blocktextmute (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locknotification (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockupper (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockazkar (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockazkar2 (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockgames (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locktag (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockdeletelink (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockkickme (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockmeendafny (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockrwayat (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS kickbotatban (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS namemeaning (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS abrag (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locklinggroup (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS idgroup (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS myphoto (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS entrygp (key, chat_id)""")

#################################################################################
#################################################################################

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locksendmsg (key)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockbroadcast (key)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockgenyoutube (key)""")

#################################################################################
#################################################################################

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS addlinkgroup (link, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockwelcome (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS addwelcomegroup (welcome, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lockbye (key, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS addbyegroup (bye, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS addcomand (command, newcommand, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS addcustomid (customid, chat_id)""")

#################################################################################
#################################################################################


dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS lonely (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS caw (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS stupid (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS donkey (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS dog (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS monkey (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS hours (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS naked (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mywife (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS myheart (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS bestfriend (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS abit (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS abny (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS bnty (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS dakry (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS fashel (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS hyawan (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS khain (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS khaina (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS khazok (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mohzaa (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS otty (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS rkasa (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS wtka (firstname,
                                                        user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS zogy (firstname,
                                                        user_id, chat_id)""")

#################################################################################
#################################################################################

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS meendafny (user_id_add INTEGER, firstname_add,
                                                 user_id_added INTEGER, chat_id INTEGER)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mycontact (counter INTEGER, user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mypointgame (counter INTEGER, user_id, chat_id)""")

dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mymessage (counter INTEGER, user_id, chat_id)""")

##################################################################################
##################################################################################


dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS was_restarted_at (chat_id INTEGER,
                                                            message_id INTEGER)""")

dbGeneral.commit()
