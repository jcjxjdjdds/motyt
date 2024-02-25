from MatrixMusic.core.bot import Zelzaly
from MatrixMusic.core.dir import dirr
from MatrixMusic.core.git import git
from MatrixMusic.core.userbot import Userbot
from MatrixMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Zelzaly()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()