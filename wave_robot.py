from waveapi import events
from waveapi import model
from waveapi import robot
from waverpg import *

def OnRobotAdded(properties, context):
  """Invoked when the robot has been added."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("For more information on using RPG Buddy, see http://rpgbuddy.appspot.com/.")

def OnBlipSubmitted(properties, context):
  blip = context.GetBlipById(properties['blipId'])
  waveId = blip.GetWaveId()
  waveletId = blip.GetWaveletId()
  text = blip.GetDocument().GetText()
  newtext = process_text(text)
  blip.GetDocument().SetText(" ")
  context.builder.DocumentAppendMarkup(waveId, waveletId, blip.GetId(), newtext)
  
if __name__ == '__main__':
  myRobot = robot.Robot('RPG Buddy', 
      image_url='http://rpgbuddy.appspot.com/dice.gif',
      version='3',
      profile_url='http://rpgbuddy.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()
