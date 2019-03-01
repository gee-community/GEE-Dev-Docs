This is a place to collect tutorial/examples/etc while platform is being built.

# How-To

## Feature Collection

**Generate regular grid intersecting a geometry**

*Author: Gena*

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

