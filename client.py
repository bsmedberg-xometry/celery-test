import tasks
import time

r = tasks.add.delay(2, 17)
while True:
    ready = r.ready()
    print "ready?", ready
    if ready:
        break
    time.sleep(0.1)

print "result", r.get()

print "throwing"
r = tasks.div.delay()
print "result", r.get()
