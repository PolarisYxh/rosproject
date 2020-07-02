import socket
from PIL import Image
import struct
class client:
    def __init__(self,server_ip,server_port):
        self.host_content=server_ip
        self.port_content=server_port

    def get_rgbd(self):
        host = self.host_content
        port = self.port_content
        s = socket.socket()
        s.connect((host, int(port)))
        self.num=0.000000
        #get intrinsic
        s.send('intrinsic'.encode('utf-8'))
        #s.send(bytes('intrinsic', encoding='utf-8'))
        str1=s.recv(60)#60个字节
        data = bytearray(str1)
        headIndex = data.find(b'\xff\xaa\xff\xab')
        print(headIndex)
        if headIndex == 0:
            print(2)
            width,height= struct.unpack('ii',str1[4:12])
            pMtr=struct.unpack('%df'%((len(str1)-12)/4),str1[12:])
            print(height)
            print(width)
            print(pMtr)
            #get rgbd
            while True:
                #s.send(bytes('rgbd', encoding='utf-8'))
                str1 = s.recv(8)
                # head check
                data = bytearray(str1)
                headIndex = data.find(b'\xff\xaa\xff\xaa')
                if headIndex == 0:
                    allLen = struct.unpack('i',str1[4:8])
                    curSize = 0
                    allData = b''
                    # get rgb
                    while curSize < allLen:
                            data = s.recv(4)
                            allData += data
                            curSize += len(data)
                    rgbData = allData[0:]
                    str1 = s.recv(4)
                    data = bytearray(str1)
                    allLen = int.from_bytes(data[0:4], byteorder='little')
                    curSize = 0
                    allData = b''
                    # get depth
                    while curSize < allLen:
                            data = s.recv(1024)
                            allData += data
                            curSize += len(data)
                    depthData = allData[0:]

                    # bytes to PIL.Image
                    img = Image.frombuffer('RGB', (640, 480), rgbData)
                    # top and down flip
                    img = img.transpose(Image.FLIP_TOP_BOTTOM)
                    #save
                    name='%f' %self.num
                    img.save('/home/yxh/'+name+'./jpg')
                    # PIL.Image to ndarray
                    #img_conv = np.asarray(img)

                    img = Image.frombuffer('RGB', (640, 480), depthData)

                    img = img.transpose(Image.FLIP_TOP_BOTTOM)
                    #save
                    img.save('/home/yxh/'+name+'./jpg')
                    # PIL.Image to ndarray
                    #img_conv = np.asarray(img)
                    self.num+=0.000001
                    # qimage = QImage(img_conv, 640, 480, QImage.Format_RGB888)
                    # pixmap = QPixmap.fromImage(qimage)
                    # #
                    # self.dis_update.emit(pixmap)

if __name__ == "__main__":
    rgbdclient=client('localhost','9090')
    rgbdclient.get_rgbd()