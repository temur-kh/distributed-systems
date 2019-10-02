import sys, os
import socket
from threading import Thread


def send_file(filename, address, port):
    """
    Send a file to address:port
    :param filename: name of a file to be sent
    :param address: address of destination (IP or domain name)
    :param port: port of destination
    :return: None
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((address, port))
        if os.path.isfile(filename):
            # send size of a filename and the filename itself
            s.sendall(len(filename).to_bytes(1, 'big'))
            s.sendall(str(filename).encode())
            # the size of a file used for percentage bar
            file_size = os.path.getsize(filename)
            send_size = 0
            with open(filename, "rb") as file:
                while True:
                    print(f"{send_size} of {file_size} bytes sent - {send_size * 100 / file_size :.2f}% done")
                    # read at most 1024 bytes of a file if not EOF
                    buf = file.read(1024)
                    if not buf:
                        break
                    # send bytes through socket
                    s.sendall(buf)
                    send_size += len(buf)
            print("The file sending is finished!")
        else:
            print("This is not a file!")


if __name__ == "__main__":
    args = sys.argv[1:]
    filename, address, port = args
    # create a separate thread for sending a file
    thread = Thread(target=send_file, args=(filename, address, int(port)))
    thread.start()
    thread.join()
    print("The task was done!")
