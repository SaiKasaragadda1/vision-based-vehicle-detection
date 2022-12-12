import cv2

def extractFrames(pathIn):
   
   ca= cv2.VideoCapture(pathIn)
    
   count = 0
   while (ca.isOpened()):
       ret, frame = ca.read()
       if ret == True:
           
           print('Read %d frame: ' % count, ret)
           cv2.imwrite("D:/codes/traffic_signal_control/{:d}.png".format(count), frame) 
           count += 1
       else:
           break
def main():
   extractFrames('D:/codes/vehicle_detection_haarcascades-master/dataset/video1.avi')
   
if __name__=='__main__':
    main()





