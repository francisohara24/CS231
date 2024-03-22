grid_size_25_results = "260=2800, 5=4, 265=2306, 10=0, 270=3431, 15=10, 275=3383, 20=10, 280=3401, 25=31, 285=2733, 30=24, 290=3780, 35=16, 295=3462, 40=41, 300=3568, 45=45, 305=3494, 50=61, 310=3361, 55=132, 315=3202, 60=134, 320=3780, 65=146, 325=3852, 70=254, 330=4512, 75=181, 335=4288, 80=509, 340=5022, 85=251, 345=5372, 90=275, 350=5052, 95=330, 355=5169, 100=392, 360=5227, 105=471, 365=5631, 110=474, 370=5971, 115=604, 375=5872, 120=618, 380=6359, 125=691, 385=6003, 130=768, 390=6595, 135=691, 395=6555, 140=814, 400=7370, 145=755, 405=6577, 150=793, 410=7478, 155=825, 415=7050, 160=1252, 420=6917, 165=1125, 425=7158, 170=1348, 430=8049, 175=1438, 435=7811, 180=1358, 440=7686, 185=1273, 445=7328, 190=1388, 450=9237, 195=1456, 455=8684, 200=1629, 460=8933, 205=1617, 465=9445, 210=1441, 470=8745, 215=1557, 475=9676, 220=1879, 480=10922, 225=1787, 485=10522, 230=2158, 490=10242, 235=1928, 495=11217, 240=2694, 245=2326, 250=2744, 255=2438"
grid_size_50_results = "260=2541, 5=0, 265=2664, 10=0, 270=2761, 15=8, 275=2718, 20=34, 280=3286, 25=30, 285=3597, 30=47, 290=3660, 35=49, 295=3587, 40=66, 300=3502, 45=62, 305=3912, 50=98, 310=4252, 55=115, 315=4067, 60=106, 320=4052, 65=106, 325=4142, 70=170, 330=4372, 75=211, 335=4646, 80=311, 340=5324, 85=221, 345=4998, 90=304, 350=4995, 95=381, 355=4567, 100=527, 360=4739, 105=554, 365=4948, 110=465, 370=6356, 115=454, 375=6988, 120=521, 380=5557, 125=609, 385=6816, 130=802, 390=6328, 135=559, 395=5941, 140=967, 400=7000, 145=773, 405=6883, 150=990, 410=6567, 155=929, 415=7256, 160=1232, 420=7977, 165=1014, 425=7283, 170=1009, 430=7527, 175=1289, 435=8750, 180=1692, 440=8111, 185=1323, 445=8127, 190=1390, 450=8040, 195=1572, 455=9310, 200=1684, 460=8815, 205=1592, 465=8869, 210=1548, 470=9331, 215=1913, 475=9364, 220=2562, 480=9454, 225=2352, 485=10326, 230=1784, 490=9240, 235=2120, 495=11273, 240=2067, 245=2833, 250=2377, 255=3158"
initial_chance_50_results = "0.0=0, 0.3=107, 0.39999999999999997=64, 0.49999999999999994=106, 0.7000000000000001=51, 0.1=115, 0.9000000000000002=4, 0.9500000000000003=0, 0.65=86, 0.7500000000000001=40, 0.25=76, 0.35=97, 0.44999999999999996=135, 0.6=80, 0.8000000000000002=0, 0.05=6, 0.2=52, 0.15000000000000002=116, 0.5499999999999999=94, 0.8500000000000002=8"
initial_chance_100_results = "0.0=0, 0.3=305, 0.39999999999999997=342, 0.49999999999999994=263, 0.7000000000000001=245, 0.1=266, 0.9000000000000002=12, 0.9500000000000003=0, 0.65=350, 0.7500000000000001=345, 0.25=423, 0.35=345, 0.44999999999999996=264, 0.6=340, 0.8000000000000002=39, 0.05=27, 0.2=341, 0.15000000000000002=363, 0.5499999999999999=392, 0.8500000000000002=24"


print("Grid Size vs Live Cell Count(chance=0.25):")
for key_value_pair in grid_size_25_results.split(","):
    key_value_pair = key_value_pair.strip()
    key, value = key_value_pair.split("=")
    print(key.ljust(10) + value.ljust(10))


print("Grid Size vs Live Cell Count(chance=0.50):")
for key_value_pair in grid_size_50_results.split(","):
    key_value_pair = key_value_pair.strip()
    key, value = key_value_pair.split("=")
    print(key.ljust(10) + value.ljust(10))


print("Initial Chance vs Live Cell Count(grid_size=50x50):")
for key_value_pair in initial_chance_50_results.split(","):
    key_value_pair = key_value_pair.strip()
    key, value = key_value_pair.split("=")
    print(str(round(float(key), 2)).ljust(10) + value.ljust(10))


print("Initial Chance vs Live Cell Count(grid_size=100x100):")
for key_value_pair in initial_chance_100_results.split(","):
    key_value_pair = key_value_pair.strip()
    key, value = key_value_pair.split("=")
    print(str(round(float(key), 2)).ljust(10) + value.ljust(10))



