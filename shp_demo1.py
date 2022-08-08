import shape, shp_circle, shp_rectangle, shp_square

o_shp = shape.Shape()
o_sqr = shp_square.Square(3.2)
o_rec = shp_rectangle.Rectangle(3,4)
o_cir = shp_circle.Circle(5)
o_shp = o_sqr
o_shp.show()
o_shp = o_cir
o_shp.show()
o_shp = o_rec
o_shp.show()

