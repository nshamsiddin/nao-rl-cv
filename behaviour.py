from naoqi import ALProxy

# tts
# tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
# tts.say("Hello World!")

# motion
motion = ALProxy("ALMotion", "127.0.0.1", 9559)
motion.setStiffnesses("Body", 1.0)
motion.post.moveTo(-1.0, 0.0, 0.0)
