import unittest
from typing import List


class Solution:
    @staticmethod
    def count_increase_in_measurements(measurements: List[int]):
        result = 0
        for i in range(len(measurements) - 1):
            result += 1 if measurements[i] < measurements[i + 1] else 0
        return result


class Tests(unittest.TestCase):
    @staticmethod
    def _read_input(measurement_text):
        return [int(_) for _ in measurement_text.split()]

    def test_sample_input(self):
        measurements = self._read_input(
            """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
        """
        )
        self.assertEqual(
            7, Solution.count_increase_in_measurements(measurements=measurements)
        )

    def test_real_problem(self):
        measurements = self._read_input(
            """
        187
        195
        199
        218
        221
        222
        219
        225
        226
        227
        222
        223
        238
        239
        242
        252
        273
        276
        259
        260
        273
        278
        299
        310
        313
        320
        314
        313
        323
        325
        333
        335
        344
        336
        339
        340
        369
        367
        374
        378
        369
        365
        398
        395
        396
        397
        398
        421
        429
        456
        464
        489
        490
        491
        486
        461
        462
        477
        490
        492
        493
        500
        501
        518
        520
        528
        557
        558
        559
        561
        578
        579
        585
        587
        597
        595
        603
        599
        597
        612
        613
        619
        621
        630
        607
        628
        631
        647
        652
        653
        654
        660
        683
        684
        694
        719
        720
        724
        728
        732
        740
        741
        757
        767
        768
        770
        771
        777
        799
        810
        811
        817
        837
        845
        868
        870
        872
        874
        880
        887
        895
        902
        910
        913
        914
        924
        908
        940
        957
        959
        960
        967
        969
        971
        987
        988
        990
        998
        981
        979
        981
        997
        1004
        1020
        1021
        1004
        1006
        992
        993
        1001
        1003
        1040
        1041
        1055
        1059
        1073
        1082
        1087
        1093
        1112
        1117
        1120
        1123
        1127
        1142
        1153
        1154
        1155
        1157
        1163
        1162
        1161
        1144
        1137
        1140
        1141
        1134
        1140
        1143
        1141
        1142
        1147
        1150
        1155
        1164
        1166
        1169
        1188
        1191
        1197
        1193
        1197
        1191
        1213
        1214
        1215
        1224
        1236
        1238
        1245
        1237
        1235
        1250
        1291
        1302
        1306
        1307
        1308
        1316
        1319
        1332
        1358
        1388
        1393
        1396
        1403
        1406
        1411
        1412
        1414
        1434
        1439
        1440
        1453
        1452
        1474
        1475
        1504
        1508
        1509
        1511
        1515
        1516
        1519
        1520
        1566
        1565
        1549
        1567
        1582
        1568
        1569
        1572
        1573
        1581
        1590
        1591
        1596
        1606
        1631
        1644
        1641
        1651
        1657
        1659
        1664
        1663
        1662
        1645
        1650
        1657
        1673
        1694
        1695
        1705
        1706
        1708
        1716
        1717
        1719
        1728
        1745
        1746
        1755
        1761
        1769
        1770
        1771
        1773
        1777
        1782
        1783
        1785
        1779
        1795
        1806
        1823
        1830
        1832
        1833
        1830
        1832
        1833
        1817
        1821
        1829
        1839
        1840
        1841
        1838
        1841
        1830
        1816
        1818
        1820
        1825
        1846
        1863
        1862
        1865
        1873
        1876
        1882
        1890
        1897
        1899
        1902
        1906
        1918
        1919
        1909
        1907
        1906
        1907
        1914
        1919
        1917
        1939
        1943
        1948
        1952
        1953
        1970
        1975
        1976
        1989
        1991
        1975
        1979
        1982
        1986
        1984
        1991
        1995
        1993
        1995
        2003
        2004
        2003
        2004
        2005
        2013
        2015
        2017
        2022
        2033
        2040
        2042
        2048
        2056
        2041
        2040
        2046
        2055
        2058
        2057
        2063
        2068
        2065
        2063
        2068
        2069
        2070
        2071
        2072
        2073
        2075
        2082
        2080
        2084
        2090
        2091
        2098
        2090
        2091
        2092
        2093
        2113
        2114
        2110
        2111
        2113
        2114
        2132
        2138
        2139
        2140
        2147
        2150
        2165
        2169
        2171
        2173
        2178
        2182
        2179
        2182
        2198
        2192
        2213
        2227
        2234
        2233
        2248
        2258
        2259
        2260
        2264
        2268
        2265
        2269
        2258
        2287
        2293
        2292
        2293
        2299
        2302
        2285
        2286
        2305
        2310
        2339
        2322
        2326
        2333
        2334
        2352
        2355
        2357
        2362
        2363
        2364
        2376
        2379
        2380
        2381
        2390
        2396
        2397
        2399
        2401
        2407
        2409
        2408
        2412
        2428
        2445
        2459
        2442
        2456
        2458
        2467
        2471
        2496
        2500
        2501
        2502
        2505
        2504
        2505
        2506
        2507
        2509
        2511
        2519
        2538
        2540
        2550
        2549
        2564
        2570
        2571
        2572
        2573
        2586
        2594
        2590
        2598
        2599
        2602
        2603
        2608
        2612
        2607
        2619
        2629
        2636
        2612
        2615
        2619
        2632
        2633
        2639
        2624
        2627
        2633
        2634
        2635
        2632
        2655
        2657
        2674
        2678
        2680
        2674
        2675
        2674
        2678
        2670
        2688
        2692
        2699
        2707
        2724
        2731
        2742
        2744
        2746
        2747
        2748
        2750
        2753
        2758
        2759
        2768
        2771
        2775
        2766
        2768
        2773
        2767
        2766
        2765
        2766
        2771
        2783
        2784
        2799
        2800
        2801
        2806
        2813
        2814
        2806
        2811
        2830
        2836
        2850
        2854
        2861
        2862
        2866
        2874
        2875
        2880
        2886
        2877
        2885
        2889
        2916
        2912
        2914
        2915
        2941
        2956
        2957
        2959
        2968
        2969
        2973
        2979
        2993
        2997
        2994
        2995
        3004
        3012
        3021
        3022
        3026
        3028
        3030
        3033
        3031
        3032
        3038
        3034
        3048
        3049
        3063
        3064
        3061
        3071
        3059
        3062
        3073
        3071
        3072
        3075
        3076
        3082
        3085
        3097
        3099
        3101
        3105
        3108
        3112
        3142
        3144
        3145
        3146
        3134
        3139
        3176
        3183
        3187
        3193
        3194
        3197
        3194
        3195
        3175
        3189
        3195
        3196
        3206
        3200
        3193
        3199
        3201
        3229
        3236
        3250
        3263
        3267
        3290
        3291
        3293
        3303
        3307
        3309
        3311
        3308
        3300
        3307
        3309
        3334
        3337
        3354
        3353
        3372
        3384
        3395
        3396
        3395
        3396
        3392
        3393
        3397
        3398
        3399
        3397
        3399
        3400
        3402
        3408
        3430
        3432
        3434
        3426
        3447
        3470
        3475
        3478
        3477
        3478
        3481
        3484
        3487
        3496
        3514
        3519
        3515
        3516
        3518
        3533
        3536
        3521
        3522
        3517
        3521
        3530
        3531
        3540
        3539
        3552
        3553
        3561
        3587
        3594
        3603
        3647
        3651
        3687
        3684
        3693
        3692
        3693
        3701
        3703
        3704
        3697
        3677
        3669
        3670
        3672
        3674
        3675
        3680
        3683
        3686
        3688
        3687
        3706
        3709
        3717
        3698
        3712
        3720
        3722
        3734
        3747
        3750
        3793
        3797
        3799
        3803
        3804
        3818
        3817
        3819
        3820
        3819
        3820
        3824
        3822
        3857
        3862
        3877
        3880
        3881
        3888
        3880
        3862
        3863
        3872
        3873
        3877
        3879
        3881
        3889
        3890
        3893
        3894
        3889
        3888
        3892
        3894
        3895
        3891
        3887
        3898
        3884
        3890
        3895
        3896
        3897
        3920
        3921
        3918
        3919
        3921
        3935
        3945
        3947
        3950
        3958
        3963
        3959
        3961
        3982
        3984
        3987
        4006
        4007
        4009
        4010
        4011
        4012
        4039
        4038
        4041
        4044
        4051
        4054
        4055
        4053
        4055
        4065
        4080
        4088
        4090
        4120
        4123
        4127
        4128
        4135
        4136
        4141
        4142
        4146
        4136
        4153
        4163
        4165
        4161
        4171
        4175
        4176
        4169
        4195
        4222
        4220
        4221
        4216
        4233
        4219
        4222
        4217
        4222
        4241
        4248
        4249
        4243
        4246
        4241
        4245
        4250
        4253
        4254
        4255
        4257
        4261
        4260
        4280
        4288
        4290
        4299
        4303
        4318
        4322
        4323
        4331
        4334
        4352
        4354
        4356
        4368
        4369
        4370
        4371
        4372
        4376
        4367
        4368
        4402
        4405
        4406
        4427
        4428
        4431
        4447
        4445
        4450
        4457
        4458
        4464
        4462
        4488
        4490
        4492
        4495
        4499
        4486
        4488
        4492
        4493
        4494
        4498
        4500
        4509
        4511
        4512
        4522
        4531
        4535
        4561
        4562
        4564
        4565
        4597
        4603
        4619
        4617
        4618
        4619
        4620
        4624
        4625
        4629
        4644
        4668
        4671
        4674
        4676
        4680
        4687
        4688
        4697
        4702
        4706
        4710
        4711
        4712
        4718
        4719
        4721
        4722
        4723
        4740
        4748
        4758
        4759
        4763
        4765
        4774
        4783
        4817
        4824
        4828
        4829
        4830
        4838
        4842
        4846
        4853
        4854
        4853
        4861
        4871
        4872
        4874
        4875
        4877
        4879
        4890
        4895
        4897
        4923
        4949
        4952
        4954
        4959
        4969
        4970
        4979
        4978
        4980
        4964
        4986
        4978
        4981
        4986
        4987
        4988
        4994
        4986
        4988
        4998
        5001
        5032
        5035
        5016
        5018
        5023
        5025
        5047
        5046
        5049
        5076
        5073
        5074
        5081
        5085
        5089
        5091
        5095
        5098
        5100
        5104
        5105
        5091
        5093
        5104
        5083
        5087
        5092
        5094
        5095
        5096
        5099
        5102
        5101
        5108
        5101
        5106
        5112
        5113
        5121
        5127
        5130
        5132
        5138
        5131
        5119
        5120
        5122
        5127
        5116
        5114
        5115
        5116
        5117
        5115
        5120
        5127
        5131
        5130
        5134
        5135
        5167
        5177
        5183
        5185
        5216
        5221
        5220
        5221
        5228
        5231
        5232
        5229
        5228
        5230
        5234
        5231
        5232
        5236
        5238
        5242
        5247
        5264
        5263
        5265
        5270
        5279
        5283
        5290
        5298
        5301
        5305
        5307
        5303
        5320
        5331
        5344
        5364
        5365
        5374
        5381
        5388
        5390
        5392
        5413
        5418
        5425
        5428
        5441
        5442
        5445
        5446
        5445
        5450
        5449
        5453
        5462
        5463
        5473
        5470
        5469
        5468
        5476
        5485
        5487
        5494
        5484
        5486
        5509
        5525
        5533
        5531
        5532
        5537
        5540
        5537
        5538
        5561
        5555
        5557
        5559
        5563
        5564
        5565
        5569
        5571
        5576
        5579
        5581
        5585
        5578
        5579
        5574
        5590
        5591
        5593
        5602
        5609
        5622
        5623
        5632
        5638
        5640
        5645
        5648
        5653
        5677
        5678
        5688
        5684
        5695
        5704
        5713
        5715
        5722
        5723
        5732
        5741
        5743
        5746
        5749
        5748
        5750
        5778
        5784
        5779
        5778
        5787
        5783
        5785
        5791
        5797
        5819
        5804
        5805
        5836
        5844
        5849
        5848
        5849
        5853
        5856
        5854
        5855
        5860
        5861
        5859
        5883
        5893
        5928
        5929
        5935
        5948
        5954
        5959
        5961
        5956
        5959
        5974
        5983
        5985
        5999
        6000
        6002
        6003
        6004
        6006
        6011
        6024
        6043
        6045
        6048
        6049
        6033
        6043
        6058
        6059
        6062
        6063
        6046
        6051
        6052
        6054
        6059
        6060
        6066
        6092
        6104
        6106
        6107
        6110
        6127
        6143
        6149
        6187
        6181
        6184
        6185
        6201
        6203
        6204
        6230
        6229
        6232
        6238
        6239
        6241
        6262
        6239
        6244
        6233
        6234
        6239
        6241
        6244
        6245
        6243
        6253
        6267
        6269
        6270
        6268
        6262
        6265
        6266
        6268
        6270
        6271
        6274
        6275
        6273
        6274
        6276
        6285
        6297
        6298
        6313
        6314
        6309
        6319
        6331
        6340
        6360
        6361
        6370
        6382
        6393
        6395
        6396
        6399
        6401
        6403
        6417
        6392
        6396
        6408
        6409
        6410
        6423
        6424
        6425
        6430
        6444
        6430
        6429
        6428
        6432
        6440
        6445
        6451
        6453
        6455
        6468
        6475
        6481
        6480
        6503
        6506
        6513
        6514
        6495
        6490
        6489
        6493
        6494
        6495
        6516
        6525
        6531
        6553
        6552
        6553
        6554
        6562
        6573
        6572
        6583
        6582
        6584
        6589
        6586
        6587
        6588
        6591
        6599
        6614
        6619
        6629
        6641
        6645
        6646
        6673
        6701
        6730
        6732
        6733
        6732
        6733
        6734
        6762
        6763
        6765
        6787
        6784
        6799
        6812
        6825
        6826
        6838
        6872
        6873
        6877
        6865
        6875
        6879
        6880
        6885
        6886
        6889
        6896
        6931
        6933
        6950
        6953
        6956
        6959
        6962
        6964
        6965
        6966
        6965
        6966
        6969
        6971
        6973
        6997
        7012
        7020
        7021
        7017
        7033
        7050
        7048
        7054
        7051
        7025
        7029
        7039
        7042
        7043
        7044
        7053
        7070
        7066
        7069
        7072
        7075
        7076
        7077
        7083
        7091
        7089
        7095
        7114
        7109
        7111
        7117
        7118
        7116
        7158
        7159
        7167
        7174
        7177
        7187
        7198
        7204
        7207
        7210
        7211
        7216
        7213
        7224
        7222
        7225
        7258
        7268
        7271
        7270
        7271
        7264
        7291
        7295
        7315
        7332
        7333
        7335
        7342
        7332
        7330
        7345
        7352
        7353
        7366
        7367
        7365
        7361
        7370
        7398
        7391
        7398
        7399
        7406
        7420
        7418
        7420
        7422
        7426
        7435
        7426
        7423
        7421
        7425
        7427
        7429
        7446
        7448
        7447
        7444
        7449
        7450
        7453
        7457
        7474
        7476
        7479
        7481
        7512
        7513
        7517
        7522
        7527
        7549
        7554
        7551
        7533
        7534
        7535
        7557
        7562
        7560
        7576
        7571
        7574
        7583
        7580
        7582
        7584
        7593
        7579
        7571
        7593
        7594
        7599
        7600
        7601
        7602
        7629
        7630
        7636
        7637
        7658
        7666
        7673
        7686
        7688
        7689
        7687
        7695
        7697
        7698
        7702
        7705
        7702
        7705
        7708
        7718
        7720
        7730
        7753
        7752
        7751
        7752
        7753
        7748
        7751
        7755
        7754
        7755
        7725
        7742
        7751
        7761
        7762
        7769
        7774
        7776
        7780
        7805
        7822
        7825
        7843
        7834
        7848
        7851
        7849
        7851
        7862
        7858
        7861
        7862
        7861
        7863
        7864
        7866
        7889
        7878
        7899
        7911
        7913
        7915
        7916
        7921
        7938
        7948
        7937
        7944
        7935
        7936
        7933
        7954
        7964
        7958
        7960
        7980
        7985
        8004
        8008
        8015
        7993
        7994
        7996
        8001
        8017
        8029
        8065
        8074
        8085
        8090
        8098
        8109
        8114
        8116
        8123
        8140
        8139
        8141
        8139
        8142
        8151
        8154
        8160
        8169
        8162
        8168
        8170
        8188
        8189
        8190
        8192
        8189
        8190
        8198
        8197
        8200
        8201
        8209
        8222
        8225
        8226
        8227
        8232
        8236
        8232
        8235
        8234
        8235
        8236
        8237
        8256
        8289
        8280
        8289
        8273
        8268
        8283
        8287
        8288
        8299
        8300
        8323
        8335
        8336
        8343
        8345
        8346
        8348
        8379
        8388
        8389
        8390
        8395
        8420
        8422
        8423
        8425
        8426
        8429
        8422
        8432
        8440
        8436
        8447
        8460
        8464
        8466
        8480
        8481
        8482
        8484
        8481
        8477
        8478
        8466
        8473
        8477
        8482
        8483
        8495
        8516
        8518
        8525
        8548
        8552
        8553
        8559
        8557
        8556
        8546
        8545
        8546
        8547
        8549
        8553
        8546
        8548
        8549
        8553
        8556
        8566
        8565
        8571
        8573
        8572
        8583
        8584
        8587
        8585
        8573
        8574
        8585
        8592
        8601
        8603
        8618
        8619
        8615
        8619
        8615
        8616
        8617
        8619
        8629
        8653
        8640
        8644
        8666
        8667
        8684
        8687
        8689
        8678
        8693
        8700
        8731
        8744
        8729
        8717
        8718
        8748
        8757
        8758
        8756
        8757
        8734
        8752
        8753
        8756
        8749
        8750
        8751
        8759
        8779
        8783
        8789
        8790
        8815
        8829
        8846
        8857
        8859
        8860
        8867
        8859
        8866
        8890
        8889
        8890
        8895
        8896
        8901
        8903
        8904
        8907
        8899
        8915
        8919
        8937
        8915
        8928
        8936
        8942
        8943
        8944
        8951
        8941
        8942
        8949
        8953
        8960
        8958
        8977
        8979
        8999
        9000
        9017
        9018
        9019
        9018
        9019
        9025
        9038
        9040
        9042
        9043
        9042
        9050
        9051
        9052
        9055
        9056
        9055
        9056
        9057
        9066
        9067
        9075
        9069
        9072
        9073
        9083
        9084
        9094
        9104
        9114
        9122
        9125
        9143
        9144
        9148
        9135
        9136
        9137
        9139
        9147
        9145
        9151
        9154
        9156
        9173
        9175
        9176
        9174
        9176
        9170
        9168
        9179
        9174
        9176
        9175
        9203
        9224
        9228
        9239
        9253
        9254
        9269
        9284
        9283
        9299
        9301
        9302
        9317
        9322
        9323
        9320
        9326
        9327
        9339
        9337
        9336
        9347
        9366
        9386
        9410
        9412
        9416
        9404
        9405
        9396
        9397
        9409
        9410
        9427
        9448
        9450
        9486
        9528
        9536
        9553
        9556
        9569
        9572
        9575
        9597
        9600
        9606
        9609
        9601
        9604
        9615
        9622
        9625
        9630
        9643
        9636
        9639
        9641
        9643
        9635
        9637
        9638
        9652
        9651
        9643
        9644
        9645
        9646
        9633
        9635
        9636
        9638
        9639
        9640
        9612
        9604
        9607
        9626
        9646
        9654
        9655
        9657
        9635
        9643
        9645
        9667
        9664
        9665
        9666
        9671
        9674
        9683
        9684
        9713
        9726
        9735
        9737
        9752
        9745
        """
        )
        print(Solution.count_increase_in_measurements(measurements=measurements))
