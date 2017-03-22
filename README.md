# OpenCV-with-Python

## Cascade training set from a single image

### Creating training set from a single image

Directory structure:

```
gathering-images-for-haar-cascade
--info
--neg
----negimages.jpg
--bg.txt
--rubik.jpg
```

run `create_pos_n_neg()`

File bg.txt:

```
neg/2035.jpg
neg/2254.jpg
...
```

For example, with the opencv_createsamples called as following:

```
opencv_createsamples -img rubik.jpg -bg bg.txt -info info/info.lst -pngoutput -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
```

The output will have the following structure:

```
gathering-images-for-haar-cascade
--info
----posimages.jpg
----info.lst
--neg
----negimages.jpg
--bg.txt
--rubik.jpg
```

File info/info.lst:

```
0001_0023_0047_0025_0025.jpg 1 23 47 25 25
0002_0034_0036_0047_0047.jpg 1 34 36 47 47
...
```

### Converting the marked-up collection of samples into a vec format

```
opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec
```

Than create a new *data* directory.

Directory structure:

```
gathering-images-for-haar-cascade
--info
----posimages.jpg
----info.lst
--neg
----negimages.jpg
--data
--bg.txt
--positives.vec
--rubik.jpg
```

### Cascade Training

opencv_traincascade called as following:

```
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20
```

## Cascade training set from a large dataset of positive samples

### Gathering images

Directory structure:

```
gathering-images-for-haar-cascade
--neg
----negimages.jpg
--pos
----posimages.jpg
--bg.txt
--info.dat
```

run `create_pos_n_neg()`

File info.dat:

```
pos/418.jpg 1 0 0 50 50
pos/454.jpg 1 0 0 50 50
...
```

### Converting the marked-up collection of samples into a vec format

```
opencv_createsamples -info info.dat -num 960 -w 20 -h 20 -vec positives.vec
```

Than create a new *data* directory.

Directory structure:

```
gathering-images-for-haar-cascade
--data
--neg
----negimages.jpg
--pos
----posimages.jpg
--bg.txt
--info.dat
--positives.vec
```

### Cascade Training

opencv_traincascade called as following:

```
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 900 -numNeg 450 -numStages 11 -w 20 -h 20
```
