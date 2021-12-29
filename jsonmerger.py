import json
import os
import pandas as pd


def debugMessage(text):
    print('===> : ', text)


def genFileList(fp):
    fplist = [os.path.join(fp, i) for i in os.listdir(
        fp) if os.path.splitext(i)[1] == '.json']
    # debugMessage(fplist)
    return fplist


def mergeJsons(fp=None, outpath=None):
    '''input json folder directory, returns merge
    '''
    files = genFileList(fp)
    jsonList = []
    # debugMessage(files)
    for i in range(len(files)):
        with open(files[i], encoding='UTF-8') as f1:
            data1 = json.load(f1)
            jsonList.append(data1)

    if not outpath:
        outpath = 'master-traits.json'
    with open(outpath, 'w') as jf:
        json.dump(jsonList, fp=jf, indent=4)


if __name__ == '__main__':
    try:
        while True:
            filePath = input('Enter folder to merge JSONs:\n\t')
            if not os.path.isdir(filePath):
                continue
            outpath = input('..Enter an output file name:\n\t')
            if not outpath.endswith('.json'):
                debugMessage('No JSON in filename, added')
                outpath = outpath + '.json'
            mergeJsons(filePath, outpath)
            debugMessage('JSONs merged!')
    except KeyboardInterrupt:
        input('QUITTING, press enter to continue')
