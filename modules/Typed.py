import os, time, sys

class Typed:
    def __init__(self, config):
        self.text = config["text"]
        self.speed = config["speed"]
        
    def run(self):
        characters = self.text.split()
        for character in characters:
            print(character, end=" ")
            sys.stdout.flush()
            time.sleep(self.speed)
        print("", end="\n")
        
        
"""
text = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laboriosam tempore modi porro recusandae rerum nisi consectetur ducimus cum ullam eligendi soluta velit corrupti saepe, eos vitae aperiam, numquam illo expedita."

typed = Typed({
  "text": text,
  "speed": .1
})

typed.run()
"""