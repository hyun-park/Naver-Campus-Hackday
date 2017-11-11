import voice_detect as vd
import google_client as gc

while True:
    vd.record_to_file('output.wav')
    gc.recognition()