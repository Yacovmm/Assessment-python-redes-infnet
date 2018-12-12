import os

from psutil._compat import xrange


def get_files_by_file_size(dirname, reverse=False):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(filename)

    # Re-populate list with filename, size tuples
    for i in xrange(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(filepaths[i]))

    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in xrange(len(filepaths)):
        filepaths[i] = filepaths[i][0]

    return filepaths


def main():
    texto = ''

    for i in get_files_by_file_size(os.getcwd()):
        a = os.path.getsize(i)
        # print("Arquivo: {:>10}, tamanho: {:<5} \n".format(i, a))
        texto += "Arquivo: {:>10}, tamanho: {:<5}Bytes \n".format(i, a)

    arq = open("exericio3.txt", "w")
    arq.write(texto)
    arq.close()
    os.startfile('exericio3.txt')
    # print(get_files_by_file_size(os.getcwd()))


if __name__ == '__main__':
    main()
