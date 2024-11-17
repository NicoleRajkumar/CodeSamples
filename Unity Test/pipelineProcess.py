import time
import datetime
import sys
import os
import subprocess
import shutil
import glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import multiprocessing as mp
import urllib.request
import json
from multiprocessing import Process
from multiprocessing import Queue
from string import ascii_letters
import threading
from PIL import Image
from multiprocessing import Pool

class ImportSceneHandler(FileSystemEventHandler):

    def __init__(self, queue):
        self.queue = queue
        
    def process(self, event):
        self.queue.put(event)
        
    def on_created(self, event):
        self.process(event)
        now = datetime.datetime.utcnow()
       # if ".zip" in event.src_path:
        print ("{0} -- event {1} put in the queue ...".format(now.strftime("%Y/%m/%d %H:%M:%S"), event.src_path.replace("\\","/")))

def assetBuilder(event,base_dir):
    unity_location = r"C:\Program Files\Unity\Hub\Editor\2019.4.18f1\Editor\Unity.exe"
    
    #checking if input is a valid image file
    try:
        im = Image.open(event.src_path) 
    except IOError:
        print("filename is not a valid image file")
        return
    #grabbing necessary information
    size_variant_dest = base_dir + r"GluMobile\GluMobileUnityProject\Assets\Images"
    unity_project_path = base_dir + r"GluMobile\GluMobileUnityProject"
    img_name = event.src_path.replace("\\","/")
    img_name = img_name.split("/")[-1]
    img_name = img_name.split(".")[0]
    print(img_name)
    
    #requesting and loading JSON file
    with urllib.request.urlopen("https://space-stage.s3.amazonaws.com/ta-test-config.json") as url:
        data = json.loads(url.read().decode())
        
    config_info = list(data.values())[0]
    
    size_variants = config_info.get("target_sizes")
    file_format = config_info.get("format")
    bit_depth = config_info.get("bit_depth")


    #change the bit depth of inputted image
    mode = ""
    if bit_depth == 1:
        mode = "1"
    elif bit_depth == 8:
        mode = "P"
    elif bit_depth == 24:
        mode = "RGB"
    im2 = im.convert(mode)

    #save the different size variants into Unity project
    for size in size_variants:
        out = im2.resize((size,size))
        try:
            unity_dest = size_variant_dest + "\\" + img_name + "_" + str(size) + "." + file_format
            out.save(unity_dest,format =file_format)
        except OSError:
            print("cannot convert")

    #run assetbuilder c# script with Unity Batch Mode
    cmd = '"' + unity_location + '" -quit -batchmode -projectPath "' + unity_project_path + '" -executeMethod BuildAssetBundles.BuildABs'
    batcmd = 'cmd /c "' + cmd + '"'
    print(batcmd)
    result_code = os.system(batcmd)

    #clean up input and unity asset files
    os.remove(event.src_path)
    files = glob.glob(size_variant_dest + "\*")
    for f in files:
        os.remove(f)
    
    print("-------------------")

def process_load_queue(q, base_dir):
    while True:
        if not q.empty():
            pool = Pool(processes = 1, maxtasksperchild = 2)
            
            for i in range(4):
                if not q.empty():        
                    event = q.get()
                    pool.apply_async(assetBuilder, (event,base_dir))
            time.sleep(10)
            print ("closing  pool")
            pool.close()
            print( "closed pool")
            print( "joining pool")
            pool.join()
            print ("joined pool")
            time.sleep(5)
        else:
            time.sleep(1)

if __name__ == '__main__':

    importSceneQueue = Queue() # create queue
    observer = Observer()
    event_handler = ImportSceneHandler(importSceneQueue) # create event handler
    # set observer to use created handler in directory
    base_dir = r"C:\Users\Nicole\Documents\\"
    observer.schedule(event_handler, path= base_dir + r'GluMobile\input')
    observer.start()

    worker = threading.Thread(target = process_load_queue, args =(importSceneQueue,base_dir))
    worker.setDaemon(True)
    worker.start()

    # sleep until keyboard interrupt, then stop + rejoin the observer
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

