m = {}
s = """
[(-15,32,85)]
[(-30,19,-108),(-14,19,55)]
[(-31,18,-109)]
[(-31,17,-107),(-31,17,-108),(-32,17,-109),(-31,17,-110)]
[(-32,16,-105),(-32,16,-106),(-32,16,-109),(-31,16,-113)]
[(-31,15,-50),(-32,15,-103),(-32,15,-104),(-33,15,-104),(-32,15,-105),(-33,15,-105),(-33,15,-106)]
[(-32,14,-48),(-30,14,-99),(-32,14,-101),(-32,14,-103),(-33,14,-103),(-33,14,-104),(-34,14,-105)]
[(-33,13,-102),(-34,13,-102),(-33,13,-103),(-34,13,-105),(-32,13,-106),(-33,13,-109),(-32,13,-119),(-31,13,-120)]
[(-34,12,-100),(-33,12,-101),(-34,12,-101),(-32,12,-104),(-33,12,-105),(-33,12,-106),(-34,12,-107),(-33,12,-108),(-33,12,-114),(-33,12,-116),(-32,12,-118),(-32,12,-119)]
[(-34,11,-100),(-33,11,-101),(-34,11,-101),(-34,11,-102),(-33,11,-109),(-33,11,-113),(-33,11,-114),(-32,11,-115),(-34,11,-116),(-33,11,-117),(-34,11,-117),(-32,11,-118),(-33,11,-118),(-33,11,-119),(-31,11,-120)]
[(-22,10,118),(-30,10,-49),(-31,10,-66),(-31,10,-67),(-31,10,-68),(-31,10,-70),(-30,10,-71),(-33,10,-99),(-34,10,-100),(-33,10,-101),(-31,10,-102),(-33,10,-102),(-34,10,-102),(-33,10,-103),(-33,10,-104),(-34,10,-112),(-34,10,-113),(-33,10,-114),(-34,10,-115),(-33,10,-116),(-34,10,-116),(-35,10,-116),(-31,10,-118),(-32,10,-120),(-33,10,-120)]
[(-31,9,-64),(-31,9,-65),(-32,9,-65),(-31,9,-66),(-32,9,-66),(-31,9,-67),(-32,9,-67),(-32,9,-68),(-31,9,-69),(-32,9,-69),(-31,9,-70),(-31,9,-71),(-30,9,-72),(-27,9,-73),(-35,9,-74),(-29,9,-74),(-34,9,-100),(-34,9,-101),(-33,9,-102),(-33,9,-103),(-33,9,-105),(-33,9,-106),(-34,9,-110),(-34,9,-113),(-34,9,-114),(-35,9,-114),(-33,9,-115),(-34,9,-116),(-35,9,-116),(-34,9,-117),(-32,9,-118),(-34,9,-118),(-33,9,-119),(-32,9,-120),(-33,9,-120)]
[(-31,8,-62),(-30,8,-63),(-31,8,-63),(-31,8,-64),(-32,8,-64),(-30,8,-65),(-32,8,-65),(-31,8,-66),(-32,8,-66),(-30,8,-67),(-33,8,-67),(-32,8,-68),(-33,8,-68),(-31,8,-69),(-32,8,-69),(-32,8,-70),(-30,8,-71),(-31,8,-71),(-28,8,-72),(-30,8,-73),(-28,8,-75),(-31,8,-96),(-31,8,-99),(-34,8,-100),(-31,8,-101),(-33,8,-101),(-33,8,-102),(-34,8,-102),(-33,8,-103),(-33,8,-104),(-33,8,-106),(-34,8,-111),(-34,8,-112),(-35,8,-112),(-35,8,-113),(-33,8,-114),(-34,8,-115),(-34,8,-116),(-32,8,-118)]
[(-30,7,-59),(-30,7,-61),(-31,7,-61),(-33,7,-63),(-31,7,-64),(-33,7,-64),(-32,7,-65),(-33,7,-66),(-31,7,-67),(-32,7,-67),(-33,7,-67),(-34,7,-67),(-31,7,-68),(-32,7,-68),(-30,7,-69),(-31,7,-69),(-32,7,-69),(-33,7,-69),(-31,7,-70),(-29,7,-71),(-30,7,-71),(-31,7,-71),(-29,7,-72),(-30,7,-72),(-28,7,-73),(-30,7,-73),(-31,7,-73),(-28,7,-74),(-29,7,-74),(-25,7,-75),(-29,7,-75),(-32,7,-98),(-33,7,-98),(-32,7,-99),(-33,7,-99),(-32,7,-100),(-33,7,-100),(-32,7,-101),(-32,7,-102),(-32,7,-103),(-33,7,-103),(-32,7,-104),(-31,7,-111),(-34,7,-112),(-35,7,-112),(-34,7,-113),(-35,7,-113),(-34,7,-115),(-33,7,-116),(-33,7,-117),(-32,7,-118)]
[(-33,6,-61),(-33,6,-64),(-33,6,-65),(-34,6,-65),(-32,6,-66),(-32,6,-67),(-33,6,-67),(-34,6,-67),(-33,6,-68),(-31,6,-69),(-33,6,-69),(-32,6,-70),(-31,6,-71),(-32,6,-71),(-30,6,-74),(-30,6,-94),(-32,6,-99),(-32,6,-100),(-33,6,-100),(-32,6,-102),(-32,6,-104),(-34,6,-110),(-32,6,-112),(-34,6,-112),(-34,6,-113),(-33,6,-114),(-34,6,-114),(-33,6,-115),(-34,6,-115),(-32,6,-117),(-31,6,-118)]
[(-32,5,-61),(-33,5,-62),(-33,5,-63),(-34,5,-63),(-34,5,-64),(-32,5,-65),(-33,5,-66),(-33,5,-67),(-31,5,-68),(-32,5,-68),(-31,5,-69),(-30,5,-70),(-31,5,-70),(-30,5,-71),(-30,5,-72),(-29,5,-73),(-29,5,-74),(-31,5,-96),(-34,5,-112),(-35,5,-112),(-33,5,-114),(-34,5,-114),(-33,5,-115),(-33,5,-116),(-31,5,-120)]
[(-29,4,-15),(-31,4,-18),(-30,4,-62),(-33,4,-63),(-34,4,-63),(-33,4,-64),(-34,4,-64),(-32,4,-66),(-33,4,-66),(-32,4,-67),(-31,4,-69),(-31,4,-70),(-30,4,-71),(-30,4,-72),(-29,4,-73),(-28,4,-75),(-28,4,-76),(-29,4,-97),(-34,4,-110),(-31,4,-111),(-33,4,-112),(-34,4,-112),(-33,4,-114),(-31,4,-118)]
[(-30,3,0),(-31,3,-16),(-32,3,-16),(-31,3,-17),(-31,3,-21),(-33,3,-61),(-31,3,-63),(-33,3,-63),(-33,3,-64),(-32,3,-65),(-34,3,-65),(-32,3,-66),(-33,3,-66),(-31,3,-67),(-31,3,-68),(-32,3,-68),(-30,3,-69),(-30,3,-70),(-31,3,-70),(-29,3,-71),(-30,3,-72),(-30,3,-98),(-34,3,-112),(-32,3,-114),(-32,3,-115),(-33,3,-116)]
[(-31,2,-14),(-32,2,-14),(-32,2,-15),(-32,2,-16),(-33,2,-16),(-32,2,-17),(-30,2,-18),(-33,2,-18),(-31,2,-20),(-29,2,-44),(-33,2,-63),(-34,2,-63),(-32,2,-65),(-32,2,-66),(-31,2,-67),(-31,2,-68),(-26,2,-70),(-29,2,-71),(-29,2,-72),(-28,2,-73),(-29,2,-73),(-26,2,-94),(-26,2,-96),(-27,2,-96),(-28,2,-109),(-31,2,-112),(-30,2,-113),(-27,2,-114),(-31,2,-115),(-28,2,-117),(-29,2,-119)]
[(-29,1,4),(-30,1,-9),(-31,1,-12),(-32,1,-13),(-32,1,-14),(-32,1,-15),(-33,1,-15),(-33,1,-16),(-34,1,-17),(-34,1,-18),(-33,1,-20),(-31,1,-21),(-32,1,-21),(-30,1,-42),(-32,1,-63),(-33,1,-63),(-32,1,-65),(-31,1,-67),(-31,1,-68),(-32,1,-68),(-30,1,-69),(-31,1,-70),(-28,1,-74),(-28,1,-106),(-31,1,-113),(-30,1,-114),(-28,1,-118)]
[(-32,0,-11),(-33,0,-12),(-33,0,-13),(-32,0,-14),(-35,0,-17),(-33,0,-18),(-31,0,-19),(-32,0,-19),(-33,0,-19),(-34,0,-19),(-31,0,-20),(-32,0,-20),(-32,0,-21),(-30,0,-22),(-31,0,-22),(-31,0,-23),(-30,0,-40),(-30,0,-41),(-29,0,-41),(-31,0,-42),(-32,0,-63),(-33,0,-63),(-31,0,-66),(-32,0,-67),(-29,0,-71),(-25,0,-104),(-25,0,-115)]
[(-34,-1,-14),(-35,-1,-15),(-33,-1,-16),(-34,-1,-17),(-35,-1,-17),(-34,-1,-18),(-34,-1,-19),(-32,-1,-21),(-33,-1,-21),(-31,-1,-23),(-32,-1,-23),(-30,-1,-39),(-32,-1,-42),(-32,-1,-43),(-28,-1,-73)]
[(-34,-2,-13),(-35,-2,-13),(-34,-2,-14),(-35,-2,-14),(-34,-2,-15),(-35,-2,-15),(-33,-2,-16),(-34,-2,-16),(-33,-2,-17),(-33,-2,-18),(-32,-2,-19),(-31,-2,-20),(-32,-2,-20),(-31,-2,-21),(-30,-2,-22),(-31,-2,-22),(-30,-2,-23),(-31,-2,-38),(-31,-2,-40),(-32,-2,-40),(-31,-2,-42),(-33,-2,-42)]
[(-33,-3,-9),(-32,-3,-10),(-32,-3,-11),(-35,-3,-13),(-35,-3,-14),(-33,-3,-15),(-29,-3,-16),(-34,-3,-16),(-33,-3,-17),(-33,-3,-18),(-32,-3,-20),(-31,-3,-21),(-30,-3,-23),(-30,-3,-24),(-33,-3,-41),(-33,-3,-42)]
[(-34,-4,-11),(-32,-4,-13),(-34,-4,-13),(-34,-4,-14),(-35,-4,-14),(-33,-4,-15),(-34,-4,-16),(-32,-4,-17),(-31,-4,-20),(-32,-4,-20),(-30,-4,-21),(-30,-4,-22),(-31,-4,-22),(-29,-4,-23),(-30,-4,-24),(-28,-4,-26),(-29,-4,-26),(-33,-4,-38),(-32,-4,-39),(-33,-4,-39),(-33,-4,-46),(-32,-4,-47)]
[(-35,-5,-13),(-33,-5,-15),(-33,-5,-16),(-33,-5,-17),(-32,-5,-19),(-31,-5,-20),(-30,-5,-21),(-30,-5,-22),(-30,-5,-23),(-29,-5,-24),(-29,-5,-25),(-32,-5,-38),(-33,-5,-38),(-33,-5,-39),(-33,-5,-46),(-33,-5,-48)]
[(-34,-6,-14),(-35,-6,-14),(-33,-6,-15),(-28,-6,-16),(-32,-6,-17),(-27,-6,-20),(-30,-6,-21),(-31,-6,-22),(-29,-6,-23),(-30,-6,-24),(-28,-6,-26),(-29,-6,-26),(-32,-6,-38),(-32,-6,-39),(-33,-6,-39),(-32,-6,-43)]
[(-30,-7,-8),(-33,-7,-9),(-33,-7,-11),(-32,-7,-12),(-33,-7,-12),(-33,-7,-13),(-33,-7,-14),(-34,-7,-14),(-32,-7,-15),(-32,-7,-16),(-30,-7,-17),(-31,-7,-17),(-33,-7,-17),(-28,-7,-20),(-29,-7,-21),(-29,-7,-22),(-28,-7,-23),(-32,-7,-37),(-33,-7,-38),(-32,-7,-39)]
[(-29,-8,-9),(-29,-8,-10),(-30,-8,-12),(-28,-8,-13),(-26,-8,-15),(-31,-8,-15),(-29,-8,-17),(-24,-8,-18),(-28,-8,-18),(-27,-8,-18),(-30,-8,-18),(-25,-8,-19),(-29,-8,-20),(-27,-8,-21),(-27,-8,-24),(-32,-8,-38),(-33,-8,-43),(-32,-8,-44),(-33,-8,-44)]
[(-30,-9,-9),(-31,-9,-11),(-32,-9,-11),(-31,-9,-13),(-32,-9,-14),(-29,-9,-17),(-29,-9,-19),(-26,-9,-20),(-28,-9,-20),(-28,-9,-21),(-26,-9,-23),(-31,-9,-35),(-33,-9,-42),(-33,-9,-43),(-32,-9,-44),(-33,-9,-44)]
[(-28,-10,-8),(-27,-10,-10),(-28,-10,-12),(-28,-10,-17),(-23,-10,-19),(-24,-10,-19),(-26,-10,-19),(-28,-10,-31),(-33,-10,-43),(-32,-10,-43),(-33,-10,-44)]
[(-21,-11,-1),(-21,-11,-2),(-21,-11,-3),(-21,-11,-4),(-24,-11,-7),(-24,-11,-13),(-26,-11,-16),(-21,-11,-19),(-23,-11,-19),(-32,-11,-41),(-33,-11,-43),(-32,-11,-44)]
[(-21,-12,-1),(-21,-12,-2),(-21,-12,-3),(-21,-12,-5),(-20,-12,-7),(-22,-12,-7),(-21,-12,-8),(-22,-12,-9),(-18,-12,-13),(-23,-12,-13),(-21,-12,-14),(-22,-12,-16),(-23,-12,-16),(-26,-12,-17)]
[(-19,-13,-1),(-21,-13,-1),(-21,-13,-2),(-21,-13,-4),(-21,-13,-5),(-21,-13,-6),(-19,-13,-7),(-29,-13,-41),(-31,-13,-43),(-30,-13,-44)]
[(-21,-14,-1),(-17,-14,-2),(-21,-14,-2),(-20,-14,-3),(-19,-14,-5),(-20,-14,-5),(-15,-14,-8),(-19,-14,-9),(-29,-14,-42)]
[(-18,-15,3),(-20,-15,1),(-21,-15,-3),(-14,-15,-5),(-17,-15,-5),(-21,-15,-5),(-15,-15,-6),(-14,-15,-6),(-14,-15,-7),(-14,-15,-10),(-29,-15,-44)]
[(-17,-16,2),(-19,-16,0),(-19,-16,-1),(-19,-16,-2),(-14,-16,-3),(-19,-16,-3),(-20,-16,-3),(-15,-16,-4),(-26,-16,-38),(-26,-16,-41),(-26,-16,-42),(-27,-16,-44)]
[(-11,-17,8),(-10,-17,2),(-13,-17,1),(-10,-17,-1),(-19,-17,-1),(-15,-17,-2),(-15,-17,-3),(-22,-17,-37)]
[(-9,-18,7),(-13,-18,3),(-7,-18,-1),(-13,-18,-1),(-16,-18,-2),(-17,-18,-2),(-18,-18,-3),(-19,-18,-34),(-22,-18,-38),(-23,-18,-40),(-24,-18,-40),(-25,-18,-40),(-21,-18,-44)]
[(-12,-19,7),(-18,-19,-35),(-21,-19,-37),(-20,-19,-38),(-20,-19,-51),(-21,-19,-52)]
[(-7,-20,3)]




"""
#s='[(-31,4,-18),(-34,1,-17)]'
a = eval(','.join(''.join(s.split()).split("][")))
for i in range(len(a)):
 for j in range(len(a)):
  w = (a[i][1] + a[j][1]) * 10000000 + 2*a[i][0]-a[i][2]+2*a[j][0]-a[j][2]
  if w in m:
   m[w].append((i, j))
  else:
   m[w] = [(i, j)]
# 搜飞船把右边的数组改成 a，然后在里面判断
for i in [(-25,9,-74),(-33,6,-68)] + [(-34,-2,-13),(-33,13,-103)] + [(-28,-7,-24),(-26,-9,-23),(-33,7,-103),(-34,6,-115),(-31,-13,-43),(-23,-12,-16)] + [(-8,-28,1),(-20,-19,-38)]:
 w = (5 - i[1]) * 10000000 + -95 - (2*i[0]-i[2])
 if w in m:
  for k in m[w]:
   print(sorted((i, a[k[0]], a[k[1]]), key=lambda x:-x[1]), end=',')

"""
for i in range(len(a)):
 for j in range(len(a)):
  w = (5 - (a[i][1] + a[j][1])) * 10000000 + -95 - (2*a[i][0]-a[i][2]+2*a[j][0]-a[j][2])
  if w in m:
   for k in m[w]:
    print(a[i], a[j], a[k[0]], a[k[1]])
"""
