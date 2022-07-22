# Import necessary modules
from pyAesCrypt import encryptFile, decryptFile
from os.path import exists as fexists
from os import remove

# Define error messages
errorMsg001 = 'ERROR: File no filename provided.'
errorMsg002 = "ERROR: File ({}) does not exists."
errorMsg003 = 'ERROR: File ({}) already exists.'
errorMsg004 = 'ERROR: No password for encryption provided.'

def fileExists(fname: str = None):
    """
    This function checks if the file name given in fname exists or not

    :param str fname: file name to check
    """
    if (fname is None):
        print(errorMsg001)

    else:
        return(fexists(fname))

def encryptFile(infile: str = None, outfile: str = None, password: str = None, keep: bool = True):
    """
    Function to encrypt a file

    :param str infile   : file to be encrypted
    :param str outfile  : encrypted filename
    :param str password : what password are we going to use to encrypt the file
    :param bool keep    : do we keep infile or delete it after encrypting it (default := True)
    """
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

def decryptFile(infile = None, outfile = None, password = None, keep: bool = True):
    """
    Function to decrypt a file

    :param str infile   : file to be decrypted
    :param str outfile  : decrypted filename
    :param str password : what password are we going to use to decrypt the file
    :param bool keep    : do we keep infile or delete it after encrypting it (default := True)
    """
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