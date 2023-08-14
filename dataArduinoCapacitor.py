import numpy as np
import matplotlib.pyplot as plt
import math

from scipy.optimize import curve_fit


# Bloque de datos en una sola línea
data_str = "tiempo:0.04,voltaje10bits:17,voltaje:0.093,tiempo:0.09,voltaje10bits:27,voltaje:0.147,tiempo:0.13,voltaje10bits:38,voltaje:0.200,tiempo:0.17,voltaje10bits:48,voltaje:0.239,tiempo:0.22,voltaje10bits:56,voltaje:0.288,tiempo:0.26,voltaje10bits:66,voltaje:0.342,tiempo:0.31,voltaje10bits:77,voltaje:0.386,tiempo:0.35,voltaje10bits:86,voltaje:0.430,tiempo:0.40,voltaje10bits:96,voltaje:0.474,tiempo:0.44,voltaje10bits:104,voltaje:0.518,tiempo:0.49,voltaje10bits:113,voltaje:0.562,tiempo:0.53,voltaje10bits:122,voltaje:0.611,tiempo:0.58,voltaje10bits:131,voltaje:0.655,tiempo:0.63,voltaje10bits:140,voltaje:0.694,tiempo:0.67,voltaje10bits:149,voltaje:0.738,tiempo:0.72,voltaje10bits:157,voltaje:0.777,tiempo:0.76,voltaje10bits:166,voltaje:0.821,tiempo:0.81,voltaje10bits:174,voltaje:0.860,tiempo:0.85,voltaje10bits:182,voltaje:0.904,tiempo:0.90,voltaje10bits:191,voltaje:0.943,tiempo:0.95,voltaje10bits:199,voltaje:0.978,tiempo:0.99,voltaje10bits:206,voltaje:1.017,tiempo:1.04,voltaje10bits:215,voltaje:1.056,tiempo:1.08,voltaje10bits:222,voltaje:1.095,tiempo:1.13,voltaje10bits:230,voltaje:1.134,tiempo:1.17,voltaje10bits:237,voltaje:1.173,tiempo:1.22,voltaje10bits:246,voltaje:1.207,tiempo:1.27,voltaje10bits:253,voltaje:1.241,tiempo:1.31,voltaje10bits:260,voltaje:1.281,tiempo:1.36,voltaje10bits:267,voltaje:1.315,tiempo:1.40,voltaje10bits:275,voltaje:1.354,tiempo:1.45,voltaje10bits:281,voltaje:1.383,tiempo:1.49,voltaje10bits:289,voltaje:1.422,tiempo:1.54,voltaje10bits:296,voltaje:1.457,tiempo:1.59,voltaje10bits:303,voltaje:1.486,tiempo:1.63,voltaje10bits:309,voltaje:1.520,tiempo:1.68,voltaje10bits:316,voltaje:1.554,tiempo:1.72,voltaje10bits:324,voltaje:1.588,tiempo:1.77,voltaje10bits:331,voltaje:1.623,tiempo:1.82,voltaje10bits:337,voltaje:1.652,tiempo:1.86,voltaje10bits:343,voltaje:1.681,tiempo:1.91,voltaje10bits:349,voltaje:1.716,tiempo:1.95,voltaje10bits:356,voltaje:1.745,tiempo:2.00,voltaje10bits:362,voltaje:1.779,tiempo:2.04,voltaje10bits:368,voltaje:1.808,tiempo:2.09,voltaje10bits:374,voltaje:1.838,tiempo:2.14,voltaje10bits:381,voltaje:1.867,tiempo:2.18,voltaje10bits:387,voltaje:1.896,tiempo:2.23,voltaje10bits:393,voltaje:1.926,tiempo:2.27,voltaje10bits:399,voltaje:1.960,tiempo:2.32,voltaje10bits:405,voltaje:1.984,tiempo:2.36,voltaje10bits:410,voltaje:2.014,tiempo:2.41,voltaje10bits:416,voltaje:2.043,tiempo:2.46,voltaje10bits:422,voltaje:2.072,tiempo:2.50,voltaje10bits:428,voltaje:2.097,tiempo:2.55,voltaje10bits:433,voltaje:2.126,tiempo:2.59,voltaje10bits:439,voltaje:2.151,tiempo:2.64,voltaje10bits:444,voltaje:2.180,tiempo:2.68,voltaje10bits:449,voltaje:2.204,tiempo:2.73,voltaje10bits:455,voltaje:2.229,tiempo:2.78,voltaje10bits:460,voltaje:2.258,tiempo:2.82,voltaje10bits:465,voltaje:2.283,tiempo:2.87,voltaje10bits:471,voltaje:2.307,tiempo:2.91,voltaje10bits:476,voltaje:2.331,tiempo:2.96,voltaje10bits:481,voltaje:2.361,tiempo:3.00,voltaje10bits:486,voltaje:2.380,tiempo:3.05,voltaje10bits:492,voltaje:2.405,tiempo:3.10,voltaje10bits:496,voltaje:2.429,tiempo:3.14,voltaje10bits:501,voltaje:2.454,tiempo:3.19,voltaje10bits:506,voltaje:2.478,tiempo:3.23,voltaje10bits:510,voltaje:2.502,tiempo:3.28,voltaje10bits:516,voltaje:2.527,tiempo:3.32,voltaje10bits:520,voltaje:2.546,tiempo:3.37,voltaje10bits:524,voltaje:2.571,tiempo:3.42,voltaje10bits:530,voltaje:2.590,tiempo:3.46,voltaje10bits:534,voltaje:2.615,tiempo:3.51,voltaje10bits:538,voltaje:2.639,tiempo:3.55,voltaje10bits:543,voltaje:2.659,tiempo:3.60,voltaje10bits:548,voltaje:2.683,tiempo:3.65,voltaje10bits:552,voltaje:2.703,tiempo:3.69,voltaje10bits:556,voltaje:2.722,tiempo:3.74,voltaje10bits:560,voltaje:2.747,tiempo:3.78,voltaje10bits:565,voltaje:2.766,tiempo:3.83,voltaje10bits:569,voltaje:2.786,tiempo:3.87,voltaje10bits:573,voltaje:2.805,tiempo:3.92,voltaje10bits:577,voltaje:2.825,tiempo:3.97,voltaje10bits:582,voltaje:2.849,tiempo:4.01,voltaje10bits:585,voltaje:2.869,tiempo:4.06,voltaje10bits:590,voltaje:2.889,tiempo:4.10,voltaje10bits:593,voltaje:2.908,tiempo:4.15,voltaje10bits:598,voltaje:2.928,tiempo:4.19,voltaje10bits:602,voltaje:2.947,tiempo:4.24,voltaje10bits:605,voltaje:2.962,tiempo:4.29,voltaje10bits:609,voltaje:2.986,tiempo:4.33,voltaje10bits:613,voltaje:3.006,tiempo:4.38,voltaje10bits:617,voltaje:3.016,tiempo:4.42,voltaje10bits:620,voltaje:3.035,tiempo:4.47,voltaje10bits:624,voltaje:3.055,tiempo:4.51,voltaje10bits:628,voltaje:3.074,tiempo:4.56,voltaje10bits:631,voltaje:3.089,tiempo:4.61,voltaje10bits:635,voltaje:3.109,tiempo:4.65,voltaje10bits:639,voltaje:3.123,tiempo:4.70,voltaje10bits:642,voltaje:3.143,tiempo:4.74,voltaje10bits:646,voltaje:3.162,tiempo:4.79,voltaje10bits:649,voltaje:3.177,tiempo:4.83,voltaje10bits:652,voltaje:3.192,tiempo:4.88,voltaje10bits:656,voltaje:3.211,tiempo:4.93,voltaje10bits:659,voltaje:3.231,tiempo:4.97,voltaje10bits:663,voltaje:3.245,tiempo:5.02,voltaje10bits:666,voltaje:3.260,tiempo:5.06,voltaje10bits:669,voltaje:3.275,tiempo:5.11,voltaje10bits:671,voltaje:3.289,tiempo:5.15,voltaje10bits:675,voltaje:3.309,tiempo:5.20,voltaje10bits:679,voltaje:3.314,tiempo:5.25,voltaje10bits:682,voltaje:3.338,tiempo:5.29,voltaje10bits:685,voltaje:3.353,tiempo:5.34,voltaje10bits:687,voltaje:3.363,tiempo:5.38,voltaje10bits:690,voltaje:3.382,tiempo:5.43,voltaje10bits:694,voltaje:3.397,tiempo:5.47,voltaje10bits:697,voltaje:3.416,tiempo:5.52,voltaje10bits:700,voltaje:3.426,tiempo:5.57,voltaje10bits:703,voltaje:3.436,tiempo:5.61,voltaje10bits:705,voltaje:3.451,tiempo:5.66,voltaje10bits:708,voltaje:3.465,tiempo:5.70,voltaje10bits:712,voltaje:3.480,tiempo:5.75,voltaje10bits:714,voltaje:3.495,tiempo:5.80,voltaje10bits:717,voltaje:3.509,tiempo:5.84,voltaje10bits:720,voltaje:3.524,tiempo:5.89,voltaje10bits:722,voltaje:3.534,tiempo:5.93,voltaje10bits:725,voltaje:3.548,tiempo:5.98,voltaje10bits:728,voltaje:3.558,tiempo:6.02,voltaje10bits:730,voltaje:3.573,tiempo:6.07,voltaje10bits:733,voltaje:3.587,tiempo:6.12,voltaje10bits:735,voltaje:3.602,tiempo:6.16,voltaje10bits:739,voltaje:3.612,tiempo:6.21,voltaje10bits:741,voltaje:3.622,tiempo:6.25,voltaje10bits:743,voltaje:3.636,tiempo:6.30,voltaje10bits:745,voltaje:3.651,tiempo:6.34,voltaje10bits:749,voltaje:3.661,tiempo:6.39,voltaje10bits:750,voltaje:3.671,tiempo:6.44,voltaje10bits:753,voltaje:3.680,tiempo:6.48,voltaje10bits:756,voltaje:3.700,tiempo:6.53,voltaje10bits:759,voltaje:3.710,tiempo:6.57,voltaje10bits:761,voltaje:3.719,tiempo:6.62,voltaje10bits:763,voltaje:3.729,tiempo:6.66,voltaje10bits:765,voltaje:3.744,tiempo:6.71,voltaje10bits:767,voltaje:3.754,tiempo:6.76,voltaje10bits:770,voltaje:3.768,tiempo:6.80,voltaje10bits:772,voltaje:3.778,tiempo:6.85,voltaje10bits:774,voltaje:3.788,tiempo:6.89,voltaje10bits:777,voltaje:3.798,tiempo:6.94,voltaje10bits:779,voltaje:3.807,tiempo:6.98,voltaje10bits:781,voltaje:3.817,tiempo:7.03,voltaje10bits:783,voltaje:3.832,tiempo:7.08,voltaje10bits:785,voltaje:3.842,tiempo:7.12,voltaje10bits:787,voltaje:3.851,tiempo:7.17,voltaje10bits:789,voltaje:3.861,tiempo:7.21,voltaje10bits:791,voltaje:3.871,tiempo:7.26,voltaje10bits:794,voltaje:3.886,tiempo:7.30,voltaje10bits:795,voltaje:3.891,tiempo:7.35,voltaje10bits:798,voltaje:3.900,tiempo:7.40,voltaje10bits:799,voltaje:3.910,tiempo:7.44,voltaje10bits:802,voltaje:3.915,tiempo:7.49,voltaje10bits:803,voltaje:3.930,tiempo:7.53,voltaje10bits:806,voltaje:3.939,tiempo:7.58,voltaje10bits:807,voltaje:3.949,tiempo:7.62,voltaje10bits:810,voltaje:3.954,tiempo:7.67,voltaje10bits:811,voltaje:3.964,tiempo:7.72,voltaje10bits:813,voltaje:3.978,tiempo:7.76,voltaje10bits:815,voltaje:3.983,tiempo:7.81,voltaje10bits:816,voltaje:3.993,tiempo:7.85,voltaje10bits:818,voltaje:4.003,tiempo:7.90,voltaje10bits:820,voltaje:4.013,tiempo:7.95,voltaje10bits:823,voltaje:4.027,tiempo:7.99,voltaje10bits:823,voltaje:4.027,tiempo:8.04,voltaje10bits:826,voltaje:4.042,tiempo:8.08,voltaje10bits:827,voltaje:4.052,tiempo:8.13,voltaje10bits:828,voltaje:4.057,tiempo:8.17,voltaje10bits:831,voltaje:4.062,tiempo:8.22,voltaje10bits:833,voltaje:4.066,tiempo:8.27,voltaje10bits:834,voltaje:4.076,tiempo:8.31,voltaje10bits:836,voltaje:4.091,tiempo:8.36,voltaje10bits:838,voltaje:4.096,tiempo:8.40,voltaje10bits:839,voltaje:4.101,tiempo:8.45,voltaje10bits:840,voltaje:4.115,tiempo:8.49,voltaje10bits:842,voltaje:4.115,tiempo:8.54,voltaje10bits:844,voltaje:4.125,tiempo:8.59,voltaje10bits:845,voltaje:4.130,tiempo:8.63,voltaje10bits:847,voltaje:4.145,tiempo:8.68,voltaje10bits:848,voltaje:4.150,tiempo:8.72,voltaje10bits:850,voltaje:4.154,tiempo:8.77,voltaje10bits:851,voltaje:4.164,tiempo:8.81,voltaje10bits:852,voltaje:4.179,tiempo:8.86,voltaje10bits:854,voltaje:4.174,tiempo:8.91,voltaje10bits:856,voltaje:4.189,tiempo:8.95,voltaje10bits:857,voltaje:4.189,tiempo:9.00,voltaje10bits:859,voltaje:4.203,tiempo:9.04,voltaje10bits:860,voltaje:4.203,tiempo:9.09,voltaje10bits:861,voltaje:4.213,tiempo:9.13,voltaje10bits:863,voltaje:4.223,tiempo:9.18,voltaje10bits:864,voltaje:4.223,tiempo:9.23,voltaje10bits:866,voltaje:4.238,tiempo:9.27,voltaje10bits:867,voltaje:4.242,tiempo:9.32,voltaje10bits:869,voltaje:4.247,tiempo:9.36,voltaje10bits:870,voltaje:4.252,tiempo:9.41,voltaje10bits:871,voltaje:4.262,tiempo:9.45,voltaje10bits:872,voltaje:4.267,tiempo:9.50,voltaje10bits:874,voltaje:4.272,tiempo:9.55,voltaje10bits:875,voltaje:4.282,tiempo:9.59,voltaje10bits:877,voltaje:4.286,tiempo:9.64,voltaje10bits:877,voltaje:4.291,tiempo:9.68,voltaje10bits:879,voltaje:4.296,tiempo:9.73,voltaje10bits:881,voltaje:4.301,tiempo:9.78,voltaje10bits:880,voltaje:4.306,tiempo:9.82,voltaje10bits:883,voltaje:4.316,tiempo:9.87,voltaje10bits:884,voltaje:4.316,tiempo:9.91,voltaje10bits:886,voltaje:4.326,tiempo:9.96,voltaje10bits:886,voltaje:4.335,tiempo:10.00,voltaje10bits:887,voltaje:4.335,tiempo:10.05,voltaje10bits:888,voltaje:4.345,tiempo:10.10,voltaje10bits:890,voltaje:4.350,tiempo:10.14,voltaje10bits:891,voltaje:4.355,tiempo:10.19,voltaje10bits:892,voltaje:4.360,tiempo:10.24,voltaje10bits:894,voltaje:4.370,tiempo:10.28,voltaje10bits:894,voltaje:4.370,tiempo:10.33,voltaje10bits:895,voltaje:4.379,tiempo:10.38,voltaje10bits:896,voltaje:4.389,tiempo:10.42,voltaje10bits:898,voltaje:4.389,tiempo:10.47,voltaje10bits:899,voltaje:4.394,tiempo:10.52,voltaje10bits:901,voltaje:4.399,tiempo:10.57,voltaje10bits:901,voltaje:4.404,tiempo:10.61,voltaje10bits:903,voltaje:4.413,tiempo:10.66,voltaje10bits:903,voltaje:4.413,tiempo:10.71,voltaje10bits:904,voltaje:4.423,tiempo:10.75,voltaje10bits:904,voltaje:4.423,tiempo:10.80,voltaje10bits:906,voltaje:4.428,tiempo:10.85,voltaje10bits:907,voltaje:4.433,tiempo:10.89,voltaje10bits:908,voltaje:4.443,tiempo:10.94,voltaje10bits:909,voltaje:4.443,tiempo:10.99,voltaje10bits:910,voltaje:4.448,tiempo:11.03,voltaje10bits:911,voltaje:4.457,tiempo:11.08,voltaje10bits:912,voltaje:4.462,tiempo:11.13,voltaje10bits:912,voltaje:4.462,tiempo:11.17,voltaje10bits:914,voltaje:4.467,tiempo:11.22,voltaje10bits:915,voltaje:4.472,tiempo:11.27,voltaje10bits:916,voltaje:4.482,tiempo:11.31,voltaje10bits:917,voltaje:4.482,tiempo:11.36,voltaje10bits:918,voltaje:4.492,tiempo:11.41,voltaje10bits:919,voltaje:4.492,tiempo:11.45,voltaje10bits:921,voltaje:4.492,tiempo:11.50,voltaje10bits:920,voltaje:4.497,tiempo:11.55,voltaje10bits:921,voltaje:4.501,tiempo:11.59,voltaje10bits:922,voltaje:4.506,tiempo:11.64,voltaje10bits:923,voltaje:4.511,tiempo:11.69,voltaje10bits:924,voltaje:4.516,tiempo:11.73,voltaje10bits:924,voltaje:4.521,tiempo:11.78,voltaje10bits:925,voltaje:4.526,tiempo:11.83,voltaje10bits:927,voltaje:4.531,tiempo:11.88,voltaje10bits:927,voltaje:4.531,tiempo:11.92,voltaje10bits:928,voltaje:4.536,tiempo:11.97,voltaje10bits:929,voltaje:4.541,tiempo:12.02,voltaje10bits:930,voltaje:4.545,tiempo:12.06,voltaje10bits:931,voltaje:4.555,tiempo:12.11,voltaje10bits:931,voltaje:4.550,tiempo:12.16,voltaje10bits:931,voltaje:4.555,tiempo:12.20,voltaje10bits:932,voltaje:4.560,tiempo:12.25,voltaje10bits:933,voltaje:4.560,tiempo:12.30,voltaje10bits:935,voltaje:4.570,tiempo:12.34,voltaje10bits:935,voltaje:4.570,tiempo:12.39,voltaje10bits:936,voltaje:4.575,tiempo:12.44,voltaje10bits:937,voltaje:4.575,tiempo:12.48,voltaje10bits:938,voltaje:4.589,tiempo:12.53,voltaje10bits:938,voltaje:4.585,tiempo:12.58,voltaje10bits:939,voltaje:4.585,tiempo:12.62,voltaje10bits:940,voltaje:4.589,tiempo:12.67,voltaje10bits:941,voltaje:4.594,tiempo:12.72,voltaje10bits:940,voltaje:4.599,tiempo:12.76,voltaje10bits:941,voltaje:4.609,tiempo:12.81,voltaje10bits:943,voltaje:4.604,tiempo:12.86,voltaje10bits:943,voltaje:4.604,tiempo:12.90,voltaje10bits:943,voltaje:4.609,tiempo:12.95,voltaje10bits:944,voltaje:4.619,tiempo:13.00,voltaje10bits:945,voltaje:4.619,tiempo:13.04,voltaje10bits:947,voltaje:4.624,tiempo:13.09,voltaje10bits:946,voltaje:4.624,tiempo:13.14,voltaje10bits:946,voltaje:4.629,tiempo:13.19,voltaje10bits:947,voltaje:4.633,tiempo:13.23,voltaje10bits:948,voltaje:4.633,tiempo:13.28,voltaje10bits:949,voltaje:4.638,tiempo:13.33,voltaje10bits:950,voltaje:4.643,tiempo:13.37,voltaje10bits:950,voltaje:4.648,tiempo:13.42,voltaje10bits:951,voltaje:4.648,tiempo:13.47,voltaje10bits:951,voltaje:4.653,tiempo:13.51,voltaje10bits:951,voltaje:4.653,tiempo:13.56,voltaje10bits:952,voltaje:4.658,tiempo:13.61,voltaje10bits:953,voltaje:4.653,tiempo:13.65,voltaje10bits:954,voltaje:4.663,tiempo:13.70,voltaje10bits:954,voltaje:4.668,tiempo:13.75,voltaje10bits:955,voltaje:4.668,tiempo:13.79,voltaje10bits:955,voltaje:4.668,tiempo:13.84,voltaje10bits:956,voltaje:4.673,tiempo:13.89,voltaje10bits:957,voltaje:4.677,tiempo:13.93,voltaje10bits:957,voltaje:4.682,tiempo:13.98,voltaje10bits:958,voltaje:4.682,tiempo:14.03,voltaje10bits:959,voltaje:4.687,tiempo:14.07,voltaje10bits:959,voltaje:4.682,tiempo:14.12,voltaje10bits:959,voltaje:4.687,tiempo:14.17,voltaje10bits:960,voltaje:4.697,tiempo:14.21,voltaje10bits:961,voltaje:4.692,tiempo:14.26,voltaje10bits:962,voltaje:4.697,tiempo:14.31,voltaje10bits:961,voltaje:4.697,tiempo:14.35,voltaje10bits:961,voltaje:4.702,tiempo:14.40,voltaje10bits:962,voltaje:4.702,tiempo:14.45,voltaje10bits:963,voltaje:4.712,tiempo:14.50,voltaje10bits:963,voltaje:4.712,tiempo:14.54,voltaje10bits:964,voltaje:4.717,tiempo:14.59,voltaje10bits:964,voltaje:4.712,tiempo:14.64,voltaje10bits:964,voltaje:4.717,tiempo:14.68,voltaje10bits:966,voltaje:4.721,tiempo:14.73,voltaje10bits:965,voltaje:4.721,tiempo:14.78,voltaje10bits:967,voltaje:4.721,tiempo:14.82,voltaje10bits:967,voltaje:4.726,tiempo:14.87,voltaje10bits:966,voltaje:4.726,tiempo:14.92,voltaje10bits:967,voltaje:4.731,tiempo:14.96,voltaje10bits:968,voltaje:4.731,tiempo:15.01,voltaje10bits:969,voltaje:4.736,tiempo:15.06,voltaje10bits:969,voltaje:4.736,tiempo:15.10,voltaje10bits:969,voltaje:4.736,tiempo:15.15,voltaje10bits:969,voltaje:4.741,tiempo:15.20,voltaje10bits:970,voltaje:4.741,tiempo:15.24,voltaje10bits:971,voltaje:4.746,tiempo:15.29,voltaje10bits:971,voltaje:4.746,tiempo:15.34,voltaje10bits:972,voltaje:4.751,tiempo:15.38,voltaje10bits:973,voltaje:4.751,tiempo:15.43,voltaje10bits:973,voltaje:4.756,tiempo:15.48,voltaje10bits:974,voltaje:4.756,tiempo:15.52,voltaje10bits:973,voltaje:4.756,tiempo:15.57,voltaje10bits:973,voltaje:4.756,tiempo:15.62,voltaje10bits:974,voltaje:4.761,tiempo:15.66,voltaje10bits:975,voltaje:4.765,tiempo:15.71,voltaje10bits:975,voltaje:4.761,tiempo:15.76,voltaje10bits:975,voltaje:4.765,tiempo:15.81,voltaje10bits:975,voltaje:4.765,tiempo:15.85,voltaje10bits:975,voltaje:4.775,tiempo:15.90,voltaje10bits:976,voltaje:4.770,tiempo:15.95,voltaje10bits:978,voltaje:4.770,tiempo:15.99,voltaje10bits:977,voltaje:4.770,tiempo:16.04,voltaje10bits:977,voltaje:4.780,tiempo:16.09,voltaje10bits:978,voltaje:4.780,tiempo:16.13,voltaje10bits:978,voltaje:4.785,tiempo:16.18,voltaje10bits:979,voltaje:4.785,tiempo:16.23,voltaje10bits:979,voltaje:4.780,tiempo:16.27,voltaje10bits:978,voltaje:4.785,tiempo:16.32,voltaje10bits:979,voltaje:4.790,tiempo:16.37,voltaje10bits:980,voltaje:4.790,tiempo:16.41,voltaje10bits:980,voltaje:4.790,tiempo:16.46,voltaje10bits:980,voltaje:4.795,tiempo:16.51,voltaje10bits:981,voltaje:4.790,tiempo:16.55,voltaje10bits:981,voltaje:4.795,tiempo:16.60,voltaje10bits:981,voltaje:4.804,tiempo:16.65,voltaje10bits:982,voltaje:4.800,tiempo:16.69,voltaje10bits:981,voltaje:4.800,tiempo:16.74,voltaje10bits:983,voltaje:4.800,tiempo:16.79,voltaje10bits:982,voltaje:4.804,tiempo:16.83,voltaje10bits:983,voltaje:4.809,tiempo:16.88,voltaje10bits:983,voltaje:4.814,tiempo:16.93,voltaje10bits:984,voltaje:4.809,tiempo:16.97,voltaje10bits:984,voltaje:4.809,tiempo:17.02,voltaje10bits:984,voltaje:4.814,tiempo:17.07,voltaje10bits:985,voltaje:4.819,tiempo:17.12,voltaje10bits:985,voltaje:4.814,tiempo:17.16,voltaje10bits:985,voltaje:4.814,tiempo:17.21,voltaje10bits:985,voltaje:4.819,tiempo:17.26,voltaje10bits:985,voltaje:4.819,tiempo:17.30,voltaje10bits:986,voltaje:4.824,tiempo:17.35,voltaje10bits:986,voltaje:4.819,tiempo:17.40,voltaje10bits:987,voltaje:4.819,tiempo:17.44,voltaje10bits:988,voltaje:4.819,tiempo:17.49,voltaje10bits:988,voltaje:4.824,tiempo:17.54,voltaje10bits:987,voltaje:4.829,tiempo:17.58,voltaje10bits:987,voltaje:4.834,tiempo:17.63,voltaje10bits:989,voltaje:4.829,tiempo:17.68,voltaje10bits:989,voltaje:4.829,tiempo:17.72,voltaje10bits:990,voltaje:4.834,tiempo:17.77,voltaje10bits:989,voltaje:4.834,tiempo:17.82,voltaje10bits:989,voltaje:4.839,tiempo:17.86,voltaje10bits:989,voltaje:4.834,tiempo:17.91,voltaje10bits:989,voltaje:4.834,tiempo:17.96,voltaje10bits:990,voltaje:4.839,tiempo:18.00,voltaje10bits:990,voltaje:4.844,tiempo:18.05,voltaje10bits:990,voltaje:4.844,tiempo:18.10,voltaje10bits:991,voltaje:4.844,tiempo:18.14,voltaje10bits:992,voltaje:4.839,tiempo:18.19,voltaje10bits:991,voltaje:4.844,tiempo:18.24,voltaje10bits:992,voltaje:4.844,tiempo:18.28,voltaje10bits:991,voltaje:4.853,tiempo:18.33,voltaje10bits:993,voltaje:4.844,tiempo:18.38,voltaje10bits:992,voltaje:4.848,tiempo:18.43,voltaje10bits:992,voltaje:4.853,tiempo:18.47,voltaje10bits:993,voltaje:4.848,tiempo:18.52,voltaje10bits:992,voltaje:4.853,tiempo:18.57,voltaje10bits:993,voltaje:4.853,tiempo:18.61,voltaje10bits:994,voltaje:4.858,tiempo:18.66,voltaje10bits:993,voltaje:4.853,tiempo:18.71,voltaje10bits:993,voltaje:4.853,tiempo:18.75,voltaje10bits:993,voltaje:4.858,tiempo:18.80,voltaje10bits:995,voltaje:4.863,tiempo:18.85,voltaje10bits:995,voltaje:4.863,tiempo:18.89,voltaje10bits:994,voltaje:4.858,tiempo:18.94,voltaje10bits:996,voltaje:4.858,tiempo:18.99,voltaje10bits:994,voltaje:4.863,tiempo:19.03,voltaje10bits:995,voltaje:4.863,tiempo:19.08,voltaje10bits:996,voltaje:4.863,tiempo:19.13,voltaje10bits:996,voltaje:4.863,tiempo:19.17,voltaje10bits:996,voltaje:4.868,tiempo:19.22,voltaje10bits:996,voltaje:4.868,tiempo:19.27,voltaje10bits:996,voltaje:4.868,tiempo:19.31,voltaje10bits:996,voltaje:4.868,tiempo:19.36,voltaje10bits:997,voltaje:4.873,tiempo:19.41,voltaje10bits:997,voltaje:4.873,tiempo:19.45,voltaje10bits:997,voltaje:4.873,tiempo:19.50,voltaje10bits:997,voltaje:4.873,tiempo:19.55,voltaje10bits:998,voltaje:4.878,tiempo:19.59,voltaje10bits:998,voltaje:4.878,tiempo:19.64,voltaje10bits:998,voltaje:4.878,tiempo:19.69,voltaje10bits:997,voltaje:4.878,tiempo:19.74,voltaje10bits:997,voltaje:4.878,tiempo:19.78,voltaje10bits:998,voltaje:4.883,tiempo:19.83,voltaje10bits:999,voltaje:4.883,tiempo:19.88,voltaje10bits:999,voltaje:4.878,tiempo:19.92,voltaje10bits:998,voltaje:4.883,tiempo:19.97,voltaje10bits:999,voltaje:4.883,tiempo:20.02,voltaje10bits:999,voltaje:4.883,tiempo:20.06,voltaje10bits:1001,voltaje:4.883,tiempo:20.11,voltaje10bits:1000,voltaje:4.888,tiempo:20.16,voltaje10bits:1000,voltaje:4.888,tiempo:20.21,voltaje10bits:999,voltaje:4.888,tiempo:20.25,voltaje10bits:1000,voltaje:4.888,tiempo:20.30,voltaje10bits:1000,voltaje:4.888,tiempo:20.35,voltaje10bits:1002,voltaje:4.888,tiempo:20.40,voltaje10bits:1000,voltaje:4.888,tiempo:20.44,voltaje10bits:1001,voltaje:4.892,tiempo:20.49,voltaje10bits:1001,voltaje:4.888,tiempo:20.54,voltaje10bits:1000,voltaje:4.892,tiempo:20.59,voltaje10bits:1001,voltaje:4.892,tiempo:20.64,voltaje10bits:1000,voltaje:4.892,tiempo:20.68,voltaje10bits:1003,voltaje:4.892,tiempo:20.73,voltaje10bits:1002,voltaje:4.897,tiempo:20.78,voltaje10bits:1002,voltaje:4.892,tiempo:20.83,voltaje10bits:1002,voltaje:4.892,tiempo:20.87,voltaje10bits:1001,voltaje:4.897,tiempo:20.92,voltaje10bits:1003,voltaje:4.897,tiempo:20.97,voltaje10bits:1002,voltaje:4.897,tiempo:21.02,voltaje10bits:1003,voltaje:4.897,tiempo:21.07,voltaje10bits:1003,voltaje:4.902,tiempo:21.11,voltaje10bits:1002,voltaje:4.897,tiempo:21.16,voltaje10bits:1003,voltaje:4.902,tiempo:21.21,voltaje10bits:1003,voltaje:4.902,tiempo:21.26,voltaje10bits:1004,voltaje:4.902,tiempo:21.31,voltaje10bits:1003,voltaje:4.907,tiempo:21.35,voltaje10bits:1004,voltaje:4.902,tiempo:21.40,voltaje10bits:1004,voltaje:4.902,tiempo:21.45,voltaje10bits:1004,voltaje:4.907,tiempo:21.50,voltaje10bits:1004,voltaje:4.912,tiempo:21.54,voltaje10bits:1004,voltaje:4.902,tiempo:21.59,voltaje10bits:1004,voltaje:4.912,tiempo:21.64,voltaje10bits:1004,voltaje:4.912,tiempo:21.69,voltaje10bits:1004,voltaje:4.917,tiempo:21.74,voltaje10bits:1005,voltaje:4.912,tiempo:21.78,voltaje10bits:1005,voltaje:4.912,tiempo:21.83,voltaje10bits:1005,voltaje:4.907,tiempo:21.88,voltaje10bits:1005,voltaje:4.917,tiempo:21.93,voltaje10bits:1006,voltaje:4.907,tiempo:21.97,voltaje10bits:1005,voltaje:4.917,tiempo:22.02,voltaje10bits:1005,voltaje:4.912,tiempo:22.07,voltaje10bits:1005,voltaje:4.917,tiempo:22.12,voltaje10bits:1006,voltaje:4.917,tiempo:22.17,voltaje10bits:1006,voltaje:4.917,tiempo:22.21,voltaje10bits:1007,voltaje:4.912,tiempo:22.26,voltaje10bits:1006,voltaje:4.922,tiempo:22.31,voltaje10bits:1006,voltaje:4.922,tiempo:22.36,voltaje10bits:1006,voltaje:4.917,tiempo:22.41,voltaje10bits:1006,voltaje:4.917,tiempo:22.45,voltaje10bits:1006,voltaje:4.922,tiempo:22.50,voltaje10bits:1007,voltaje:4.922,tiempo:22.55,voltaje10bits:1006,voltaje:4.917,tiempo:22.60,voltaje10bits:1007,voltaje:4.917,tiempo:22.64,voltaje10bits:1007,voltaje:4.927,tiempo:22.69,voltaje10bits:1007,voltaje:4.922,tiempo:22.74,voltaje10bits:1007,voltaje:4.917,tiempo:22.79,voltaje10bits:1006,voltaje:4.922,tiempo:22.84,voltaje10bits:1007,voltaje:4.927,tiempo:22.88,voltaje10bits:1007,voltaje:4.932,tiempo:22.93,voltaje10bits:1007,voltaje:4.922,tiempo:22.98,voltaje10bits:1007,voltaje:4.922,tiempo:23.03,voltaje10bits:1007,voltaje:4.932,tiempo:23.07,voltaje10bits:1008,voltaje:4.927,tiempo:23.12,voltaje10bits:1008,voltaje:4.927,tiempo:23.17,voltaje10bits:1008,voltaje:4.922,tiempo:23.22,voltaje10bits:1008,voltaje:4.932,tiempo:23.27,voltaje10bits:1008,voltaje:4.932,tiempo:23.31,voltaje10bits:1008,voltaje:4.927,tiempo:23.36,voltaje10bits:1008,voltaje:4.927,tiempo:23.41,voltaje10bits:1009,voltaje:4.927,tiempo:23.46,voltaje10bits:1009,voltaje:4.927,tiempo:23.51,voltaje10bits:1008,voltaje:4.927,tiempo:23.55,voltaje10bits:1008,voltaje:4.932,tiempo:23.60,voltaje10bits:1010,voltaje:4.932,tiempo:23.65,voltaje10bits:1009,voltaje:4.927,tiempo:23.70,voltaje10bits:1009,voltaje:4.932,tiempo:23.74,voltaje10bits:1009,voltaje:4.927,tiempo:23.79,voltaje10bits:1010,voltaje:4.932,tiempo:23.84,voltaje10bits:1009,voltaje:4.932,tiempo:23.89,voltaje10bits:1009,voltaje:4.932,tiempo:23.94,voltaje10bits:1010,voltaje:4.932,tiempo:23.98,voltaje10bits:1009,voltaje:4.932,tiempo:24.03,voltaje10bits:1010,voltaje:4.941,tiempo:24.08,voltaje10bits:1009,voltaje:4.932,tiempo:24.13,voltaje10bits:1010,voltaje:4.932,tiempo:24.17,voltaje10bits:1010,voltaje:4.936,tiempo:24.22,voltaje10bits:1010,voltaje:4.932,tiempo:24.27,voltaje10bits:1010,voltaje:4.936,tiempo:24.32,voltaje10bits:1010,voltaje:4.936,tiempo:24.37,voltaje10bits:1010,voltaje:4.936,tiempo:24.41,voltaje10bits:1010,voltaje:4.936,tiempo:24.46,voltaje10bits:1010,voltaje:4.936,tiempo:24.51,voltaje10bits:1010,voltaje:4.936,tiempo:24.56,voltaje10bits:1011,voltaje:4.936,tiempo:24.61,voltaje10bits:1010,voltaje:4.941,tiempo:24.65,voltaje10bits:1010,voltaje:4.941,tiempo:24.70,voltaje10bits:1010,voltaje:4.941,tiempo:24.75,voltaje10bits:1011,voltaje:4.941,tiempo:24.80,voltaje10bits:1011,voltaje:4.941,tiempo:24.84,voltaje10bits:1011,voltaje:4.941,tiempo:24.89,voltaje10bits:1010,voltaje:4.936,tiempo:24.94,voltaje10bits:1010,voltaje:4.941,tiempo:24.99,voltaje10bits:1011,voltaje:4.946,tiempo:25.04,voltaje10bits:1011,voltaje:4.941,tiempo:25.08,voltaje10bits:1012,voltaje:4.941,tiempo:25.13,voltaje10bits:1011,voltaje:4.941,tiempo:25.18,voltaje10bits:1011,voltaje:4.941,tiempo:25.23,voltaje10bits:1011,voltaje:4.941,tiempo:25.27,voltaje10bits:1012,voltaje:4.941,tiempo:25.32,voltaje10bits:1011,voltaje:4.951,tiempo:25.37,voltaje10bits:1011,voltaje:4.951,tiempo:25.42,voltaje10bits:1011,voltaje:4.941,tiempo:25.47,voltaje10bits:1012,voltaje:4.951,tiempo:25.51,voltaje10bits:1011,voltaje:4.946,tiempo:25.56,voltaje10bits:1012,voltaje:4.946,tiempo:25.61,voltaje10bits:1012,voltaje:4.941,tiempo:25.66,voltaje10bits:1012,voltaje:4.946,tiempo:25.71,voltaje10bits:1012,voltaje:4.946,tiempo:25.75,voltaje10bits:1012,voltaje:4.946,tiempo:25.80,voltaje10bits:1012,voltaje:4.946,tiempo:25.85,voltaje10bits:1013,voltaje:4.951,tiempo:25.90,voltaje10bits:1012,voltaje:4.946,tiempo:25.94,voltaje10bits:1013,voltaje:4.951,tiempo:25.99,voltaje10bits:1013,voltaje:4.951,tiempo:26.04,voltaje10bits:1014,voltaje:4.946,tiempo:26.09,voltaje10bits:1013,voltaje:4.951,tiempo:26.14,voltaje10bits:1012,voltaje:4.946,tiempo:26.18,voltaje10bits:1013,voltaje:4.951,tiempo:26.23,voltaje10bits:1012,voltaje:4.946,tiempo:26.28,voltaje10bits:1012,voltaje:4.946,tiempo:26.33,voltaje10bits:1011,voltaje:4.946,tiempo:26.37,voltaje10bits:1013,voltaje:4.946,tiempo:26.42,voltaje10bits:1012,voltaje:4.951,tiempo:26.47,voltaje10bits:1012,voltaje:4.951,tiempo:26.52,voltaje10bits:1014,voltaje:4.951,tiempo:26.57,voltaje10bits:1013,voltaje:4.956,tiempo:26.61,voltaje10bits:1013,voltaje:4.951,tiempo:26.66,voltaje10bits:1014,voltaje:4.956,tiempo:26.71,voltaje10bits:1014,voltaje:4.951,tiempo:26.76,voltaje10bits:1014,voltaje:4.951,tiempo:26.81,voltaje10bits:1013,voltaje:4.956,tiempo:26.85,voltaje10bits:1014,voltaje:4.956,tiempo:26.90,voltaje10bits:1013,voltaje:4.951,tiempo:26.95,voltaje10bits:1013,voltaje:4.956,tiempo:27.00,voltaje10bits:1015,voltaje:4.956,tiempo:27.04,voltaje10bits:1013,voltaje:4.956,tiempo:27.09,voltaje10bits:1014,voltaje:4.951,tiempo:27.14,voltaje10bits:1013,voltaje:4.956,tiempo:27.19,voltaje10bits:1013,voltaje:4.951,tiempo:27.24,voltaje10bits:1015,voltaje:4.956,tiempo:27.28,voltaje10bits:1014,voltaje:4.951,tiempo:27.33,voltaje10bits:1014,voltaje:4.956,tiempo:27.38,voltaje10bits:1013,voltaje:4.956,tiempo:27.43,voltaje10bits:1014,voltaje:4.956,tiempo:27.47,voltaje10bits:1014,voltaje:4.956,tiempo:27.52,voltaje10bits:1014,voltaje:4.961,tiempo:27.57,voltaje10bits:1014,voltaje:4.956,tiempo:27.62,voltaje10bits:1014,voltaje:4.956,tiempo:27.67,voltaje10bits:1014,voltaje:4.956,tiempo:27.71,voltaje10bits:1014,voltaje:4.961,tiempo:27.76,voltaje10bits:1015,voltaje:4.956,tiempo:27.81,voltaje10bits:1015,voltaje:4.956,tiempo:27.86,voltaje10bits:1014,voltaje:4.956,tiempo:27.91,voltaje10bits:1014,voltaje:4.961,tiempo:27.95,voltaje10bits:1015,voltaje:4.961,tiempo:28.00,voltaje10bits:1015,voltaje:4.956,tiempo:28.05,voltaje10bits:1014,voltaje:4.956,tiempo:28.10,voltaje10bits:1014,voltaje:4.956,tiempo:28.14,voltaje10bits:1016,voltaje:4.961,tiempo:28.19,voltaje10bits:1014,voltaje:4.956,tiempo:28.24,voltaje10bits:1014,voltaje:4.961,tiempo:28.29,voltaje10bits:1015,voltaje:4.961,tiempo:28.34,voltaje10bits:1016,voltaje:4.956,tiempo:28.38,voltaje10bits:1014,voltaje:4.961,tiempo:28.43,voltaje10bits:1015,voltaje:4.961,tiempo:28.48,voltaje10bits:1016,voltaje:4.961,tiempo:28.53,voltaje10bits:1016,voltaje:4.956,tiempo:28.57,voltaje10bits:1015,voltaje:4.961,tiempo:28.62,voltaje10bits:1015,voltaje:4.961,tiempo:28.67,voltaje10bits:1015,voltaje:4.961,tiempo:28.72,voltaje10bits:1015,voltaje:4.961,tiempo:28.77,voltaje10bits:1015,voltaje:4.961,tiempo:28.81,voltaje10bits:1015,voltaje:4.961,tiempo:28.86,voltaje10bits:1015,voltaje:4.961,tiempo:28.91,voltaje10bits:1015,voltaje:4.961,tiempo:28.96,voltaje10bits:1015,voltaje:4.961,tiempo:29.01,voltaje10bits:1015,voltaje:4.966,tiempo:29.05,voltaje10bits:1015,voltaje:4.961,tiempo:29.10,voltaje10bits:1015,voltaje:4.961,tiempo:29.15,voltaje10bits:1015,voltaje:4.966,tiempo:29.20,voltaje10bits:1016,voltaje:4.961,tiempo:29.24,voltaje10bits:1015,voltaje:4.961,tiempo:29.29,voltaje10bits:1015,voltaje:4.961,tiempo:29.34,voltaje10bits:1015,voltaje:4.961,tiempo:29.39,voltaje10bits:1016,voltaje:4.961,tiempo:29.44,voltaje10bits:1016,voltaje:4.961,tiempo:29.48,voltaje10bits:1016,voltaje:4.961,tiempo:29.53,voltaje10bits:1016,voltaje:4.966,tiempo:29.58,voltaje10bits:1016,voltaje:4.966,tiempo:29.63,voltaje10bits:1016,voltaje:4.966,tiempo:29.67,voltaje10bits:1015,voltaje:4.966,tiempo:29.72,voltaje10bits:1016,voltaje:4.966,tiempo:29.77,voltaje10bits:1015,voltaje:4.971,tiempo:29.82,voltaje10bits:1016,voltaje:4.966,tiempo:29.87,voltaje10bits:1015,voltaje:4.966,tiempo:29.91,voltaje10bits:1016,voltaje:4.966,tiempo:29.96,voltaje10bits:1017,voltaje:4.961,tiempo:30.01,voltaje10bits:1015,voltaje:4.966,tiempo:30.06,voltaje10bits:1016,voltaje:4.971,tiempo:30.11,voltaje10bits:1017,voltaje:4.966,tiempo:30.15,voltaje10bits:1016,voltaje:4.966,tiempo:30.20,voltaje10bits:1017,voltaje:4.966,tiempo:30.25,voltaje10bits:1017,voltaje:4.966,tiempo:30.30,voltaje10bits:1016,voltaje:4.966,tiempo:30.34,voltaje10bits:1016,voltaje:4.966,tiempo:30.39,voltaje10bits:1016,voltaje:4.971,tiempo:30.44,voltaje10bits:1016,voltaje:4.966,tiempo:30.49,voltaje10bits:1016,voltaje:4.966,tiempo:30.54,voltaje10bits:1016,voltaje:4.966,tiempo:30.58,voltaje10bits:1016,voltaje:4.971,tiempo:30.63,voltaje10bits:1016,voltaje:4.971,tiempo:30.68,voltaje10bits:1017,voltaje:4.966,tiempo:30.73,voltaje10bits:1017,voltaje:4.966,tiempo:30.77,voltaje10bits:1016,voltaje:4.966,tiempo:30.82,voltaje10bits:1017,voltaje:4.966,tiempo:30.87,voltaje10bits:1015,voltaje:4.966,tiempo:30.92,voltaje10bits:1017,voltaje:4.966,tiempo:30.97,voltaje10bits:1017,voltaje:4.966,tiempo:31.01,voltaje10bits:1016,voltaje:4.966,tiempo:31.06,voltaje10bits:1017,voltaje:4.966,tiempo:31.11,voltaje10bits:1016,voltaje:4.966,tiempo:31.16,voltaje10bits:1016,voltaje:4.971,tiempo:31.21,voltaje10bits:1017,voltaje:4.971,tiempo:31.25,voltaje10bits:1016,voltaje:4.966,tiempo:31.30,voltaje10bits:1017,voltaje:4.966,tiempo:31.35,voltaje10bits:1016,voltaje:4.966,tiempo:31.40,voltaje10bits:1017,voltaje:4.966,tiempo:31.44,voltaje10bits:1015,voltaje:4.971,tiempo:31.49,voltaje10bits:1017,voltaje:4.976,tiempo:31.54,voltaje10bits:1017,voltaje:4.971,tiempo:31.59,voltaje10bits:1017,voltaje:4.971,tiempo:31.64,voltaje10bits:1017,voltaje:4.971,tiempo:31.68,voltaje10bits:1016,voltaje:4.971,tiempo:31.73,voltaje10bits:1016,voltaje:4.971,tiempo:31.78,voltaje10bits:1017,voltaje:4.966,tiempo:31.83,voltaje10bits:1017,voltaje:4.971,tiempo:31.87,voltaje10bits:1016,voltaje:4.971,tiempo:31.92,voltaje10bits:1016,voltaje:4.971,tiempo:31.97,voltaje10bits:1018,voltaje:4.971,tiempo:32.02,voltaje10bits:1017,voltaje:4.966,tiempo:32.07,voltaje10bits:1017,voltaje:4.976,tiempo:32.11,voltaje10bits:1016,voltaje:4.966,tiempo:32.16,voltaje10bits:1017,voltaje:4.971,tiempo:32.21,voltaje10bits:1017,voltaje:4.971,tiempo:32.26,voltaje10bits:1017,voltaje:4.971,tiempo:32.31,voltaje10bits:1017,voltaje:4.976,tiempo:32.35,voltaje10bits:1017,voltaje:4.971,tiempo:32.40,voltaje10bits:1017,voltaje:4.971,tiempo:32.45,voltaje10bits:1016,voltaje:4.971,tiempo:32.50,voltaje10bits:1018,voltaje:4.966,tiempo:32.54,voltaje10bits:1016,voltaje:4.971,tiempo:32.59,voltaje10bits:1017,voltaje:4.976,tiempo:32.64,voltaje10bits:1017,voltaje:4.971,tiempo:32.69,voltaje10bits:1018,voltaje:4.971,tiempo:32.74,voltaje10bits:1017,voltaje:4.971"

# Dividir los datos en una lista de pares variable:valor
data_pairs = data_str.split(',')

# Inicializar arrays para almacenar los valores
tiempo= []
voltaje10bits= []
voltaje= []

# Iterar sobre los pares variable:valor y almacenar en los arrays correspondientes
for pair in data_pairs:
    variable, valor = pair.split(':')
    if variable == 'tiempo':
        tiempo.append(float(valor))
    elif variable == 'voltaje10bits':
        voltaje10bits.append(int(valor))
    elif variable == 'voltaje':
        voltaje.append(float(valor))

# Imprimir los arrays resultantes

print("Longitud de Tiempo:", len(tiempo))
print("Longitud de Voltaje 10 bits:", len(voltaje10bits))
print("Longitud de Voltaje:", len(voltaje))

# Convertir las listas a arrays de NumPy
arr_tiempo = np.array(tiempo)
arr_voltaje = np.array(voltaje)

# Función exponencial
def exponential_func(t, Vmax, RC):
    return Vmax * (1 - np.exp(-t / RC))


params, covariance = curve_fit(exponential_func, arr_tiempo, arr_voltaje)


# Obtener los parámetros ajustados
Vmax_fit, RC_fit = params

# Coeficiente de correlación (R cuadrado)
residuals = arr_voltaje - exponential_func(arr_tiempo, Vmax_fit, RC_fit)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((arr_voltaje - np.mean(arr_voltaje))**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"R cuadrado: {r_squared:.2f}")


# Valor de la línea horizontal previamente calculada
horizontal_line = (1 - 1/np.e) * Vmax_fit

# Calcular punto de intersección
intersection_point = (RC_fit * np.log(Vmax_fit / (Vmax_fit - horizontal_line)), horizontal_line)

# Crear el gráfico
plt.figure(figsize=(8, 6))

# Agregar la línea horizontal y la línea vertical
plt.axhline(y=horizontal_line, color='green', linestyle='--', label='(1-1/e)Vmax')
plt.axvline(x=intersection_point[0], color='blue', linestyle='--', label='RC')

# Gráfico de los datos originales y la curva ajustada
plt.scatter(arr_tiempo, arr_voltaje, label='Datos')
plt.plot(arr_tiempo, exponential_func(arr_tiempo, Vmax_fit, RC_fit), color='red', label='Regresión Exponencial')

# Etiquetas y leyendas
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')
plt.title('Voltaje Vs Tiempo del capacitor en carga')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()

# Imprimir la ecuación de la regresión
print("\nEcuación de la regresión exponencial:")
print("V(t) =", (Vmax_fit), " * (1 - exp(-t /", RC_fit, "))")
print("\nRedondeado se obtiene:")
print(f"V(t) = {(Vmax_fit):.2f} * (1 - exp(-t /{RC_fit:.2f}))")

# valor de la resistencia conocida en ohmios (Ω)
resistencia_ohmios = 10000

capacitancia =  RC_fit  / resistencia_ohmios * 1e6
   

print(f"Capacitancia: {capacitancia:.2f} µF")

