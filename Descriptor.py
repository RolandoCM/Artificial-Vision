import cv2
import numpy as np
from matplotlib import pyplot as plt

# method for save in archive
def save_descriptor():
    global arch, arch2
    global des
    for j in xrange(des.shape[0]):
        for ka in xrange(des.shape[1]):
            arch.write(str(des[j, ka]) + ',')
        arch.write(id_exit)
    arch2.write(str(des.shape[0])+'\n')

arch2 = open('file.csv', 'a')
def object_name():
    global name
    global id_exit
    global ob
    ob = input('select a object: ')

    if ob == 0:
        # nutella
        name = "objeto0"
        id_exit = "1,0,0,0,0,0\n"
    if ob == 1:
        # coffeemate
        name = "objeto1"
        id_exit = "0,1,0,0,0,0\n"
    if ob == 2:
        # svetia
        name = "objeto2"
        id_exit = "0,0,1,0,0,0\n"
    if ob == 3:
        # desodorante
        name = "objeto3"
        id_exit = "0,0,0,1,0,0\n"
    if ob == 4:
        # desodorante spray
        name = "objeto4"
        id_exit = "0,0,0,0,1,0\n"
    if ob == 5:
        # coffee
        name = "objeto5"
        id_exit = "0,0,0,0,0,1\n"


size = 2
step = 1
separate = True
name = "nothing"

# create instance of sift
sift = cv2.xfeatures2d.SIFT_create(100)

# kernel selection
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

for ob in range(0, 1):

    object_name()
    print name
    # images
    nb = 1 + ob * 3 * 74

    if size == 1:
        ni = nb + 1
        nf = ni + 72
    if size == 2:
        ni = nb + 74 +1
        nf = ni + 74 * 2 - 2
    if size == 3:
        ni = nb + 74*2 + 1
        nf = ni + 74 * 3 - 2

    # background image
    bgImg = cv2.imread('database/img' + str(nb) + '.png')
    c = 2

    # open new archive
    arch = open('descriptors/evaluate/100/' + name + '.csv', 'w')

    for i in range(ni, nf):
        print i
        if i >= nb + 74:
            nb = nb + 74
            bgImg = cv2.imread('database/img' + str(nb) + '.png')
            # print 'nb = %d' % (nb)

            if separate:
                arch.close()
                arch = open('descriptors/evaluate/100/' + name + str(c) + '.csv', 'w')
                c = c + 1

        print ('nb = %d' % nb)

        # read image
        fgImg = cv2.imread('database/img' + str(i) + '.png')

        # convert image to scale of gray
        gray = cv2.cvtColor(fgImg, cv2.COLOR_BGR2GRAY)

        dif = cv2.subtract(bgImg, fgImg)
        fgMask = np.uint8(dif.max(2) > 40)

        # detect keypoints in the image and use of mask for only a part of image
        # and detect descriptor
        # kp in a list of keypoints and des is a numpy array (number of keypoints * 128)
        kp, des = sift.detectAndCompute(gray, fgMask)
        # save points
        save_descriptor()
        bgMask = np.uint8(fgMask != 1)

        img = cv2.drawKeypoints(gray, kp, fgImg)
        cv2.imwrite('sift_keypoints.jpeg', img)

        # show frame of images
        cv2.imshow('mask', fgMask)
        cv2.imshow('foreground', fgMask * 255)
        cv2.imshow('background', bgMask * 255)
        cv2.imshow('dif', dif)
        cv2.imshow('img', fgImg)

        # calculate the absolute difference between tho arrays
        obj = cv2.bitwise_and(fgImg, fgImg, mask=fgMask)
        cv2.imshow('obj', obj)
        # cv2.imshow('img', cv2.drawKeypoints(fgImg, kp))

        # exit program
        k = cv2.waitKey(500) & 0xff
        if k == 27:
            break
# close instance of cv2 and all the window
cv2.destroyAllWindows()
# close archive
arch.close()
arch2.close()