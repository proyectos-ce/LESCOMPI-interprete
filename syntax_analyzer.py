from queue import Queue
from collections import Counter
import threading


class SyntaxAnalyzer:
    """
    Does something
    """

    def __init__(self):

        self.queue = Queue()

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
        print("Lista:" + str(list) + "\n")
        print("Lista cortada:" + str(cropped_list) + "\n")

        frequent_number_2 = 0
        frequent_number_3 = 0

        frequent_number_1 = max(set(cropped_list), key=cropped_list.count)
        number_1_apparitions = self.times_inlist(cropped_list, frequent_number_1)
        result_list.append({number_1_apparitions / num * 100, frequent_number_1})
        cropped_list = [x for x in cropped_list if x != frequent_number_1]

        if cropped_list != []:
            frequent_number_2 = max(set(cropped_list), key=cropped_list.count)
            number_2_apparitions = self.times_inlist(cropped_list, frequent_number_2)
            cropped_list = [x for x in cropped_list if x != frequent_number_2]
            result_list.append({number_2_apparitions / num * 100, frequent_number_2})

            if cropped_list != []:

                frequent_number_3 = max(set(cropped_list), key=cropped_list.count)
                number_3_apparitions = self.times_inlist(cropped_list, frequent_number_3)
                result_list.append({number_3_apparitions / num * 100, frequent_number_3})
        print(result_list)
        return result_list


        # print("Numero:"+str(frequent_number_1)+"\n")
        # print("Apariciones:" + str(number_1_apparitions) + "\n")
        # print("Lista:" + str(cropped_list) + "\n")

    def stop(self):
        self.status = False
        self.thread.join()

    # def repeat(self):
    # 	while self.status:
    # 		self.queue.put(self.random_number())
    # 		time.sleep(1/80)

    def get_queue(self):
        return self.queue
