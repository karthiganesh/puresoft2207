#kg220729 demo for importing UDF
import demo_mod_const
import demo_mod_UDF
import shape1

#main starts here
demo_mod_UDF.show_conf()
print(demo_mod_const.DT_DEV_START)
o_shp1 = shape1.Square()
o_shp1.run()
o_shp2 = shape1.Rectangle()
o_shp2.run()
