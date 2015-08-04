### estimate regresisonr results ####
# from numpy import *
# import scipy as sp
# from pandas import *
# from rpy2.robjects.packages import importr
# import rpy2.robjects as ro
# import pandas.rpy.common as com
#from view_helper import tryout
import json
import csv

# ro.r('x=c()')
# ro.r('x[1]=22')
# ro.r('x[2]=44')
# print(ro.r('x'))

# print(ro.r['x'])
# ro.r('x=c(22,21,20,19,18)')
# ro.r('x[1] = poly(x,4)')
# print(ro.r('x'))

# def estimation(intercept, year, year2, year3, year4, height, height2, height3, height4, width, width2, width3, width4, sale_year, sale_year2, sale_year3, sale_year4, prov, certificate, mediumpaper, mediumpainting):
#     i = 1
#     c = c_cruz
#     result = c['(Intercept)'][i]*intercept + c['poly(year, 4)1'][i]*year + c['poly(year, 4)2'][i]*(year2) + c['poly(year, 4)3'][i]*(year3) + c['poly(year, 4)4'][i]*(year4)
#     + c['poly(height, 4)1'][i]*height + c['poly(height, 4)2'][i]*(height2) + c['poly(height, 4)3'][i]*(height3) + c['poly(height, 4)4'][i]*(height4)
#     + c['poly(width, 4)1'][i]*width + c['poly(width, 4)2'][i]*(width2) + c['poly(width, 4)3'][i]*(width3) + c['poly(width, 4)4'][i]*(width4)
#     + c['poly(sale_year, 4)1'][i]*sale_year + c['poly(sale_year, 4)2'][i]*(sale_year2) + c['poly(sale_year, 4)3'][i]*(sale_year3) + c['poly(sale_year, 4)4'][i]*(sale_year4)
#     + c['prov'][i]*prov + c['certificate'][i]*certificate + c['mediumpainting'][i]*mediumpainting + c['mediumpaper'][i]*mediumpaper
#     return result

#print estimation(1, 0.097,0.055,-0.0100,-0.0811,-0.025,0.0036,0.0269,-0.034,-0.028,0.0127,0.0067,-0.037,0.033,0.0104,-0.0160,-0.036,0,0,0,0)

# def estimat(width, width2, width3, width4):
#     i = quality
#     c = c_lam
#     result = c['poly(width, 4)1'][i]*width + c['poly(width, 4)2'][i]*width2 + c['poly(width, 4)3'][i]*width3 + c['poly(width, 4)4'][i]*width4
#     return result

#print estimat(width, width2, width3, width4)

### Diego rivera ###
"","c1","c2","c3","c4","c5"
c_rivera = {"(Intercept)": [11192.1748743296,22080.4227632018,47167.2076294848,81148.9110306502,292018.548884628],
"poly(year, 4)1":[-34072.9267911634,-114421.298076288,-134917.22828128,-178182.32725737,-44606.6832541242],
"poly(year, 4)2":[20253.5661575287,131641.142961169,185100.795610601,285546.547199381,1127549.86912342],
"poly(year, 4)3":[-31265.7110996448,-192681.461773152,-272833.547721936,-347837.802415874,-657099.458572986],
"poly(year, 4)4":[22011.0949153747,116674.626427868,170258.21920855,174410.835572468,450002.091594102],
"poly(height, 4)1":[351744303.025682,546165967.252234,3142023947.12523,3394595559.37004,3292803854.66179],
"poly(height, 4)2":[234104467.939278,364183647.088991,2096402357.95369,2264404788.51783,2197064162.67034],
"poly(height, 4)3":[14655934.1381665,23677043.5427514,135376206.549502,146210895.285799,144634524.831115],
"poly(height, 4)4":[683057.144294429,1592927.30213583,7766542.91971797,8552155.5478296,9037748.85589802],
"poly(width, 4)1":[-325216390.768743,-504752976.245089,-2905883014.1456,-3138565090.76299,-3040843585.33857],
"poly(width, 4)2":[-268769278.303009,-418175992.871121,-2404509368.18273,-2598426952.68922,-2525921560.41942],
"poly(width, 4)3":[-27018344.3294101,-42826959.7362176,-244365356.551955,-264652691.928204,-256986769.690621],
"poly(width, 4)4":[-1636794.04825008,-2879585.59437679,-15445841.5337894,-16704926.8526751,-10556444.9085842],
"poly(sale_year, 4)1":[-35880.4146154448,-52657.1676701545,-48002.6205071837,39821.7231568174,976721.025225506],
"poly(sale_year, 4)2":[10291.915415287,24260.4904920446,-31402.0965854185,-6908.12272497226,487386.975316465],
"poly(sale_year, 4)3":[-43034.7356581152,-50258.3761547079,-74490.7500332305,-101771.435004131,176199.616040408],
"poly(sale_year, 4)4":[10542.0236611939,11713.5169533826,11400.1705380806,22686.3027577711,-481452.751748451],
"prov":[4886.59740685292,4280.66391979405,5152.52403757809,7459.40001131664,-1196.33302068299],
"certificate":[-1935.97336611625,-601.110133960115,2884.35794497608,897.646539298976,-35403.4203049395],
"mediumpainting":[45488.4560438386,125199.722554223,275154.088827709,382039.753897425,686423.958764877],
"mediumpaper":[4008.70994761548,6952.38659177097,13719.5123875657,14319.3824291276,36478.4103298551],}

### Cruz-Diez ###
c_cruz = {"(Intercept)": [15948.3926882015,44056.6442909019,73086.0761727673,103708.712496947,270805.720475316],
"poly(year, 4)1": [-81223.2686712085,-277838.213336888,-460630.529285992,-531511.207145758,-306984.89792752],
"poly(year, 4)2": [-42636.9024060533,-51604.8535693941,-67973.8640238258,-76431.6723864685,8742.05264357326],
"poly(year, 4)3": [58856.331140289,160054.552620602,236781.337055309,297988.018738226,997202.920418523],
"poly(year, 4)4": [4739.44254653035,-46647.2414010779,-88988.0254510511,-85089.5234706405,-1155823.57931006],
"poly(height, 4)1": [-11476.8981462271,-135928.686776647,-169141.269511981,-272673.266415415,-1507884.62876535],
"poly(height, 4)2": [-178351.362512729,-483464.2128346,-725329.542632254,-939804.097425688,-1150681.159442],
"poly(height, 4)3": [-98843.8716182481,-347012.663443385,-586530.885431171,-948996.017871425,-1320141.55417155],
"poly(height, 4)4": [-68360.6171245851,-236503.995340736,-420236.390498348,-671935.333515105,-1428060.45645227],
"poly(width, 4)1": [600765.634506336,1125480.72449114,1557572.35369691,2040073.54047369,3493800.7520246],
"poly(width, 4)2": [672731.286558412,788845.753349199,971649.97265706,1221338.56616767,1202602.96354999],
"poly(width, 4)3": [246398.345788717,245417.344593809,167984.139090368,169933.561341781,764940.32966183],
"poly(width, 4)4": [143514.292748812,300321.420651983,276665.305049332,402736.639259857,1304045.83880023],
"poly(sale_year, 4)1": [284261.458572581,677818.698518144,870419.165519447,983753.099890943,811243.879982478],
"poly(sale_year, 4)2": [-76641.83770907,-101911.283822304,62608.711228494,183524.239965251,133705.404682559],
"poly(sale_year, 4)3": [-151879.617059688,-273648.029089975,-220266.192578075,-77752.3963540533,153176.890370681],
"poly(sale_year, 4)4": [-98783.7069607526,-192671.461900929,-220607.159442524,-217143.32198063,-588927.86059034],
"prov": [30945.0871412781,34087.5244566855,24919.6275097254,9121.97290504747,3566.04688491094],
"certificate": [-2133.40082548791,1703.8905359088,7322.54849420026,20133.427399445,-31901.4254668276],
"mediumpainting":[12012.3000393041,16359.2940358913,20255.6657551041,30602.4242037819,53089.1974208043],
"mediumpaper": [-4967.25700988004,-17659.2523483382,-4194.03145644159,2059.89907316897,-19230.7304852107],}

### Carrington ###
c_carrington = {"(Intercept)":[2935.28478084722,16071.2456459401,37812.0642487467,71556.6925426805,250073.765400413],
"poly(year, 4)1":[-50791.7052500432,-78716.1322632937,-146547.561361158,-199889.356443144,-672226.652720805],
"poly(year, 4)2":[-18984.7704099152,-48583.2960335759,-55510.145204995,-117531.586197178,-495181.245692008],
"poly(year, 4)3":[27106.3677009855,39239.0724407538,41421.8371870592,52073.5027609792,-238454.839677299],
"poly(year, 4)4":[-17378.8160005393,-33706.7129121179,-32511.9419999545,-55358.8634974349,-245108.117630918],
"poly(height, 4)1":[274601.622986124,438281.745047461,656806.163352268,1186879.12316513,5830349.08051514],
"poly(height, 4)2":[303686.797833595,314191.810536256,358110.800594329,475041.70508984,3170489.54028726],
"poly(height, 4)3":[131458.386248714,-15243.5314245582,-181347.061786264,-790610.873526126,-2829398.02713136],
"poly(height, 4)4":[20513.4030146962,-95515.3266055725,-277093.545839791,-656104.719137882,-2383202.32744393],
"poly(width, 4)1":[138302.98004061,309223.693222229,488604.826861289,679040.028309221,425389.653123408],
"poly(width, 4)2":[68942.3847870448,121612.804568993,196397.442681096,110770.998762686,-1507691.46365545],
"poly(width, 4)3":[-27979.1212025898,-165967.050139457,-278647.738681096,-491519.641615745,-2548156.24402336],
"poly(width, 4)4":[77706.3466676007,4978.29970485194,-182865.296773982,-168739.898794243,-1124307.01219349],
"poly(sale_year, 4)1":[115368.479779964,249924.477361534,214531.772416894,372546.551825057,1005765.78725536],
"poly(sale_year, 4)2":[-88547.3130460876,-103180.295329667,-12817.5782635448,28594.625504588,617304.76042869],
"poly(sale_year, 4)3":[-38246.5246202126,-89283.8935102394,-47539.58819069,-56302.7752373451,186763.642296609],
"poly(sale_year, 4)4":[94590.1226569304,130794.192386022,39159.6767447012,18.2857748552291,209565.316277964],
"prov":[-800.781333444306,216.817009498855,9570.72218361988,18753.5995323921,31356.483120128],
"certificate":[12743.9102142256,9087.3078666719,2607.1978759588,4455.4445865942,160394.660090763],
"mediumpainting":[31251.9728091354,48770.6860046409,64784.9714413651,98664.6204983985,135134.318785541],
"mediumpaper":[4164.34876343513,1545.24506937801,-88.6392023130866,-1655.20527639151,-14489.3223537443],}

### Bermudez ###
c_bermudez = {"(Intercept)":[4182.86771019413,8214.03184613177,15979.23494944,25630.66428947,70121.2185610981],
"poly(year, 4)1":[-11342.3748991362,-8645.79034379937,2852.0051161903,-17020.6173682703,-921337.088534229],
"poly(year, 4)2":[41192.3552133025,81670.6280568851,107522.153968732,119660.869792682,1288796.94740137],
"poly(year, 4)3":[27460.739177119,44920.8305311508,27283.755675164,27973.0178652832,-526718.593457938],
"poly(year, 4)4":[27833.0864398812,64508.7488041035,102007.301736347,92912.3969560297,665965.718089715],
"poly(height, 4)1":[31876.5150481068,22247.8200929842,48703.2527398504,-2446.07959506283,197205.426995909],
"poly(height, 4)2":[1498.78293531337,-18589.2730142862,-44090.6630127415,-56900.6655370677,-315499.611293714],
"poly(height, 4)3":[38083.9687469355,2446.58658894312,-23251.7810917822,-64152.696198748,-364437.9314515],
"poly(height, 4)4":[3682.86429347583,-17060.8237223751,-30173.7039751276,-19763.8922827263,-146078.598402356],
"poly(width, 4)1":[30202.921133414,52065.3791185541,26451.2841467741,123901.416914964,-53669.4818759288],
"poly(width, 4)2":[-22367.1518825012,-30381.8157551547,-29572.0654025367,72433.9939411043,42853.6312443058],
"poly(width, 4)3":[-8838.77287018207,8955.69315197999,80.8433890602602,108822.682718513,133975.472686235],
"poly(width, 4)4":[6811.88677432028,5249.68729357207,36922.1001213166,136139.931552827,94890.3939832029],
"poly(sale_year, 4)1":[76112.4183282254,80417.7324444648,148900.21725185,139497.976014311,207119.644646029],
"poly(sale_year, 4)2":[-55475.7312679219,-71797.1140963258,-37361.8362336628,-29837.1567247379,-158018.592028382],
"poly(sale_year, 4)3":[-22235.7132063034,-23660.8117200038,28327.2076770238,-14332.4619746753,-12098.1549359156],
"poly(sale_year, 4)4":[-272.421380167803,-4885.54279194921,19318.3634540656,12851.6924707784,245995.955141535],
"prov":[-10907.263413365,1011.76174060495,-14675.7999654723,79647.5381365988,-67544.6964576106],
"certificate":[4398.75960726321,5976.63867702319,11682.838497998,17634.8744013653,40771.1860909093],
"mediumpainting":[9299.31169889154,11530.269792712,16213.5348244387,30469.7571364269,126189.506317438],
"mediumpaper":[2296.41364003923,776.802293864348,-1835.56449426417,-6071.7330087616,48702.0403980301],}

### Orozco ### 
c_orozco = {"(Intercept)":[3180.01102150192,6605.26210988731,18117.3349771034,64061.2532220423,223690.788213591],
"poly(year, 4)1":[-29329.9823092133,-34002.8055765909,-66868.1198810749,-134729.313290214,-117856.89506512],
"poly(year, 4)2":[20204.8890216904,12866.9651545765,-28151.2107891277,-14479.182755684,-149268.388157154],
"poly(year, 4)3":[-32074.3370284786,-45041.063804305,-83661.5698898283,-17193.6587129411,-63545.759619191],
"poly(year, 4)4":[9632.60940479097,-6910.31375908786,-30561.197533441,-99973.4145385912,-47139.696904591],
"poly(height, 4)1":[33495.1145163571,-149007.206041068,-555542.976185647,1158436.95404608,4410884.01494306],
"poly(height, 4)2":[-1428.06564800324,-266926.928819313,-972839.993757311,246367.153813055,-294852.558545117],
"poly(height, 4)3":[-9775.31599269791,-51413.3218429856,-253905.267999663,-610813.07149176,-3370537.39851492],
"poly(height, 4)4":[-8705.45748316232,-4786.24100179259,-58824.0223054581,-325667.612234415,-1588905.58777077],
"poly(width, 4)1":[10041.8784731684,168629.057623741,651166.597371986,102731.044927292,50612.2336418483],
"poly(width, 4)2":[16488.3622184399,228723.802694781,833049.333394935,-441224.983801712,-951736.85425795],
"poly(width, 4)3":[10209.3003734741,213718.840243683,662162.61402589,-766401.014965933,-1823828.59668235],
"poly(width, 4)4":[-314.347750874538,98055.4687198374,272037.268950345,-382718.172526677,-1040267.89407413],
"poly(sale_year, 4)1":[8248.10302096554,11041.4868930938,2710.98060323564,156667.431613363,152230.749224665],
"poly(sale_year, 4)2":[-37646.7376067816,-52982.7695160869,-70196.6934833945,-76205.5151353032,-157247.106797885],
"poly(sale_year, 4)3":[12058.2358427439,4330.89523287765,-61971.1161502869,-122775.310937085,-152899.201965076],
"poly(sale_year, 4)4":[-4058.50358611809,-13180.7395823384,-22793.5031117042,-53868.9618821612,48108.5883167545],
"prov":[1871.13151033376,9864.37788698383,12510.9649259532,-2960.08099217959,-28923.8676911506],
"certificate":[-656.959171559635,-849.516388343377,-1135.08470030195,-11878.9462774626,-47825.7675158076],
"mediumpainting":[13293.0131980767,19616.6267458797,37403.6280799823,43326.1335288954,32023.5304273321],
"mediumpaper":[1437.38548472305,2498.08074729729,7367.95549549873,4397.10179177083,-1962.76041043596],}

### Pedro Coronel ###
c_coronel = {"(Intercept)":[17734.3520845733,18353.7926280551,30502.5313200582,55702.5855040781,63437.1383414982],
"poly(year, 4)1":[8206.65565390505,27742.6178894334,20225.1601814152,17995.8413807218,-391040.512464732],
"poly(year, 4)2":[-25035.42234623,-7868.87231354121,3562.08498010419,-2113.06093623625,-134395.41364024],
"poly(year, 4)3":[922.446051980344,6760.22361940051,50688.6600730537,98688.9363515011,352445.65399304],
"poly(year, 4)4":[21568.5559309537,-5136.07585693082,20004.2790408797,19966.3798764464,-184502.835058299],
"poly(height, 4)1":[47605.6228545874,42926.5844296926,144670.362017102,334657.692526739,494201.300486679],
"poly(height, 4)2":[-38426.405193478,-51817.343045319,-114392.336781136,-86955.5680703312,-234847.791825032],
"poly(height, 4)3":[43152.8695704754,13265.4787534318,-40911.9766596468,-165314.306097206,-191730.402251436],
"poly(height, 4)4":[50707.3371491108,66367.8528361055,41081.3743054277,67284.1937852658,155291.555245654],
"poly(width, 4)1":[301780.328875071,371595.747517869,485063.724973499,702796.140265118,572961.494810298],
"poly(width, 4)2":[51455.6626453377,79386.5337465024,186698.37530663,423794.606136593,180156.793321546],
"poly(width, 4)3":[-101926.501362542,-114064.650254523,-188947.698662673,160395.126169542,-16234.0054898714],
"poly(width, 4)4":[-16975.3197042335,-47239.2445806702,-17285.5040687185,207986.514538754,223948.494859625],
"poly(sale_year, 4)1":[138915.337701283,197601.205522874,266540.177568146,257935.471860889,319394.335569254],
"poly(sale_year, 4)2":[-69518.3705229725,-76317.2227678047,-122465.153312804,-139457.600848567,-94163.2833873761],
"poly(sale_year, 4)3":[23085.1472205722,36063.3865682984,58602.7834537287,88887.7798384683,464965.354873846],
"poly(sale_year, 4)4":[-58128.9437657335,-72486.4380997764,-118795.798354807,-121266.419619884,85747.8498655951],
"prov":[1668.57020656293,696.630531941462,8847.26780096776,-9873.62124503641,-35714.2463608494],
"certificate":[-2344.54581294039,30.8563094010454,-327.704682560284,2124.56789065468,46832.6185531332],
"mediumpainting":[11537.4152094831,27366.5252582761,36474.3452119609,37370.1773841166,79942.8119295377],
"mediumpaper":[-707.32562120739,-2299.35599442244,1400.13212609238,6713.65290910922,45778.6759860432],}

### Siqueiros ###
c_siqueiros = {"(Intercept)":[6727.03301414025,11105.2344712537,25990.158981304,51737.6377850787,193746.411396449],
"poly(year, 4)1":[-31727.1758428606,-32314.1965786292,-76899.2353780819,-169662.464418255,-765722.160750388],
"poly(year, 4)2":[-25687.3927453211,-55372.6008523874,-83660.6586439718,-117903.461879716,-1256865.1332671],
"poly(year, 4)3":[18572.116025998,10634.3321585902,-12103.8183813043,4069.27092543992,656036.877024774],
"poly(year, 4)4":[-5203.48827543204,-12501.1969694762,8928.33606939263,11470.2978710474,894151.018514579],
"poly(height, 4)1":[106468.832954859,145976.535319128,206948.29445058,515655.549701533,439477.127378829],
"poly(height, 4)2":[7021.37491695476,17259.0579230204,17588.649310227,62679.5047129453,-84984.6044257423],
"poly(height, 4)3":[-13916.7965563417,-43373.2377091564,-72977.8367666882,-187904.503921009,-281336.992762476],
"poly(height, 4)4":[36495.7882021937,27592.392935091,6796.38001871634,-45146.5944307232,124445.697934195],
"poly(width, 4)1":[249649.869520193,297287.948822325,360070.474905174,276124.160015853,-52799.3551544128],
"poly(width, 4)2":[211741.18992931,185788.893422778,126829.5924464,13573.3799732786,-400956.953435595],
"poly(width, 4)3":[-70043.145986196,-119100.601372961,-142757.722315406,2717.90542002706,779929.265683054],
"poly(width, 4)4":[-117460.994487305,-180583.676516925,-186953.223138302,-75616.878032986,-808952.187885012],
"poly(sale_year, 4)1":[32740.7877761592,65202.5272155031,104879.439701467,228202.780757064,1863170.37698437],
"poly(sale_year, 4)2":[-96698.4945522383,-123077.144514802,-173755.12492286,-131044.590325217,-579161.639075458],
"poly(sale_year, 4)3":[-21020.8567625476,-30966.9801437362,-52832.2871004792,-56444.695009329,-497791.535197496],
"poly(sale_year, 4)4":[29611.1841931577,23166.2211589114,21691.1708985111,7686.08087152707,-196797.62928263],
"prov":[6222.05149088064,10672.9029615347,40819.1209614176,118814.384500963,220992.377766457],
"certificate":[-1161.15442566177,-4632.91496390792,-2651.20111473532,-11344.4785230445,-173782.734506849],
"mediumpainting":[13131.0866229824,20322.7455077998,17905.6825351283,15605.7579979275,80250.6817073796],
"mediumpaper":[2945.19401703818,5072.05643335673,1460.52756188682,7219.14352456137,166969.353804275],}

### Tamayo ###
c_tamayo = {"(Intercept)":[13890.63772888,20657.1077040497,31161.4090513918,81905.3913029823,831687.571750314],
"poly(year, 4)1":[-124408.836054883,-200348.111282719,-384426.321412388,-854060.791112932,-3545122.61743487],
"poly(year, 4)2":[75104.4860015106,126908.301153016,116833.66241152,-136548.515868245,-523509.125603531],
"poly(year, 4)3":[-41326.4977436176,-85858.1399074496,17298.5166578305,136555.752725603,1540511.30170245],
"poly(year, 4)4":[-25208.802486572,-35798.8118612991,-75848.2303970593,-97471.1432609054,-1347479.8991075],
"poly(height, 4)1":[652332.406886451,881653.423955169,1188637.45398292,1209497.70798288,51667806.2105042],
"poly(height, 4)2":[-119138.466216558,-179274.155183301,-276745.843083772,-845318.601880356,-11803931.2921327],
"poly(height, 4)3":[-996616.103998801,-1324439.94083015,-1718298.45781832,-423676.991696658,-75806260.9322271],
"poly(height, 4)4":[-701427.68484167,-843005.640676929,-1097785.30524951,476603.789034221,-37779550.0163354],
"poly(width, 4)1":[4229288.40273636,3811995.44922003,3342501.05460094,5218467.05135041,-65760459.5879612],
"poly(width, 4)2":[3341930.52595498,2996323.97843625,2597561.27946312,3067806.84062855,-49077893.266064],
"poly(width, 4)3":[338723.059234525,296050.609915461,268760.921697317,728726.416080169,2035836.77565624],
"poly(width, 4)4":[68946.8246073397,192776.954107941,330090.835537141,1257096.02990554,6051182.10521491],
"poly(sale_year, 4)1":[-15719.6123682441,-17140.6025740095,-21131.0944837755,-261369.971238755,-1116896.25596427],
"poly(sale_year, 4)2":[-9947.41458092418,-5886.61092800762,-20436.9558879193,-8305.70534224297,-2911524.72914606],
"poly(sale_year, 4)3":[-823.851064400753,-12707.6295179287,-12217.1864128598,-34371.9865134683,384775.036545456],
"poly(sale_year, 4)4":[-3022.90272352726,6524.1805561132,5225.32022078024,-45924.8808845479,1578564.95841246],
"prov":[750.399421679246,1366.52142698044,4333.6749726101,18690.127544594,-25491.1864489863],
"certificate":[-765.952983896595,-1414.55320772101,-2483.6309166811,9352.97398815103,-7037.98694465592],
"mediumpainting":[133446.072148692,317310.108883052,425799.200313375,505869.15054237,2455065.38075147],
"mediumpaper":[1361.35903003212,531.970247375247,396.99671061662,529.666382314523,-77303.554820332],}

### Lam ###
c_lam ={"(Intercept)":[21518.671974845,38903.5428257746,70385.8593585945,123225.569537096,426958.731631729],
"poly(year, 4)1":[-45571.1464403018,-108423.402029938,-181104.747485682,-337156.290375311,-2422735.0306125],
"poly(year, 4)2":[-2735.2373196307,-43400.5578473789,-37559.8444775268,-70974.8723214031,279457.421451866],
"poly(year, 4)3":[28583.4462231482,94955.7480956393,194905.562126664,329035.923902861,1101161.47579455],
"poly(year, 4)4":[-46288.7613833319,-105546.381067233,-115395.854243494,-191276.636488046,-1010484.16244542],
"poly(height, 4)1":[1096101.29649551,1634774.86886405,3470286.93262411,4721582.38976055,16293413.9795134],
"poly(height, 4)2":[876929.833145557,1316903.86388872,3527609.46542741,3702450.37965734,7277572.30377091],
"poly(height, 4)3":[124298.6081078,311477.571960547,1163846.6357685,78854.0368558259,-4752109.276736],
"poly(height, 4)4":[-53574.9213397818,-6126.21287255779,139097.767537408,-462635.45323914,-2187579.57995237],
"poly(width, 4)1":[321484.675669773,720597.23313727,1229095.3640883,1983936.92954866,-1389642.85944965],
"poly(width, 4)2":[115092.806606373,312727.389473165,513709.95458807,718844.645341228,-808350.218890687],
"poly(width, 4)3":[-232570.949259889,-598060.965685793,-1033427.01745639,-1577594.60742585,935476.628875244],
"poly(width, 4)4":[-124098.264368634,-381397.011310857,-609668.37727408,-933312.781437821,1091832.4401581],
"poly(sale_year, 4)1":[33045.3877110051,118133.906667843,155731.461021057,210854.206754071,537602.555471617],
"poly(sale_year, 4)2":[-79679.365300166,-97496.2616355945,-74060.692287693,-128221.042605699,431108.385672962],
"poly(sale_year, 4)3":[-5490.70208204875,-22347.5188355426,21638.6165961269,46014.527681002,948609.810407478],
"poly(sale_year, 4)4":[30893.7680515651,50379.8279216783,35410.6281430018,74965.7340511253,867473.334168518],
"prov":[1971.74539682291,464.781538955319,773.80833619843,398.101238730207,522983.64525678],
"certificate":[3390.78454103482,4218.65377382535,10269.3762228049,20185.0139817357,38330.9643047247],
"mediumpainting":[24917.0276455577,44898.9141778316,62537.0881019283,69341.5501699274,95844.5738728972],
"mediumpaper":[3387.73188437334,1028.47253957743,-686.895028818716,-12190.6647744453,1497.18255246019],}


cruz = 'poly_CarlosCruzDiez.csv'
carrington = 'poly_Carrington.csv'
bermudez = 'poly_CundoBermudez.csv'
rivera = 'poly_DiegoRivera.csv'
orozco = 'poly_Orozco.csv'
coronel = 'poly_PedroCoronel.csv'
tamayo = 'poly_Tamayo.csv'
lam = 'poly_WifredoLam.csv'
siqueiros = 'poly_Siqueiros.csv'
openlist = (cruz, carrington, bermudez, rivera, orozco, coronel, tamayo, lam, siqueiros)
j = 0
poly_list = []
poly_dict = {}
for i in openlist:
    reader = csv.reader(open(i))
    year = {}
    sale_year = {}
    height = {}
    width = {}
    for row in reader:
        key1 = row[1]
        key2 = row[6]
        key3 = row[11]
        key4 = row[16]
        if key1 in year:
            pass
        year[key1] = row[2:6]
        if key2 in sale_year:
            # implement your duplicate row handling here
            pass
        sale_year[key2] = row[7:11]
        if key3 in height:
            # implement your duplicate row handling here
            pass
        height[key3] = row[12:16]
        if key4 in width:
            # implement your duplicate row handling here
            pass
        width[key4] = row[17:21]
        #print year
        # print sale_year
        # print width
        # print height
        j += 1
        # print j
    # assign dictionary to values ##
    poly_dict[i] = [year, sale_year, height, width]
    # clean data and convert to floats #
    del poly_dict[i][1]['sale_year']
    del poly_dict[i][0]['year']
    del poly_dict[i][2]['height']
    del poly_dict[i][3]['width']
    poly_dict[i][0] = {float(k):[float(i) for i in v] for k,v in poly_dict[i][0].items()}
    poly_dict[i][1] = {float(k):[float(i) for i in v] for k,v in poly_dict[i][1].items()}
    poly_dict[i][2] = {float(k):[float(i) for i in v] for k,v in poly_dict[i][2].items()}
    poly_dict[i][3] = {float(k):[float(i) for i in v] for k,v in poly_dict[i][3].items()}

def price_estimation(input_artist, input_year, input_height, input_width, materials, quality):
    intercept = 1
    certificate = 1
    input_sale_year = 2015
    i = quality

    ## place artist name to relevant categories ##
    if input_artist == "Leonora Carrington":
        c = c_carrington
        artist_poly = carrington
    elif input_artist == "Diego Rivera":
        c = c_rivera
        artist_poly = rivera
    elif input_artist == "Carlos Cruz Diez":
        c = c_cruz
        artist_poly = cruz
    elif input_artist == "Cundo Bermudez":
        c = c_bermudez
        artist_poly = bermudez
    elif input_artist == "Jose Clemente Orozco":
        c = c_orozco
        artist_poly = orozco
    elif input_artist == "Pedro Coronel":
        c = c_coronel
        artist_poly = coronel
    elif input_artist == "David Alfaro Siqueiros":
        c = c_siqueiros
        artist_poly = siqueiros
    elif input_artist == "Rufino Tamayo":
        c = c_tamayo
        artist_poly = tamayo
    elif input_artist == "Wifredo Lam":
        c = c_lam
        artist_poly = lam
    else:
        c = c_rivera
        artist_poly = rivera



    if materials == 'painting':
        mediumpaper = 0
        mediumpainting = 1
    elif materials == 'paper':
        mediumpaper = 1
        mediumpainting = 0
    else:
        mediumpaper = 0
        mediumpainting = 0

    if quality<3:
        prov = 0
    elif quality<4:
        prov = 3
    else:
        prov = 7


    ### assigning polynomial values to inputs ### 
    year_list = poly_dict[cruz][0].keys()
    a = min(year_list, key=lambda x:abs(x-input_year))
    year = poly_dict[artist_poly][0][a][0]
    year2 = poly_dict[artist_poly][0][a][1]
    year3 = poly_dict[artist_poly][0][a][2]
    year4 = poly_dict[artist_poly][0][a][3]

    sale_year_list = poly_dict[artist_poly][1].keys()
    a = min(sale_year_list, key=lambda x:abs(x-input_sale_year))
    sale_year = poly_dict[artist_poly][1][a][0]
    sale_year2 = poly_dict[artist_poly][1][a][1]
    sale_year3 = poly_dict[artist_poly][1][a][2]
    sale_year4 = poly_dict[artist_poly][1][a][3]

    height_list = poly_dict[artist_poly][2].keys()
    a = min(height_list, key=lambda x:abs(x-input_height))
    height = poly_dict[artist_poly][2][a][0]
    height2 = poly_dict[artist_poly][2][a][1]
    height3 = poly_dict[artist_poly][2][a][2]
    height4 = poly_dict[artist_poly][2][a][3]

    width_list = poly_dict[artist_poly][3].keys()
    a = min(width_list, key=lambda x:abs(x-input_width))
    width = poly_dict[artist_poly][3][a][0]
    width2 = poly_dict[artist_poly][3][a][1]
    width3 = poly_dict[artist_poly][3][a][2]
    width4 = poly_dict[artist_poly][3][a][3]


    ###  estimation equation ###
    result = (c['(Intercept)'][i]*intercept + c['poly(year, 4)1'][i]*year + c['poly(year, 4)2'][i]*year2 + c['poly(year, 4)3'][i]*(year3) + c['poly(year, 4)4'][i]*year4
    + c['poly(height, 4)1'][i]*height + c['poly(height, 4)2'][i]*height2 + c['poly(height, 4)3'][i]*height3 + c['poly(height, 4)4'][i]*height4
    + c['poly(width, 4)1'][i]*width + c['poly(width, 4)2'][i]*width2 + c['poly(width, 4)3'][i]*width3 + c['poly(width, 4)4'][i]*width4
    + c['poly(sale_year, 4)1'][i]*sale_year + c['poly(sale_year, 4)2'][i]*(sale_year2) + c['poly(sale_year, 4)3'][i]*(sale_year3) + c['poly(sale_year, 4)4'][i]*(sale_year4)
    + c['prov'][i]*prov + c['certificate'][i]*certificate + c['mediumpainting'][i]*mediumpainting + c['mediumpaper'][i]*mediumpaper)
    #return result

    return result 


input_artist = "Leonora Carrington"
input_year = 1990

input_height = 20
input_width = 20
intercept = 1
materials = 'painting'
quality = 0

print price_estimation(input_artist, input_year, input_height, input_width, materials, quality)
