import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BHlnhYN7j-FZwOthOr0ikYjCHAK1H9OO-g0CRymazLLP0qMiPE5Ri3VvOKSaza3lwzNywPJGs2LGTY2FVXYYP-hTdLZ0goqc3eW5qcnSpR-Lkd1gjnpeVe8ptsEjYMa7fqTc9ME'
    transferData = TransferData(access_token)

    file_from = input("Enter Source File Path: ")
    file_to = input("Enter Full Path To Upload To Dropbox: ")

    transferData.upload_file(file_from, file_to)

    print("File Has Been Moved!")
main()