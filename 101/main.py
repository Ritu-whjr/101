import dropbox as db
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=db.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)
def main():
    # change access_token to your own access token
    access_token = 'sl.BIr95z_b_G0laTY3j-_ca8zOLITivdB3xaGBxPvG3hw9aZYKOSHDPbcdk1ADElHwGBqeDL9Vf3YGpKb4vGECPhMW0qZXJTPdUqQFk5JWR_eCtBa_lp0oXJGsy6bQjiL6NyCT3VwmIUxV'
    transferData= TransferData(access_token)
   # change file path to your own file path. Can also use input() to get user input for file path
    file_from='test.txt'
    # change file path to your liking . Can also use input() to get user input for file path
    file_to='/testcheck.txt'
    print(transferData.upload_file(file_from,file_to))

if __name__=='__main__':
     main()