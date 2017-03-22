#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: gathering-images-for-haar-cascade.py

import urllib.request
import os
import numpy as np
import cv2


def store_raw_images(images_link, file_type, shape):

    proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:10801'})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    images_urls = urllib.request.urlopen(images_link).read().decode()

    pic_num = 1064

    if not os.path.exists(file_type):
        os.makedirs(file_type)

    for url in images_urls.split('\n'):
        try:
            print(url)
            image_path = file_type + '/' + str(pic_num) + '.jpg'

            with open(image_path, "wb") as f:
                f.write(urllib.request.urlopen(url).read())

            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, shape)
            cv2.imwrite(image_path, resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))


def find_uglies():
    for file_type in ['pos', 'neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    ugly = cv2.imread('uglies/' + str(ugly))
                    question = cv2.imread(current_image_path)
                    if (ugly.shape == question.shape and
                        (not (np.bitwise_xor(ugly, question).any()))):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


def create_pos_n_neg():
    for file_type in ['pos', 'neg']:
        for img in os.listdir(file_type):
            if file_type == 'pos':
                line = file_type + '/' + img + ' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)


# neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
# neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
pos_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n13914608'

# should be larger than samples / pos pic (so we can place our image on it)
# store_raw_images(neg_images_link, 'neg', (100, 100))
# store_raw_images(pos_images_link, 'pos', (50, 50))

# find_uglies()

create_pos_n_neg()
