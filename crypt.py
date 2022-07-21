# Import necessary modules
from pyAesCrypt import encryptFile, decryptFile
from os.path import exists as fexists
from os import remove

# Define error messages
errorMsg001 = 'ERROR: File no filename provided.'
errorMsg002 = "ERROR: File ({}) does not exists."
errorMsg003 = 'ERROR: File ({}) already exists.'
errorMsg004 = 'ERROR: No password for encryption provided.'

# Use this function to check if a file exists or not
def fileExists(fname = None):
    if (fname is None):
        print(errorMsg001)

    else:
        return(fexists(fname))

# Encrypt file
#    infile := file to be encrypted
#    outfile := encrypted filename
#    password := what password are we going to use
#    keep := do we keep infile or delete it after encrypting it (default := True)
def encryptFile(infile: str = None, outfile: str = None, password: str = None, keep: bool = True):
    if ((fileExists(infile)) and (not fileExists(outfile)) and (password is not None)):
        encryptFile(infile, outfile, password)

        # Delete infile if we are not going to keep it.
        if(not keep):
            remove(infile)
        
        return(True)

    else:
        if(not fileExists(infile)):
            print(errorMsg002.format(infile))

        if(fileExists(outfile)):
            print(errorMsg003.format(outfile))

        if (password is  None):
            print(errorMsg004)

        return(False)

# Decrypt file
#    infile := file to be decrypted
#    outfile := decrypted filename
#    password := what password are we going to use
#    keep := do we keep infile or delete it after encrypting it (default := True)
def decryptFile(infile = None, outfile = None, password = None, keep: bool = True):
    if ((fileExists(infile)) and (not fileExists(outfile)) and (password is not None)):
        decryptFile(infile, outfile, password)

        # Delete infile if we are not going to keep it.
        if(not keep):
            remove(infile)

        return(True)

    else:
        if(not fileExists(infile)):
            print(errorMsg002.format(infile))

        if(fileExists(outfile)):
            print(errorMsg003.format(outfile))

        if (password is  None):
            print(errorMsg004)

        return(False)