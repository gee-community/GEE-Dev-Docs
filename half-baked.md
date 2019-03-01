This is a place to collect tutorials/examples/etc while platform is being built.


- [How-To](#how-to)
  * [Landsat](#landsat)
    + [Terrain Correction](#terrain-correction)
  * [Feature Collection](#feature-collection)
  * [Charts](#charts)
    + [Scatterplot](#scatterplot)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>



# How-To

## Landsat

### Terrain Correction

**Minnaert-correction**

Implementation where Minnaert constant k is calculated per pixel as a function of slope.

*Author: Justin Braaten*

> Ge, H., Lu, D., He, S., Xu, A., Zhou, G., & Du, H. (2008). Pixel-based Minnaert correction method for reducing topographic effects on a Landsat 7 ETM+ image. Photogrammetric Engineering & Remote Sensing, 74(11), 1343-1350. | https://orst.library.ingentaconnect.com/content/asprs/pers/2008/00000074/00000011/art00003?crawler=true&mimetype=application/pdf

https://code.earthengine.google.com/1fcc034eb3014d7606eec467241dc1da

TODO: Sun azimuth and zenith angles are taken from image metadata, so represent nadir position and are held constant. Could adjust for every pixel. 

## Feature Collection

**Generate regular grid intersecting a geometry**

*Author: Gennadii Donchyts*

https://code.earthengine.google.com/ff50a3e4745b1e732b1b7ac8a12623b6

Also implemented in `users/gena/packages:grid` library

```js
var g = require('users/gena/packages:grid')
var dx = 0.45
var dy = 0.45
var grid = g.generateGridForGeometry(region.bounds(), dx, dy)
```

Example of its use in dividing an image for export

*Author: marortpab*

https://code.earthengine.google.com/3a413327f67acc350bec59ba5ce1cb3c

TODO: make reproducable - calls on marortpab assets


## Charts

### Scatterplot

**3-band Scatterplot**

*Author: Gennadii Donchyts*

https://code.earthengine.google.com/252fda4ed0340c3e926096b01668576b





