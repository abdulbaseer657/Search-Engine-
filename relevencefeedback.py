totalQueryVectors = []
totalQueryVectors.append(query_vector)
while(1):
    relFedd = str(raw_input("Enter space seprated relevant documents (-1 to exit): "))
    relFedd = relFedd.split()
    
    if int(relFedd[0])!=-1:

        relVectors = []
        non_relVectors = []

        for i in range(len(relFedd)):
            ind_val = int(relFedd[i])
            t_Vect = tfresults[sorted_sim_results[ind_val][0]]
            relVectors.append(t_Vect)

        for i in range(len(sorted_sim_results)):
            if str(i) not in relFedd:
                t_Vect = tfresults[sorted_sim_results[i][0]]
                non_relVectors.append(t_Vect)

        mean_rel_vector = np.zeros(len(relVectors[0]))

        for i in range(len(relVectors)):
            tv = np.array(relVectors[i])
            mean_rel_vector+=tv
        mean_rel_vector = mean_rel_vector/len(relVectors)

        mean_non_rel_vector = np.zeros(len(non_relVectors[0]))

        for i in range(len(non_relVectors)):
            tv = np.array(non_relVectors[i])
            mean_non_rel_vector+=tv
        mean_non_rel_vector = mean_non_rel_vector/len(non_relVectors)



        query_vector = (0.1 * query_vector) + (0.75 * mean_rel_vector) - (0.25 * mean_non_rel_vector)
        cosine_sim_results = {}

        query_vector = np.array(query_vector)

        for k,v in tfresults.iteritems():
            doc_vector = np.array(v)
            simval = cos_sim(query_vector,doc_vector)
            cosine_sim_results[k] = simval

        k_value = 10

        sorted_sim_results = sorted(cosine_sim_results.items(), key=operator.itemgetter(1),reverse=True)
        sorted_sim_results = sorted_sim_results[:k_value]

        print()
        for i in range(len(sorted_sim_results)):
            print(str(i)+"\t"+str(count_to_name[sorted_sim_results[i][0]])+"\t"+str(sorted_sim_results[i][1]))
        totalQueryVectors.append(query_vector)
    else:
        break