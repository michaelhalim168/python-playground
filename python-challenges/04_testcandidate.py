def test_candidate():
    list_of_nums = [float(i)/10 for i in range(0, 101)]
    
    total = 1000
    candidate_number = 0

    def compute(my_list, data_num, candidate_num):
        return my_list.append((data_num-candidate_num)**2)

    for num in list_of_nums:
        sum_of_num = []
        for data_num in [2, 7, 1, 5, 10]:
            compute(sum_of_num, data_num, num)
        result = sum(sum_of_num)
        if result < total:
            total = result
            candidate_number = num

    print(f"The candidate number is {candidate_number}, the total is {total}.")

test_candidate()