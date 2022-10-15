import ftplib
import os

def uploadFileToFtp(localFilePath, ftpHost, ftpPort, ftpUname, ftpPass, remoteWorkingDirectory):
    # initialize the flag that specifies if upload is success
    isUploadSuccess: bool = False

    # extract the filename of local file from the file path
    _, targetFilename = os.path.split(localFilePath)

    # create an FTP client instance, use the timeout parameter for slow connections only
    ftp = ftplib.FTP(timeout=30)

    # connect to the FTP server
    ftp.connect(ftpHost, ftpPort)

    # login to the FTP server
    ftp.login(ftpUname, ftpPass)

    # change current working directory if specified
    if not (remoteWorkingDirectory == None or remoteWorkingDirectory.strip() == ""):
        _ = ftp.cwd(remoteWorkingDirectory)

    # Read file in binary mode
    with open(localFilePath, "rb") as file:
        # upload file to FTP server using storbinary, specify blocksize(bytes) only if higher upload chunksize is required
        retCode = ftp.storbinary(f"STOR {targetFilename}", file, blocksize=1024*1024)

    # send QUIT command to the FTP server and close the connection
    ftp.quit()

    # check if upload is success using the return code (retCode)
    if retCode.startswith('226'):
        isUploadSuccess = True

    # return the upload status
    return isUploadSuccess

# connection parameters
ftpHost = '192.168.18.6'
ftpPort = 21
ftpUname = 'Usuario1'
ftpPass = 'aivocado'
remoteFolder = "/"

# upload file
for i in range(9):
    localFile = 'AivocadoCamera\p'+str(i)+'.jpg'
    isUploadSuccess = uploadFileToFtp(localFile, ftpHost, ftpPort, ftpUname, ftpPass, remoteFolder)
    print("upload status = {0}".format(isUploadSuccess))