from xCore import xCore
from xOC01 import xOC01

OC01 = xOC01()

while True:
    OC01.digitalWrite(OC01.OUT0, True)
    xCore.sleep(500)
    OC01.digitalWrite(OC01.OUT0, False)
    xCore.sleep(500)