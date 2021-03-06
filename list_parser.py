class ListParser:
    def times_inlist(self, list, frequent_number):
        counter = 0
        # for i in range(len(list)):
        for i in list:
            if frequent_number == i:
                counter += 1
        return counter

    def percent_analyzer(self, list, num):

        cropped_list = list[:num]
        result_list = []

        frequent_number_2 = 0
        frequent_number_3 = 0

        frequent_number_1 = max(set(cropped_list), key=cropped_list.count)
        number_1_apparitions = self.times_inlist(cropped_list, frequent_number_1)
        result_list.append((number_1_apparitions / num * 100, frequent_number_1))
        cropped_list = [x for x in cropped_list if x != frequent_number_1]

        if cropped_list != []:
            frequent_number_2 = max(set(cropped_list), key=cropped_list.count)
            number_2_apparitions = self.times_inlist(cropped_list, frequent_number_2)
            cropped_list = [x for x in cropped_list if x != frequent_number_2]
            result_list.append((number_2_apparitions / num * 100, frequent_number_2))

            if cropped_list != []:

                frequent_number_3 = max(set(cropped_list), key=cropped_list.count)
                number_3_apparitions = self.times_inlist(cropped_list, frequent_number_3)
                result_list.append((number_3_apparitions / num * 100, frequent_number_3))
        return result_list


    def stop(self):
        self.status = False
        self.thread.join()
