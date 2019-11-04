import socket
import predictor
import os, sys

service = ('localhost', 4444)

data=''

while True:
    try:
        if __name__ == "__main__":

            print('loading model')

            # load model config

            # load model entity
            pdt = predictor.Predictor(sys.argv[1])
            # load infer batch(tied with cpu)i
            # create a socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # bind
            #sock.settimeout(15)
            sock.bind(service)
            # socket, start to listen
            sock.listen(64)
            while True:
                # receieve data#print('reading data')
                print('listening')


                con, meat = sock.accept()
                data=''
                input_texts = []

                while True:
                    buff=con.recv(4096)
                    if buff:
                        #print('\n',buff[-4:], '\n')
                        if buff[-4:] == b'\x02\x02\x02\x02':
                            data+=buff[:-4].decode("utf-8", "ignore")
                            break
                        data+=buff.decode("utf-8", "ignore")
                        #con.sendall(buff)
                    else:
                        break
                tag=False
                data=data.split('\n')
                if len(data) < 0:
                    con.close()
                    continue
                elif len(data) == 1:
                    data = [data[0], data[0]]
                    tag=True
                for line in data:
                    input_texts.append(line.strip("\n"))
                print('predicting')
                predict_label_namez=pdt.predict_batch(input_texts)
                if tag:
                    con.sendall([predict_label_namez[0]].__str__().encode('utf-8'))
                else:
                    con.sendall(predict_label_namez.__str__().encode('utf-8'))
                con.close()
    except Exception as E:
            print('socket server:', data, E, 'restarting')
            

