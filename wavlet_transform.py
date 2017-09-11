# -*- coding: utf-8 -*-
import csv

import pywt
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate


def main():
    # file_name = str(raw_input('Please input file name:\n'))
    # data_size = int(raw_input('Input data size:\n'))
    # csv_file_name = str(raw_input('Please input csv file name:\n'))
    file_name = 'signal.dtu'
    # data_size = 100
    csv_file_name = 'qwerty.csv'
    time, sig_1_1, sig_1_3, sig_2_1, sig_2_2, sig_3_1, sig_3_3 = get_data(file_name)
    approximation, detail_coefficients= wavelet_transformation(sig_1_1, sig_1_3, sig_2_1, sig_2_2, sig_3_1, sig_3_3)
    # write_csv(sig_3_3, approximation, detail_coefficients, time, csv_file_name)
    draw_plot(approximation, detail_coefficients, time)

def get_data(file_name):
    time, sig_1_1, sig_1_3, sig_2_1, sig_2_2, sig_3_1, sig_3_3 = [], [], [], [], [], [], []
    with open(file_name, 'r') as text_file:
        for line in text_file:
            arr = []
            for value in line.strip().split('\t'):
                try:
                    value = float(value.strip('﻿'))
                    arr.append(value)
                except ValueError:
                    break
            if not len(arr) == 0:
                time.append(arr[0])
                sig_1_1.append(arr[1])
                sig_1_3.append(arr[2])
                sig_2_1.append(arr[3])
                sig_2_2.append(arr[4])
                sig_3_1.append(arr[5])
                sig_3_3.append(arr[6])
    return time, sig_1_1, sig_1_3, sig_2_1, sig_2_2, sig_3_1, sig_3_3


def wavelet_transformation(sig_1_1, sig_1_3, sig_2_1, sig_2_2, sig_3_1, sig_3_3):
    approximation, detail_coefficients = pywt.dwt(sig_3_3, 'sym7')
    # approximation, detail_coefficients = approximation[:data_size], detail_coefficients
    # time = np.arange(0, len(approximation), 10)
    return approximation, detail_coefficients


def draw_plot(approximation, detail_coefficients, time):
    time = np.array(time)
    xi, yi = np.linspace(approximation.min(), approximation.max(), approximation.size), np.linspace(time.min(), time.max(), approximation.size)
    xi, yi = np.meshgrid(xi, yi)

    rbf = scipy.interpolate.Rbf(approximation, time[:approximation.size], detail_coefficients, function='linear')
    zi = rbf(xi, yi)

    plt.imshow(zi, vmin=detail_coefficients.min(), vmax=detail_coefficients.max(), origin='lower',
               extent=[time.min(), time.max(), approximation.min(), approximation.max()])
    plt.colorbar()
    plt.show()


def write_csv(sig_3_3, approximation, detail_coefficients, time, csv_file_name):
        with open(csv_file_name,'a') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            fields = ['Original Signal', 'Approximation', 'Detail Coefficients', 'Time']
            writer.writerow(fields)
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for i, value in enumerate(approximation):
                writer.writerow([sig_3_3[i], approximation[i], detail_coefficients[i], time[i]])

if __name__ == '__main__':
    main()
