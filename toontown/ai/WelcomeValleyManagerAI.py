<<<<<<< HEAD
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class WelcomeValleyManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("WelcomeValleyManagerAI")

    def clientSetZone(self, todo0):
        pass

    def requestZoneIdMessage(self, todo0, todo1):
        pass

    def requestZoneIdResponse(self, todo0, todo1):
        pass

=======
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class WelcomeValleyManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("WelcomeValleyManagerAI")

    def clientSetZone(self, todo0):
        pass

    def requestZoneIdMessage(self, todo0, todo1):
        pass

    def requestZoneIdResponse(self, todo0, todo1):
        pass

>>>>>>> 30847815294dd00139dc93e7849d6bffd935eca9
