from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyJukeboxActivityBaseAI import DistributedPartyJukeboxActivityBaseAI

class DistributedPartyValentineJukebox40ActivityAI(DistributedPartyJukeboxActivityBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyValentineJukebox40ActivityAI")

