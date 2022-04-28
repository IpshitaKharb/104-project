import pandas as pd
import statistics 
import csv

df = pd.read_csv('StudentsPerformance.csv')
degree_list=df['"parental level of education"'].to_list()
degree_mean= statistics.mean(degree_list)
degree_median= statistics.median(degree_list)
degree_mode= statistics.mode(degree_list)
degree_standardDeviation= statistics.stdev(degree_list)

print(
    "Mean, Median and Mode of height is {}, {} and {} respectively".format(
        degree_mean, degree_median, degree_mode))

degree_1_std_deviation_start, degree_1_std_deviation_end = degree_mean-degree_standardDeviation, degree_mean+degree_standardDeviation
degree_2_std_deviation_start, degree_2_std_deviation_end = degree_mean-(2*degree_standardDeviation), degree_mean+(2* degree_standardDeviation)
degree_3_std_deviation_start,degree_3_std_deviation_end = degree_mean-(3* degree_standardDeviation), degree_mean+(3* degree_standardDeviation)

height_list_of_data_within_1_std_deviation = [result for result in degree_list if result > degree_1_std_deviation_start and result < degree_1_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in degree_list if result > degree_2_std_deviation_start and result < degree_2_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in degree_list if result > degree_3_std_deviation_start and result < degree_3_std_deviation_end]

print('{} % of data for degree lies within the 1 standard deviation'.format(len(height_list_of_data_within_1_std_deviation)*100.0/len(degree_list)))
print('{} % of data for degree lies within the 2 standard deviation'.format(len(height_list_of_data_within_2_std_deviation)*100.0/len(degree_list)))
print('{} % of data for degree lies within the 3 standard deviation'.format(len(height_list_of_data_within_3_std_deviation)*100.0/len(degree_list)))