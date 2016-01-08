import os, sys

startString = 'XEW' # the string that a valid Xcom Enemu Within folder must start with
connector = ' - ' # the connector between startString and mod name

launcherFolderName = '.XCOMLauncher'
launcherFolderPath = os.path.join(os.getcwd(), launcherFolderName)

dataFileName = 'folders'
dataFilePath = os.path.join(launcherFolderPath, dataFileName)

currentFolderFileName = 'current'
currentFolderFilePath = os.path.join(launcherFolderPath, currentFolderFileName)

currentMod = ''
modsList = []

def IsXcomFolder(name):
    '''
    Checks if the folder by the name is a valid Xcom Enemy Within folder (starts with XEW)
    Returns true if it is a valid folder, false otherwise
    '''
    
    if name[:len(startString)] == startString:
        return True
    else:
        return False

def scan():
    '''
    Scans the parent folder for directories which are Xcom directories and writes the directories to the data file.
    '''
    
    # filter out the folders into xcomDirectories
    dirObjs = os.listdir(os.getcwd())
    directories = filter(os.path.isdir, dirObjs)
    xcomDirectories = filter(IsXcomFolder, directories)

    # write to the data file in .XCOMLauncher 
    if not os.path.exists(launcherFolderPath):
        os.makedirs(launcherFolderPath)

    with open(dataFilePath, 'w') as dataFile:
        for xcomDir in xcomDirectories:
            # if the directory name is the default name (the one launched by steam) ...
            if xcomDir == 'XEW':
                # then ask the user for the name of the mod. This will be written as the current mod
                modName = raw_input('Detected default directory, please enter mod name: ')
                xcomDir = startString + connector + modName

                with open(currentFolderFilePath, 'w') as currentFile:
                    currentFile.write(xcomDir)
            
            dataFile.write(xcomDir + '\n')

def loadFolders():
    '''
    load the current folders into a list, as well as the currently loaded mod.
    '''
    global modsList
    global currentMod

    try:
        dataFile = open(dataFilePath, 'r')
    except IOError:
        scan()
        dataFile = open(dataFilePath, 'r')

    for line in dataFile:
        modsList += [line[:-1]] # stripping the last character (newline)
    print modsList

    dataFile.close()

    try:
        currentFile = open(currentFolderFilePath, 'r')
        for line in currentFile:
            currentMod = line
        currentFile.close()
    except IOError:
        currentMod = ''
        
    print currentMod

def PrettyFolderName(folderName):
    '''
    Returns a prettyified folderName.
    e.g., returns 'Long War' for 'XEW - Long War' if startString is 'XEW' and connector is ' - '
    '''

    return folderName[len(startString) + len(connector):]

def SwitchToMod(modName):
    '''
    Switches the folder layout of the parent folder to switch the default game folder (XEW) to match the mod named modName
    '''
    global currentMod

    if modName == currentMod:
        return # already on modName, no need to do anything
    elif currentMod != '':
        os.rename('XEW', currentMod)

    os.rename(modName, 'XEW')
    currentMod = modName
    with open(currentFolderFilePath, 'w') as currentFile:
        currentFile.write(currentMod)
    

def main():
    loadFolders()
        
    print 'What mod do you want to make default?'
    for i, mod in zip(range(len(modsList)), modsList):
        print i, PrettyFolderName(mod)

    modIndex = input()
    if not isinstance(modIndex, (int, long)) or modIndex >= len(modsList) or modIndex < 0:
        print 'Invalid mod, exiting...'
        sys.exit()
    else:
        SwitchToMod(modsList[modIndex])

if __name__ == '__main__':
    main()
