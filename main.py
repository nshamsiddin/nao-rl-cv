# http://doc.aldebaran.com/2-1/dev/python/reacting_to_events.html
# http://doc.aldebaran.com/2-1/index.html
from naoqi import ALProxy

# tts
# tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
# tts.say("Hello World!")

# motion
motion = ALProxy("ALMotion", "127.0.0.1", 9559)
# motion.setStiffnesses("Body", 1.0)

print(motion.__getattribute__("Stiffnesses"))


motion.post.moveTo(0.0, 0.0, 3.0)
