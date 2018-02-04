# Copyright (c) Microsoft. All rights reserved.

# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

from __future__ import print_function
import zipfile
import os, sys, time
from sys import platform
import shutil

try:
    from urllib.request import urlretrieve 
except ImportError: 
    from urllib import urlretrieve


def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def save(url, filename):
    urlretrieve(url, filename, reporthook)

def download_beverage_models():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    model_folder = os.path.join(base_folder, "models")
    if not os.path.exists(model_folder):
        os.makedirs(model_folder)

    if not os.path.exists(os.path.join(model_folder, "models")):
        filename = os.path.join(model_folder, "cntk_models.zip")
        if not os.path.exists(filename):
            url = "https://computervisionworkshop.blob.core.windows.net/models/cntk_models.zip"
            print('Downloading data from ' + url + '...')
            save(url, filename)
        try:
            print('Extracting ' + filename + '...')
            with zipfile.ZipFile(filename) as myzip:
                myzip.extractall(model_folder)
        finally:
            os.remove(filename)
        print('Done.')
    else:
        print('Data already available at ' + model_folder)

def download_beverage_data():
    base_folder = os.path.dirname(os.path.abspath(__file__))
    dataset_folder = os.path.join(base_folder, "dataset")
    if not os.path.exists(dataset_folder):
        os.makedirs(dataset_folder)

    if not os.path.exists(os.path.join(dataset_folder, "Beverages")):
        filename = os.path.join(dataset_folder, "Beverages.zip")
        if not os.path.exists(filename):
            url = "https://computervisionworkshop.blob.core.windows.net/dataset/Beverages.zip"
            print('Downloading data from ' + url + '...')
            save(url, filename)
        try:
            print('Extracting ' + filename + '...')
            with zipfile.ZipFile(filename) as myzip:
                myzip.extractall(dataset_folder)
            # if platform != "win32":
            #     testfile  = os.path.join(dataset_folder, "Beverages", "test.txt")
            #     unixfile = os.path.join(dataset_folder, "Beverages", "test_unix.txt")
            #     out = open(unixfile, 'w')
            #     with open(testfile) as f:
            #         for line in f:
            #             out.write(line.replace('\\', '/'))
            #     out.close()
            #     shutil.move(unixfile, testfile)
        finally:
            os.remove(filename)
        print('Done.')
    else:
        print('Data already available at ' + dataset_folder + '/Grocery')
    
if __name__ == "__main__":
    download_beverage_data()
    download_beverage_models()