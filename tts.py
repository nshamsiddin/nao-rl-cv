from naoqi import ALProxy
tts = ALProxy()
tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)
tts.say("Hello World!")