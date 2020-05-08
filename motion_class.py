from naoqi import ALProxy

motion = ALProxy("ALMotion", "127.0.0.1", 9559)
# motion.setStiffnesses("Body", 1.0)

print(motion.__getattribute__("Stiffnesses"))


motion.post.moveTo(0.0, 0.0, 3.0)
