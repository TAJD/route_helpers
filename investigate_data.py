import routing_helper as rh
import numpy as np

def test_wisp():
    year = "2005"
    quarter = "q1"
    path = "/scratch/td7g11/era5/polynesia_"+year+"_"+quarter+"/polynesia_"+year+"_"+quarter+".nc"

    wisp, widi, wh, wd, wp, time = rh.retrieve_era5_ensemble(path, 0)

    print(wisp)
    print(wisp.dropna("time"))

    processed_wisp, lons, lats = rh.return_data(wisp)
    print(processed_wisp)
    print(lons)
    print(lats)

def test_waves(): 
    year = "2005"
    quarter = "q1"
    path = "/scratch/td7g11/era5/polynesia_"+year+"_"+quarter+"/polynesia_"+year+"_"+quarter+".nc"

    wisp, widi, wh, wd, wp, time = rh.retrieve_era5_ensemble(path, 0)
    #print(wh)
    #print(wisp)
    #print(time.size)
 #   processed_wisp, lons, lats = rh.return_data(wisp)
 #   print(processed_wisp)
 #   print(lons)
#    print(lats)

#test_waves()    


def check_performance():
    x_tws = np.array([0.0, 5.0, 10.0])
    x_tws, x_twa, y_bsp = rh.generate_canoe_performance(60.0, x_tws, 0.3)
    print(y_bsp)


check_performance()
