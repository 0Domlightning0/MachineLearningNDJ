test_string = "675	225	150	165	220	275	295	255	215	190	225	140	235	305	275	210	275	230	410	325	125	210	270	235	405	165	255	530	125	215	350	420	320	630	240	135	355	225	245	180	260	185	345	320	255	355	280	200	155	630	315	175	180	560	250	150	365	500	195	175	285	180	235	275	290	325	495	265	475	165	390	325	265	545	290	290	120	355	210	155	165	170	285	240	265	255	355	150	440	225	280	365	450	315	130	195	175	150	205	125	145	325	295	470	230	125	285	385	170	235	200	125	185	325	275	255	370	210	410	340	170	195	190	140	250	150	220	415	200	130	225	130	250	135	135	160	255	270	165	185	100	340	335	125	210	250	285	260	180	250	230	245	235	200	280	210	210	130	430	380	225	245	95	200	340	170	145	85	145	180	125	260	245	400	405	520	400	435	250	265	360	450	90	125	270	510	160	145	460	420	255	595	240	305	715	690	365	115	620	320	215	230	225	455	235	365	250	245	380	410	695	230	465	215	360	475	160	230	375	310	660	235	280	280	575	160	590	400	325	390	285	420	295	350	190	235	345	325	390	380	315	285	320	445	245	225	435	390	435	490	330	220	525	190	340	410	335	195	315	520	245	275	225	220	255	195	130	355	365	385	410	425	265	265	395	270	215	305	515	280	320	445	490	375	300	490	235	470	300	140	205	240	355	590	150	345	230	380	325	485	350	475	465	555	350	265	500	255	240	520	315	460	270	625	205	310	265	360	340	310	480	485	265	540	240	325	255	445	400	240	650	275	490	270	345	205	305	315	385	255	285	175	400	520	220	310	325	290	310	370	510	270	270	280	410	265	335	275	500	350	460	290	595	305	420	490	575	615	395	555	325	160	450	390	610	390	565	335	195	300	235	365	360	605	205	545	490	230	340	210	330	170	195	195	460	220	310	250	390	500	145	375	370	410	315	270	360	435	280	440	365	170	540	330	365	305	185	165	220	355	270	335	240	215	300	150	345	260	495	215	445	600	245	450	555	620	255	705	630	185	435	285	455	300	295	130	350	170	450	225	325	165	380	395	475	415	260	235	180	315	235	490	310	525	445	300	245	230	255	290	235	125	520	410	450	285	370	530	230	425	335	370	570	470	175	350	155	380	280	415	315	350	355	570	380	325	420	300	400	245	245	265	415	430	315	385	275	275	570	475	475	460	250	470	300	300	190	170	165	235	225	390	340	250	130	430	420	160	285	275	530	170	140	90	145	190	205	240	270	265	305	220	500	160	230	375	235	210	360	225	170	180	180	170	170	195	510	230	355	180	390	200	330	465	335	210	485	430	505	720	895	210	325	260	235	200	325	480	250	295	575	400	590	480	325	385	275	470	390	305	270	545	520	335	355	445	570	955	350	395	270	320	500	260	1020	570	245	505	460	530	215	795	435	955	875	510	625	315	305	400	875	405	215	410	505	740	750	410	280	935	570	735	780	940	940	390	875	760	370	635	390	340	575	605	405	315	530	335	195	385	390	830	455	260	545	290	355	640	365	370	565	185	300	550	1060	995	1095	290	345	1145	500	795	615	810	495	815	1085	625	515	645	595	995	620	1045	615	645	680	890	240	565	555	440	990	485	1010	565	815	490	805	600"
new_String = ""
count = 0

# Python3 code to demonstrate
# getting numbers from string

# initializing string


# printing original string
print("The original string : " + test_string)


# getting numbers from string
res = []
x=test_string.split()
for i in x:
	if i.isnumeric():
		res.append(int(i))

# print result
print("The numbers list is : " + str(res))